from .base_task_processor import BaseTaskProcessor

import os
import numpy as np
import mvpa2
import nibabel
import pickle
import gzip
from mvpa2.suite import *
from nilearn.image import resample_img
from nilearn import image
from scipy.signal import resample

class CorrelationTaskProcessor(BaseTaskProcessor):

    def compute_result(self):
        #work out the results of the correlation of each pixel/feature over time
        correlation_results = []

        ##work out the number of features
        range_max = self.ds.nfeatures

        #convert the story trajectory to a list
        trajectory_list = self.resampled_trajectory.ravel()

        for num in range(0, range_max):

            if num % 10 == 0:
                print("num " + str(num))

            sample_list = self.ds[:, num].samples.ravel()
            correlation_result = np.corrcoef(trajectory_list, sample_list)[1,0]
            correlation_results.append(correlation_result)

        #replace NaN with 0s
        correlation_results = np.nan_to_num(correlation_results)

        #check to ensure we have no NaN results
        np.isnan(np.sum(correlation_results))

        #use numpy to convert the array to a 2d array - enabling us to create a Dataset
        correlation_matrix = np.reshape(correlation_results,(-1,len(correlation_results)))

        #create a dataset from the correlation matrix
        correlation_dataset = Dataset(correlation_matrix)

        #map the correlation dataset back to the original dataset
        overlay_data = map2nifti(self.ds, correlation_dataset)

        self.processing_model.result = overlay_data