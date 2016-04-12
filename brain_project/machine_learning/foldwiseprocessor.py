class FoldWiseProcessor:

    results = []

    def __init__(self, dataset, trajectory, analyser, number_of_folds, skip_nearest_neighbours=false):
        #store all relevant information
        self.dataset = dataset
        self.trajectory = trajectory
        self.analyser = analyser
        self.number_of_folds = number_of_folds

        #create folds
        self.chunks = split_list(self.dataset, number_of_folds)


    def process(self):

        #every time this method is run, it will wipe the current state of #results
        print("starting to process")

        #set the turn
        turn = 0

        for i in range(0, number_of_folds):
            print("starting turn " + turn)

            #get the relevant data
            training_set = get_current_training_set(turn)
            test_set = get_current_test_set(turn)

            #train the analyser/model
            analyser.train(training_set)

            #get the prediction based on the chunks
            predictions = analyser.predict(test_set)

            #append the predictions to the global results
            results.append(predictions)

            #increment the turn
            turn = turn + 1

        print("Finished process")

        return process


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


    def get_current_results(self):
        return results

def split_list(alist, wanted_parts=1):
    length = len(alist)
    ## // notates integer division
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]