import numpy as np
from mvpa2.suite import *

class FoldWiseProcessor:

    results = []

    def __init__(self, dataset, trajectory, analyser, number_of_folds, skip_nearest_neighbours=False):
        #store all relevant information
        self.dataset = dataset
        self.trajectory = trajectory
        self.analyser = analyser
        self.number_of_folds = number_of_folds
        self.skip_nearest_neighbours = skip_nearest_neighbours

        #create folds
        #self.chunks = split_ds(self.dataset, number_of_folds)

        fold_num = generate_chunk_transform_for_ds(self.dataset, number_of_folds)
        self.dataset.sa['fold_num'] = fold_num


    def process(self):

        #every time this method is run, it will wipe the current state of #results
        print("starting to process")

        #empty resutls
        self.results = []

        temp_results = []

        #set the turn
        turn = 0

        for i in range(0, self.number_of_folds):
            print("starting turn :/ " + str(turn))
            print("results contains " + str(len(self.results)) + " entries")

            #get the relevant data
            training_set = self.get_trainig_set_chunks_from_original(turn)
            test_set = self.get_test_set_chunk_from_original(turn)

            print(training_set.sa)

            #train the analyser/model
            self.analyser.train(training_set)

            #get the prediction based on the chunks
            predictions = self.analyser.predict(test_set)

            #append the predictions to the global results
            #temp_results.append(predictions)

            # if temp_results is None:
            #     temp_results = predictions.ravel()
            #     print(temp_results)
            #else:
            temp_results.extend(predictions.ravel())

            #increment the turn
            turn = turn + 1

        self.results = temp_results

        print("Finished process")

        return self.results


    def get_current_training_set(self, turn):

        training_set = None

        #loop over all the chunks
        for i in range(0, len(self.chunks)):

            #if skipping the nearest neighbour is enabled, we must validate
            if self.skip_nearest_neighbours:
                if i > 0:
                    if i == turn - 1:
                        break;

                if i < len(self.chunks):
                    if i == turn + 1:
                        break;

            if(i != turn):


                if training_set is None:
                    training_set = np.array(self.chunks[i].samples)
                else:
                    #training_set.append(self.chunks[i])
                    training_set.concatenate(training_set, self.chunks[i].samples)

        print(training_set.shape)

        new_ds = Dataset(training_set)

        print(new_ds.shape)

        return new_ds

    def get_current_test_set(self, turn):

        #check to ensure the input turn is valid
        if turn > len(self.chunks):
            raise Exception("Turn is greater than the number of chunks.")

        #return the current chunk
        return self.chunks[turn]


    def get_current_results(self):
        return results


    def get_test_set_chunk_from_original(self, turn):
        return self.dataset[self.dataset.sa.fold_num == turn]

    def get_trainig_set_chunks_from_original(self, turn):
        #lets get that Dataset that doesn't include the current turn chunk
        new_ds = self.dataset[self.dataset.sa.fold_num != turn]

        #now let's check the neighbours
        if self.skip_nearest_neighbours:
            if turn > 1:
                new_ds = new_ds[new_ds.sa.fold_num != turn-1]

            if i < len(self.chunks)-1:
                new_ds = new_ds[new_ds.sa.fold_num != turn+1]
        return new_ds

def split_list(alist, wanted_parts=1):
    length = len(alist)
    ## // notates integer division
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def generate_chunk_transform_for_ds(ds, wanted_parts=1):
    association_transfrom = []
    
    for i in range(0, len(ds)):
        association_transfrom.append(i)

    #split this generated association_transfrom
    result_transform = split_list(association_transfrom, wanted_parts)

    result = []

    for i in range(0, len(result_transform)):        
        for value in result_transform[i]:
            result.append(i)

    return result

def split_ds(ds, wanted_parts=1):
    ds.sa['fold_num'] = split_ds(ds, wanted_parts)

    ds_array = []

    for i in range(0, wanted_parts):
        ds_array.append(ds[ds.sa.fold_num == i])

    return ds_array