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
from sklearn.tree import DecisionTreeRegressor


class RegressionTaskProcessor(BaseMachineLearningTaskProcessor):

    def compute_result(self):
        fold_wise_processor = FoldWiseProcessor(self.ds, self.resampled_trajectory, SKLLearnerAdapter(DecisionTreeRegressor()), self.num_folds, True)
        fold_wise_processor.process()
        self.processing_model.result = fold_wise_processor.results