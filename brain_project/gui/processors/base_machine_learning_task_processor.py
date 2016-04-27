from .task_processor import TaskProcessor

class BaseMachineLearningTaskProcessor(TaskProcessor):

    num_folds = 3

    def compute_result(self):
        pass