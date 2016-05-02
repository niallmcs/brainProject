import numpy as np
from mvpa2.suite import *

class BaseProcessor:

    results = []

    def __init__(self, dataset, trajectory, analyser):
        #store all relevant information
        self.dataset = dataset
        self.trajectory = trajectory
        self.analyser = analyser

    def process(self):
        pass

    def get_current_results(self):
        return results