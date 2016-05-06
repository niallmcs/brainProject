from .base_quantifier import BaseQuantifier

import numpy as np

class RegressionQuantifier(BaseQuantifier):

    def compute_accuracy(self, target_trajectory, result_trajectory):
        return abs(np.corrcoef(result_trajectory, target_trajectory)[0, 1]) * 100