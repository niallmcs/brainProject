from .base_task_processor import BaseTaskProcessor

class BaseMachineLearningTaskProcessor(BaseTaskProcessor):

    num_folds = 15

    def compute_result(self):
        pass