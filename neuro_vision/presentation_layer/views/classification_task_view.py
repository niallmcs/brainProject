from presentation_layer.views.base_machine_learning_view import BaseMachineLearningView
from presentation_layer.models.file_input_model import FileInputModel
from presentation_layer.models.base_processing_model import BaseProcessingModel
from presentation_layer.models.base_processing_request_model import BaseProcessingRequestModel
from presentation_layer.util import file_handler
from presentation_layer.processors.classification_task_processor import ClassificationTaskProcessor

class ClassificationTaskView(BaseMachineLearningView):

    title = "Classification"

    def start_processing(self):

        super(ClassificationTaskView, self).start_processing()

        ClassificationTaskProcessor(self.queue, self.processing_model).start()