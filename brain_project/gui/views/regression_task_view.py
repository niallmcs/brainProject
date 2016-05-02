from views.base_machine_learning_view import BaseMachineLearningView

from models.file_input_model import FileInputModel
from models.base_processing_model import BaseProcessingModel
from models.base_processing_request_model import BaseProcessingRequestModel
from util import file_handler
from processors.regression_task_processor import RegressionTaskProcessor

class RegressionTaskView(BaseMachineLearningView):

    title = "Regression"

    def start_processing(self):

        super(RegressionTaskView, self).start_processing()

        RegressionTaskProcessor(self.queue, self.processing_model).start()