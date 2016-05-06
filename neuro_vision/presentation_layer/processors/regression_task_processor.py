from .base_task_processor import BaseTaskProcessor
from .base_machine_learning_task_processor import BaseMachineLearningTaskProcessor

import processing_layer.fold_wise_processor
from processing_layer.util import target_data_utility
from processing_layer.fold_wise_processor import FoldWiseProcessor
from processing_layer.util.fmri_sample_cleaning_transform import get_affected_samples
from processing_layer.util.fmri_cleaner import remove_samples
from processing_layer.quantifiers.regression_quantifier import RegressionQuantifier

import os
import numpy as np
import mvpa2
import nibabel
import pickle
import gzip
from mvpa2.suite import *
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


class RegressionTaskProcessor(BaseMachineLearningTaskProcessor):

    def compute_result(self):
        fold_wise_processor = FoldWiseProcessor(self.ds, self.resampled_trajectory, SKLLearnerAdapter(DecisionTreeRegressor()), self.num_folds, True)
        fold_wise_processor.process()
        self.processing_model.result = fold_wise_processor.results
        self.processing_model.accuracy = RegressionQuantifier().compute_accuracy(self.processing_model.original, self.processing_model.result)