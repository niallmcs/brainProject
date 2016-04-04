import threading

class myThread (threading.Thread):
    def __init__(self, trajectory_location, story_data_location, anatomy, bold_location, mask_location):
        threading.Thread.__init__(self)
        self.trajectory_location = trajectory_location
        self.story_data_location = story_data_location
        self.anatomy = anatomy
        self.bold_location = bold_location
        self.mask_location = mask_location

    def run(self):
        print("running")