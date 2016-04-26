import threading
import queue
import time

class TaskProcessor(threading.Thread):

    NOT_STARTED = "Not Started"
    SETUP = "Setting up"
    FINISHED = "Finished"
    PROCESSING = "Processing"

    def __init__(self, queue, processing_model):
        threading.Thread.__init__(self)
        self.queue = queue
        self.processing_model = processing_model

    def run(self):

        self.processing_model.state.set(self.PROCESSING)
        self.processing_model.progress.set("1%")

        time.sleep(1)  # Simulate long running process
        self.queue.put("Task finished")
        print("finished 1")

        self.processing_model.state.set(self.FINISHED)
        self.processing_model.progress.set("100%")