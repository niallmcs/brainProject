import tkinter as tk
import base_view as bv
from views.file_input_view import FileInputView
from views.graph_plot_view import GraphPlotView
from models.file_input_model import FileInputModel

from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas

class BaseMachineLearningView(bv.BaseView):

    TITLE_FONT = ("Helvetica", 20, "bold")
    BUTTON_FONT = ("Helvetica", 20)
    STATUS_FONT = ("Helvetica", 20)

    def create_widgets(self):
        # label = tk.Label(self, text="Machine Learning View", font=self.TITLE_FONT)
        # label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: self.controller.show_frame("SetupScreen"))
        # button.pack()

        self.grid()

        for r in range(6):
            self.rowconfigure(r, weight=1)    
        for c in range(2):
            self.columnconfigure(c, weight=1)
            #Button(self, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        frame1 = Frame(self) #, bg="red"
        frame1.grid(row = 0, column = 0, rowspan = 6, columnspan = 1, sticky = W+E+N+S)


        title_label = ttk.Label(frame1, text="Regression", font=self.TITLE_FONT)
        title_label.pack(fill=BOTH, padx=25, pady=20)

        bold_file_input_model = FileInputModel("BOLD", "The BOLD data for the story", ["nifti"])
        bold_file_input_view = FileInputView(frame1, bold_file_input_model)
        bold_file_input_view.pack(fill=BOTH)

        story_file_input_model = FileInputModel("Story", "The story data points", ["nifti"])
        story_file_input_view = FileInputView(frame1, story_file_input_model)
        story_file_input_view.pack(fill=BOTH)

        trajectory_file_input_model = FileInputModel("Trjactory", "The story data points", ["nifti"])
        trajectory_file_input_view = FileInputView(frame1, trajectory_file_input_model)
        trajectory_file_input_view.pack(fill=BOTH)

        anatomy_file_input_model = FileInputModel("Anatomy", "The story data points", ["nifti"])
        anatomy_file_input_view = FileInputView(frame1, anatomy_file_input_model)
        anatomy_file_input_view.pack(fill=BOTH)


        process_button_style = ttk.Style()
        process_button_style.configure("Bold.TButton", font = ('Sans','20'))

        process_button = ttk.Button(frame1, text="PROCESS", width=20, style="Bold.TButton")
        process_button.pack(side=BOTTOM, padx=5, pady=50)


        # file_load_frame = Frame(frame1, bg="gold")
        # file_load_frame.pack(fill=BOTH)

        # title_button_frame = Frame(file_load_frame, bg="purple")
        # title_button_frame.pack(fill=BOTH)

        # bold_label = ttk.Label(title_button_frame, text="BOLD", font=self.TITLE_FONT)
        # bold_label.pack(side=LEFT, padx=5, pady=5)

        # load_button = ttk.Button(title_button_frame, text="LOAD")
        # load_button.pack(side=RIGHT, padx=5, pady=5)

        # filename_label = Label(file_load_frame, text="Path")
        # filename_label.pack(side=LEFT, padx=5, pady=5)

        # w = Canvas(file_load_frame, width=500, height=2)
        # w.pack()
        # w.create_line(0, 0, 500, 0, width=5)

        frame2 = GraphPlotView(self)
        frame2.grid(row = 0, column = 1, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

        frame3 = Frame(self, bg="white")
        frame3.grid(row = 3, column = 1, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

        status_label = Label(frame3, text="Status: ", font=self.TITLE_FONT, bg="white")
        status_label.pack(side=LEFT, padx=5, pady=5)

        current_status_label = Label(frame3, text="Processing", bg="white", font=self.STATUS_FONT)
        current_status_label.pack(side=LEFT, padx=5, pady=5)

    def setup_window_details(self):
        self.controller.title("Abstract Machine Learning View")
        self.controller.geometry("1000x600")
        self.center()