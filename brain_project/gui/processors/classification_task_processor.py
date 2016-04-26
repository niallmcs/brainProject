from .task_processor import TaskProcessor

class ClassificationTaskProcessor(TaskProcessor):

    def run(self):

        request = self.processing_model.processing_request_model

        print("Bold " + request.bold_location)

        print("finished")