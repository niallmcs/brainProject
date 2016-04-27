from .task_processor import TaskProcessor
from .base_machine_learning_task_processor import BaseMachineLearningTaskProcessor

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


class ClassificationTaskProcessor(BaseMachineLearningTaskProcessor):

    def compute_result(self):
        self.resampled_trajectory = targetdatautility.convert_targets_to_simple_values(self.resampled_trajectory)
        self.processing_model.original = self.resampled_trajectory
        self.ds.sa['targets'] = self.resampled_trajectory
        
        fold_wise_processor = FoldWiseProcessor(self.ds, self.resampled_trajectory, kNN(k=5, dfx=one_minus_correlation, voting='majority'), self.num_folds, True)
        fold_wise_processor.process()
        self.processing_model.result = fold_wise_processor.results

        self.processing_model.accuracy = abs(np.mean(self.processing_model.result == self.ds.targets)) * 100