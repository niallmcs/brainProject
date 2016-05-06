from presentation_layer.views.base_task_view import BaseTaskView
from presentation_layer.models.file_input_model import FileInputModel
from presentation_layer.models.base_processing_model import BaseProcessingModel
from presentation_layer.models.base_processing_request_model import BaseProcessingRequestModel
from presentation_layer.util import file_handler
from presentation_layer.views.graph_plot_view import GraphPlotView

from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas, StringVar

class BaseMachineLearningView(BaseTaskView):

    title = "Machine Learning View"

    def create_widgets(self):

        self.input_models = []

        self.input_models.append(
            FileInputModel("BOLD/fMRI File", "The BOLD data for the story", [('NIFTI files', '*.nii;*nii.gz'), ('HDR files', '*.hdr'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Mask", "The mask to remove useless brain data", [('HDR files', '*.hdr'), ('NIFTI files', '*.nii;*nii.gz'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Experiment Metadata", "The story data points", [('MATLAB files', '*.mat'), ('All files', '*')], file_handler.open_matlab))
        self.input_models.append(
            FileInputModel("Target Trjactory", "The story data points", [('PICKLE files', '*.pkl'), ('All files', '*')], file_handler.open_pickle))

        super(BaseMachineLearningView, self).create_widgets()

        self.result_view = GraphPlotView(self)
        self.result_view.grid(row = 0, column = 1, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

    def update_ui_from_processing(self, *args):

        self.status_text.set(self.processing_model.progress.get() + " [" + self.processing_model.state.get() + "]")

        self.update_ui()

        if self.processing_model.state.get() == self.processing_model.FINISHED:
            self.is_processing_active = False

            accuracy = "%.2f" % self.processing_model.accuracy

            self.status_text.set(self.processing_model.progress.get() + " [Accuracy: " + accuracy + "%]")

            self.display_results()

            #enable the button to stop multiple
            self.check_processing_possible()

    def display_results(self):

        self.result_view.plot_results(self.processing_model.original, self.processing_model.result)