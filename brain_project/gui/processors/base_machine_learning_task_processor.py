from .task_processor import TaskProcessor
import machine_learning.foldwiseprocessor
from machine_learning import targetdatautility
from machine_learning.foldwiseprocessor import FoldWiseProcessor
from machine_learning.fmrisamplecleaningtransform import get_affected_samples
from machine_learning.fmricleaner import remove_samples

import os
import numpy as np
import mvpa2
import nibabel
import pickle
import gzip
from mvpa2.suite import *
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


class BaseMachineLearningTaskProcessor(TaskProcessor):

    num_folds = 3

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
        #old_ds = ds
        #ds = old_ds[:400]

        #compute the result
        self.compute_result()

        self.processing_model.progress.set("100%")
        self.processing_model.state.set(self.FINISHED)

        print("finished")

    def compute_result(self):
        pass