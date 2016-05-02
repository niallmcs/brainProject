import tkinter as tk

from views.start_page import StartPage
from views.base_machine_learning_view import BaseMachineLearningView
from views.about_page import AboutPage
from views.classification_task_view import ClassificationTaskView
from views.correlation_task_view import CorrelationTaskView
from views.regression_task_view import RegressionTaskView

TITLE_FONT = ("Helvetica", 18, "bold")

class NeuroVisionApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, BaseMachineLearningView, AboutPage, ClassificationTaskView, RegressionTaskView, CorrelationTaskView):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.setup_window_details()


if __name__ == "__main__":
    app = NeuroVisionApp()
    app.iconbitmap('NeuroVisionIcon.ico')
    app.mainloop()