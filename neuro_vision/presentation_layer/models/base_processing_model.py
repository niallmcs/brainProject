from tkinter import StringVar

class BaseProcessingModel():

    NOT_STARTED = "Not Started"
    FINISHED = "Finished"
    PROCESSING = "Processing"
    result = None

    def __init__(self, processing_request_model):
        self.processing_request_model = processing_request_model

        self.progress = StringVar()
        self.progress.set("0%")

        self.state = StringVar()
        self.state.set(self.NOT_STARTED)