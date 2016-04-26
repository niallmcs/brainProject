class BaseProcessingRequestModel():

    def __init__(self, bold_location, mask_location, anatomy_location, story_location, trajectory_location):
        self.bold_location = bold_location
        self.mask_location = mask_location
        self.anatomy_location = anatomy_location
        self.story_location = story_location
        self.trajectory_location = trajectory_location

    def printValues(self):
        print("")
        print("mask Location " + self.mask_location)
