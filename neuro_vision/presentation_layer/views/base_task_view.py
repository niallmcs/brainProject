import tkinter as tk
import presentation_layer.views.base_view as bv

from presentation_layer.views.file_input_view import FileInputView
from presentation_layer.views.graph_plot_view import GraphPlotView

from presentation_layer.models.file_input_model import FileInputModel
from presentation_layer.models.base_processing_model import BaseProcessingModel
from presentation_layer.models.base_processing_request_model import BaseProcessingRequestModel

from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas, StringVar

import queue
from presentation_layer.processors.base_task_processor import BaseTaskProcessor

class BaseTaskView(bv.BaseView):

    TITLE_FONT = ("Helvetica", 20, "bold")
    BUTTON_FONT = ("Helvetica", 20)
    STATUS_FONT = ("Helvetica", 20)

    input_models = []
    is_processing_possible = False
    is_processing_active = False

    processing_model = None

    status_text = None

    title = "Task View"


    def create_widgets(self):

        self.status_text = StringVar()
        self.status_text.set("Not Started")

        self.grid()

        for r in range(6):
            self.rowconfigure(r, weight=1)    
        for c in range(2):
            self.columnconfigure(c, weight=1)
            #Button(self, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        frame1 = Frame(self) #, bg="red"
        frame1.grid(row = 0, column = 0, rowspan = 6, columnspan = 1, sticky = W+E+N+S)


        title_label = ttk.Label(frame1, text=self.title, font=self.TITLE_FONT)
        title_label.pack(fill=BOTH, padx=25, pady=20)

        for input_model in self.input_models:
            input_view = FileInputView(frame1, input_model)
            input_view.pack(fill=BOTH)
            input_model.location_text.trace("w", self.check_processing_possible)

        process_button_style = ttk.Style()
        process_button_style.configure("Bold.TButton", font = ('Sans','20'))

        self.process_button = ttk.Button(frame1, text="PROCESS", width=20, style="Bold.TButton", state='disabled', command=self.start_processing)
        self.process_button.pack(side=BOTTOM, padx=5, pady=50)
        
        status_view = Frame(self, bg="white")
        status_view.grid(row = 3, column = 1, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

        status_label = Label(status_view, text="Status: ", font=self.TITLE_FONT, bg="white")
        status_label.pack(side=LEFT, padx=5, pady=5)

        current_status_label = Label(status_view, textvariable=self.status_text, bg="white", font=self.STATUS_FONT)
        current_status_label.pack(side=LEFT, padx=5, pady=5)

    def setup_window_details(self):
        self.controller.title("Abstract Machine Learning View")
        self.controller.geometry("1000x700")
        self.center()

    def check_processing_possible(self, *args):
        for input_model in self.input_models:
            #if we find a location not used, then we can't continue
            if input_model.location is None:
                self.is_processing_possible = False
                break
            else:
                self.is_processing_possible = True

        #enable only if testing
        #self.is_processing_possible = True

        #check to see if already processing
        if self.is_processing_active:
            self.is_processing_possible = False

        if self.is_processing_possible:
            self.process_button.config(state='normal')
        else:
            self.process_button.config(state='disabled')

    def start_processing(self):
        #turn active flag to True
        self.is_processing_active = True

        #disable the button to stop multiple
        self.check_processing_possible()

        #get the locaiton of the files
        bold_loc = mask_loc = story_loc = trajectory_loc = anatomy_loc = ""

        for input_model in self.input_models:
            if input_model.title == "BOLD/fMRI File":
                bold_loc = input_model.location
            elif input_model.title == "Mask":
                mask_loc = input_model.location
            elif input_model.title == "Experiment Metadata":
                story_loc = input_model.location
            elif input_model.title == "Target Trjactory":
                trajectory_loc = input_model.location
            elif input_model.title == "Anatomy":
                anatomy_loc = input_model.location


        processing_model = BaseProcessingRequestModel(bold_loc, mask_loc, anatomy_loc, story_loc, trajectory_loc)

        self.processing_model = BaseProcessingModel(processing_model)

        #set up tracking for the state and progress
        self.processing_model.progress.trace("w", self.update_ui_from_processing)
        self.processing_model.state.trace("w", self.update_ui_from_processing)

        self.queue = queue.Queue()
        #BaseTaskProcessor(self.queue, self.processing_model).startit()
        #self.master.after(100, self.process_queue)

    def update_ui_from_processing(self, *args):

        self.status_text.set(self.processing_model.progress.get() + " [" + self.processing_model.state.get() + "]")

        self.update_ui()

        if self.processing_model.state.get() == self.processing_model.FINISHED:
            self.is_processing_active = False

            self.display_results()

            #enable the button to stop multiple
            self.check_processing_possible()

    def display_results(self):

        self.result_view.plot_results(self.processing_model.result, self.processing_model.result)

    def update_ui(self):
        pass