from base_task_view import BaseTaskView

from models.file_input_model import FileInputModel
from models.base_processing_model import BaseProcessingModel
from models.base_processing_request_model import BaseProcessingRequestModel
from util import file_handler

class BaseMachineLearningView(BaseTaskView):

    title = "Machine Learning View"

    def create_widgets(self):

        self.input_models = []

        self.input_models.append(
            FileInputModel("BOLD", "The BOLD data for the story", [('NIFTI files', '*.nii;*nii.gz'), ('HDR files', '*.hdr'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Mask", "The mask to remove useless brain data", [('NIFTI files', '*.nii;*nii.gz'), ('HDR files', '*.hdr'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Story", "The story data points", [('MATLAB files', '*.mat'), ('All files', '*')], file_handler.open_matlab))
        self.input_models.append(
            FileInputModel("Trjactory", "The story data points", [('PICKLE files', '*.pkl'), ('All files', '*')], file_handler.open_pickle))

        super(BaseMachineLearningView, self).create_widgets()

    def update_ui_from_processing(self, *args):

        self.status_text.set(self.processing_model.progress.get() + " [" + self.processing_model.state.get() + "]")

        self.update_ui()

        if self.processing_model.state.get() == self.processing_model.FINISHED:
            self.is_processing_active = False

            self.display_results()

            #enable the button to stop multiple
            self.check_processing_possible()