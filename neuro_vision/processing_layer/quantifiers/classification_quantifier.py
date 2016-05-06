from .base_quantifier import BaseQuantifier

import numpy as np

class ClassificationQuantifier(BaseQuantifier):

    def compute_accuracy(self, target_trajectory, result_trajectory):
        return abs(np.mean(result_trajectory == target_trajectory)) * 100