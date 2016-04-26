from base_machine_learning_view import BaseMachineLearningView

from models.file_input_model import FileInputModel
from models.base_processing_model import BaseProcessingModel
from models.base_processing_request_model import BaseProcessingRequestModel
from util import file_handler
from processors.classification_task_processor import ClassificationTaskProcessor

class ClassificationTaskView(BaseMachineLearningView):

    title = "Classification"

    def start_processing(self):

        super(ClassificationTaskView, self).start_processing()

        ClassificationTaskProcessor(self.queue, self.processing_model).start()