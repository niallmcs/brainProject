def processCorrelation(trajectory_location, story_data_location, anatomy, bold_location, mask_location):
    print("Called")

    original_dataset = fmri_dataset(bold_location, mask=mask_location)

    #get the trajectory
    with open(trajectory_location, 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        original_trajectory = u.load()

    #downsample the trajectory to fit match the number of fMRI sample
    resampled_trajectory = resample(original_trajectory, len(original_dataset.samples))

    #convert both datasets to a 1D array
    array1 = original_dataset[:, 0].samples.ravel()
    array2 = resampled_trajectory.ravel()

    correlation_results = []

    range_max = original_dataset.nfeatures

    #convert the story trajectory to a list
    trajectory_list = resampled_trajectory.ravel()

    for num in range(0, range_max):
        sample_list = original_dataset[:, num].samples.ravel()
        correlation_result = numpy.corrcoef(trajectory_list, sample_list)[1,0]
        correlation_results.append(correlation_result)

    #replace NaN with 0s
    correlation_results = np.nan_to_num(correlation_results)

    #use numpy to convert the array to a 2d array - enabling us to create a Dataset
    correlation_matrix = np.reshape(correlation_results,(-1,len(correlation_results)))