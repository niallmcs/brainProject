import threading
import queue
import time

import processing_layer.fold_wise_processor
from processing_layer.util import target_data_utility
from processing_layer.fold_wise_processor import FoldWiseProcessor
from processing_layer.util.fmri_sample_cleaning_transform import get_affected_samples
from processing_layer.util.fmri_cleaner import remove_samples

import os
import numpy as np
import mvpa2
import nibabel
import pickle
import gzip
from mvpa2.suite import *
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

class BaseTaskProcessor(threading.Thread):

    NOT_STARTED = "Not Started"
    SETUP = "Setting up"
    FINISHED = "Finished"
    PROCESSING = "Processing"

    def __init__(self, queue, processing_model):
        threading.Thread.__init__(self)
        self.queue = queue
        self.processing_model = processing_model

    def run(self):

        self.processing_model.state.set(self.SETUP)
        self.processing_model.progress.set("1%")

        request = self.processing_model.processing_request_model

        ds_removal_transform = get_affected_samples(request.trajectory_location, request.story_location)

        self.ds = remove_samples(request.bold_location, request.mask_location, ds_removal_transform)


        with open(request.trajectory_location, 'rb') as f:
            u = pickle._Unpickler(f)
            u.encoding = 'latin1'
            original_trajectory = u.load()

        self.processing_model.progress.set("10%")
        self.processing_model.state.set(self.PROCESSING)

        self.resampled_trajectory = resample(original_trajectory, len(self.ds.samples))
        self.ds.sa['targets'] = self.resampled_trajectory
        self.processing_model.original = self.resampled_trajectory

        #make the ds smaller
        #old_ds = self.ds
        #self.ds = old_ds[:100]
        #self.resampled_trajectory = resample(original_trajectory, len(self.ds.samples))

        #compute the result
        self.compute_result()

        self.processing_model.progress.set("100%")
        self.processing_model.state.set(self.FINISHED)

    def compute_result(self):
        pass