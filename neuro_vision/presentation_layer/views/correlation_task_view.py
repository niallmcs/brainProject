from presentation_layer.views.base_task_view import BaseTaskView
from presentation_layer.models.file_input_model import FileInputModel
from presentation_layer.models.base_processing_model import BaseProcessingModel
from presentation_layer.models.base_processing_request_model import BaseProcessingRequestModel
from presentation_layer.util import file_handler
from presentation_layer.processors.correlation_task_processor import CorrelationTaskProcessor
from presentation_layer.views.correlation_graph_view import CorrelationGraphView

import os
import numpy as np
import mvpa2
import nibabel
import pickle
import gzip
from mvpa2.suite import *
from nilearn.image import resample_img
from nilearn import image
from scipy.signal import resample
from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas, StringVar

class CorrelationTaskView(BaseTaskView):

    title = "Correlation"

    def create_widgets(self):

        self.input_models.append(
            FileInputModel("BOLD/fMRI File", "The BOLD data for the story", [('NIFTI files', '*.nii;*nii.gz'), ('HDR files', '*.hdr'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Mask", "The mask to remove useless brain data", [('HDR files', '*.hdr'), ('NIFTI files', '*.nii;*nii.gz'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Anatomy", "The story data points", [('HDR files', '*.hdr'), ('NIFTI files', '*.nii;*nii.gz'), ('All files', '*')], file_handler.open_nifti))
        self.input_models.append(
            FileInputModel("Experiment Metadata", "The story data points", [('MATLAB files', '*.mat'), ('All files', '*')], file_handler.open_matlab))
        self.input_models.append(
            FileInputModel("Target Trajectory", "The story data points", [('PICKLE files', '*.pkl'), ('All files', '*')], file_handler.open_pickle))


        super(CorrelationTaskView, self).create_widgets()

        self.result_view = CorrelationGraphView(self)
        self.result_view.grid(row = 0, column = 1, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

    def start_processing(self):
        super(CorrelationTaskView, self).start_processing()

        CorrelationTaskProcessor(self.queue, self.processing_model).start()

    def update_ui_from_processing(self, *args):

        self.status_text.set(self.processing_model.progress.get() + " [" + self.processing_model.state.get() + "]")

        self.update_ui()

        if self.processing_model.state.get() == self.processing_model.FINISHED:
            self.is_processing_active = False

            self.display_results()

            #enable the button to stop multiple
            self.check_processing_possible()

    def display_results(self):

        #load the high-res anatomy - this needs to be downsampled to fit the resolution of our data
        original_anatomy = nibabel.load(self.processing_model.processing_request_model.anatomy_location)

        #we will use the first volumne/sample from the bold data to 
        bold_data_sample = image.index_img(self.processing_model.processing_request_model.bold_location, 0)

        #resample the original anatomy to meet the bold data
        resampled_anatomy = resample_img(original_anatomy, target_affine = bold_data_sample.get_affine(), target_shape=bold_data_sample.shape)

        mri_args = {
            'background' : resampled_anatomy,
            'cmap_bg' : 'gray',
            'cmap_overlay' : 'PiYG', # YlOrRd_r # pl.cm.autumn
            'interactive' : cfg.getboolean('examples', 'interactive', True),
            }

        self.result_view.plot_results(self.processing_model.result, mri_args)