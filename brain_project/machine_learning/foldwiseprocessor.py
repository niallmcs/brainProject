class FoldWiseProcessor:

    def __init(self, dataset, trajectory, analyser, number_of_folds, skip_nearest_neighbours=false):
        #store all relevant information
        self.dataset = dataset
        self.trajectory = trajectory
        self.analyser = analyser
        self.number_of_folds = number_of_folds

        #create folds
        self.chunks = split_list(self.dataset, number_of_folds)


    def process(self):
        print("starting to process")


    def get_current_training_set(self, turn):

        training_set = []

        #loop over all the chunks
        for i in range(0, len(self.chunks)):

            #if skipping the nearest neighbour is enabled, we must validate
            if skip_nearest_neighbours:
                if i > 0:
                    if i == turn-1:
                        break;

                if i < len(self.chunks):
                    if i == turn+1
                        break;

            if(i != turn):
                training_set.append(self.chunks[i])

        return training_set

    def get_current_test_set(self, turn):

        #check to ensure the input turn is valid
        if turn > len(self.chunks):
            raise Exception("Turn is greater than the number of chunks.")

        #return the current chunk
        return self.chunks[i]

def split_list(alist, wanted_parts=1):
    length = len(alist)
    ## // notates integer division
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]