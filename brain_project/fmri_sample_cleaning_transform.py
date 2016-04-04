import pickle
import os
import gzip
import numpy
import scipy.io

sample_per_second = 0.5
max_diff = 0.5

def get_affected_samples(trajectory_path, subject_timeline_path):

    #trajectory = pickle.load(open(trajectory_path, "r"))

    s3 = scipy.io.loadmat(subject_timeline_path, squeeze_me=True)

    ds_cleaner_transform = []

    words = s3['words']

    ds_cleaner_transform = compute_removal_from_start(words, ds_cleaner_transform)
    ds_cleaner_transform = add_padding_to_fill_breaks(words, ds_cleaner_transform)
    ds_cleaner_transform = add_padding_to_fill_gaps(ds_cleaner_transform)

    validate_tansform(ds_cleaner_transform)


    ds_removal_transform = generate_transform_of_samples_to_remove(ds_cleaner_transform)

    return ds_removal_transform

    

def compute_removal_from_start(words, ds_cleaner_transform):

    #load in the start
    first_time = words[0][1]

    start_missing_samples = int(first_time / sample_per_second)

    current_sec_start = 0

    for i in range(0, start_missing_samples):
        ds_cleaner_transform.append(["-", current_sec_start])
        current_sec_start = current_sec_start + 0.5

    return ds_cleaner_transform

def add_padding_to_fill_breaks(words, ds_cleaner_transform):

    for value in words:
        val = value[1]
        
        #it is a normal word...
        if value[2] == 0.5:
            ds_cleaner_transform.append(["+", val])
            
        #if the thing is greater... it's a pause    
        elif value[2] > 0.5:
            #if the thing is greater... it's a pause
            
            
            # get the number of virtual words
            num_virtual_words = int(value[2] / sample_per_second)
            
            for num in range(0, num_virtual_words):
                
                ds_cleaner_transform.append(["-", val])
                val = val + 0.5
            #s_cleaner_transform.append("-")
        else:
            print("error")
            print(value)

    return ds_cleaner_transform

def add_padding_to_fill_gaps(ds_cleaner_transform):
    lower_bound = 0
    upper_bound = 0

    for i in range(0, len(ds_cleaner_transform)):
        
        if i + 1 == len(ds_cleaner_transform):
            break
            
        diff = ds_cleaner_transform[i+1][1] - ds_cleaner_transform[i][1]
            
        if diff > max_diff:
            lower_bound = ds_cleaner_transform[i]
            upper_bound = ds_cleaner_transform[i+1]
            
            num_addins = int(diff / 0.5)
            current_word_time = upper_bound[1] - 0.5
            
            for k in range(0, num_addins-1):
                ds_cleaner_transform.insert(i+1, ["-", current_word_time, "!"])
                current_word_time = current_word_time - 0.5

    return ds_cleaner_transform

def validate_tansform(ds_cleaner_transform):
    temp_array = []
    current_temp_count = 0
    for i in range(0, 2702 * 2):
        temp_array.append(current_temp_count)
        current_temp_count = current_temp_count + 0.5

    #check to ensure we are counting correctly
    for i in range(0, len(ds_cleaner_transform)):
        if ds_cleaner_transform[i][1] != temp_array[i]:
            raise Exception('Values didn\'t allign ' + str(ds_cleaner_transform[i][1]) + "!=" + str(temp_array[i]))

def generate_transform_of_samples_to_remove(ds_cleaner_transform):
    ds_removal_transform = []

    #there should be 4 sameples in each fmri sample - each sample is 2 seconds, 
    #words should appear every 0.5 seconds...therefore we should look in groups of 4
    for i in range(0, len(ds_cleaner_transform), 4):
        sample_words = []
        
        break_count = 0
        
        for j in range(0, 4):
            sample_words.append(ds_cleaner_transform[i + j])
        
        for word in sample_words:
            if word[0] == "-":
                break_count = break_count + 1
                
        #a '+' shall be used to denote a sample to keep, a '-' will be removed
                
        #if the whole 2 seconds was a break, then it should be disgarded, otherwise, it contains some data
        if break_count == 4:
            ds_removal_transform.append("-")
        #if it wasn't a whole, break, then keep it
        else:
            ds_removal_transform.append("+")

    return ds_removal_transform