from .base_task_processor import BaseTaskProcessor
from .base_machine_learning_task_processor import BaseMachineLearningTaskProcessor

import processing_layer.fold_wise_processor
from processing_layer.fold_wise_processor import FoldWiseProcessor
from processing_layer.util import target_data_utility
from processing_layer.util.fmri_sample_cleaning_transform import get_affected_samples
from processing_layer.util.fmri_cleaner import remove_samples
from processing_layer.quantifiers.classification_quantifier import ClassificationQuantifier

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
        self.resampled_trajectory = target_data_utility.convert_targets_to_simple_values(self.resampled_trajectory)
        self.processing_model.original = self.resampled_trajectory
        self.ds.sa['targets'] = self.resampled_trajectory
        
        fold_wise_processor = FoldWiseProcessor(self.ds, self.resampled_trajectory, kNN(k=5, dfx=one_minus_correlation, voting='majority'), self.num_folds, True)
        fold_wise_processor.process()
        self.processing_model.result = fold_wise_processor.results

        self.processing_model.accuracy = ClassificationQuantifier().compute_accuracy(self.ds.targets, self.processing_model.result)