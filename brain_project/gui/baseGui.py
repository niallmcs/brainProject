from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from nilearn import plotting

import matplotlib.pyplot as plt
import numpy as np
import pickle
import gzip
import numpy
import scipy.io

import mvpa2
from mvpa2.suite import *
from nilearn.image import resample_img
from nilearn import image
import nibabel
from brainCorrelationPlotter import plot_lightbox
import CorrelationProcessor

class Example(Frame):

    processing_progress = "not started"
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        
        self.parent = parent
        self.initUI()

        # self.addButtons()
        # self.addMainContent()
        
    
    def initUI(self):
      
        self.parent.title("Brain GUI")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        # style
        self.style = Style()
        self.style.theme_use("default")

        # f = Frame(self, width = 500, height = 500)
        # f.pack(side=LEFT, expand = 1)

        # f3 = Frame(f, width = 500)
        # f3.pack(side=LEFT, expand = 1, pady = 50, padx = 50)

        # f2 = Frame(self, height=100, width = 100)
        # f2.pack(side=LEFT, fill = Y)

        # b = Button(f2, text = "test")
        # b.pack()

        # b = Button(f3, text = "1")
        # b.grid(row=1, column=3)
        # b2 = Button(f3, text = "2")
        # b2.grid(row=1, column=4)
        # b3 = Button(f3, text = "2")
        # b3.grid(row=2, column=0)

        # Style().configure("TButton", padding=(0, 5, 0, 5), 
        #     font='serif 10')

        # self.columnconfigure(0, pad=3)
        # self.columnconfigure(1, pad=3)
        # self.columnconfigure(2, pad=3)
        # self.columnconfigure(3, pad=3)
        
        # self.rowconfigure(0, pad=3)
        # self.rowconfigure(1, pad=3)
        # self.rowconfigure(2, pad=3)
        # self.rowconfigure(3, pad=3)
        # self.rowconfigure(4, pad=3)

        self.trajectory_location = None
        self.trajectory = None
        self.story_data_location = None
        self.story_data = None
        self.anatomy_location = None
        self.anatomy_data = None
        self.bold_location = None
        self.bold_data = None
        self.mask_location = None
        self.mask_location = os.path.join('..','..', 'data', 'qub', 'struct', 'final_mask_w.hdr')

        # self.trajectory_location = os.path.join('..', '..', 'data', 'story', 'smoothedTrajectoriesDifferentWindowSizes', 'smoothTrajRawValenceMean_win200.pkl')
        # self.story_data_location = os.path.join('..', '..', 'data', 'plosone', 'subject_3.mat')
        # self.anatomy_location = os.path.join('..', '..', 'data', 'qub', 'struct', 'cos005a1001.hdr')
        # self.bold_location = os.path.join('..','..', 'data', 'qub', '4Dw.nii')
        


        left_frame = Frame(self, width = 500, height = 500)
        left_frame.pack(side=LEFT, fill=BOTH, expand=3)

        right_frame = Frame(self, width = 500, height = 500)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=1)

        #add content to the story section
        story_title_label = Label(left_frame, text="Story")
        story_title_label.grid(row=0, column=0)

        trajectory_button = Button(left_frame, text="Open Trajectory",
            command=self.openTrajectory)
        trajectory_button.grid(row=1, column=0)

        self.trajectory_location_label = Label(left_frame, text="No Trajectory Data Loaded")
        self.trajectory_location_label.grid(row=2, column=0)

        story_data_button = Button(left_frame, text="Open Story Data",
            command=self.openStoryData)
        story_data_button.grid(row=3, column=0)

        self.story_data_location_label = Label(left_frame, text="No Story Data Loaded")
        self.story_data_location_label.grid(row=4, column=0)

        self.plot_trajectory_button = Button(left_frame, text="Plot Trajectory",
            command=self.plotTrajectoryExternal, state=DISABLED)
        self.plot_trajectory_button.grid(row=6, column=0)

        #add content to the brain section
        brain_title_label = Label(left_frame, text="Brain")
        brain_title_label.grid(row=0, column=1)

        anatomy_button = Button(left_frame, text="Open anatomy",
            command=self.openAnatomy)
        anatomy_button.grid(row=1, column=1)

        self.anatomy_location_label = Label(left_frame, text="No anatomy Data Loaded")
        self.anatomy_location_label.grid(row=2, column=1)

        bold_button = Button(left_frame, text="Open BOLD",
            command=self.openBold)
        bold_button.grid(row=3, column=1)

        self.bold_location_label = Label(left_frame, text="No BOLD Data Loaded")
        self.bold_location_label.grid(row=4, column=1)

        self.plot_anatomy_button = Button(left_frame, text="Plot anatomy",
            command=self.plotAnatomyExternal, state=DISABLED)
        self.plot_anatomy_button.grid(row=6, column=1)

        #add content to the processing section
        processing_title_label = Label(right_frame, text="Processing")
        processing_title_label.grid(row=0, column=0)

        self.start_processing_button = Button(right_frame, text="Start Processing",
            command=self.startProcessing, state=DISABLED)
        self.start_processing_button.grid(row=1, column=0)

        self.processing_progress_label = Label(right_frame, text="Prcoessing: " + self.processing_progress)
        self.processing_progress_label.grid(row=2, column=0)

        self.plot_processing_results = Button(right_frame, text="Plot Results",
            command=self.plotProcessingResultsExternal, state=DISABLED)
        self.plot_processing_results.grid(row=3, column=0)

        self.export_processing_results = Button(right_frame, text="Export Results",
            command=self.exportProcessingResults, state=DISABLED)
        self.export_processing_results.grid(row=4, column=0)

        self.plot_external_results = Button(right_frame, text="Plot External Results",
            command=self.plotExernalResults, state=DISABLED)
        self.plot_external_results.grid(row=5, column=0)


    def centerWindow(self):
      
        w = 571
        h = 175

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onOpen(self, types):
      
        ftypes = types
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            return fl

    def openTrajectory(self):
        file = self.onOpen([('PICKLE files', '*.pkl'), ('All files', '*')])

        self.trajectory_location = file

        with open(file, 'rb') as f:
            u = pickle._Unpickler(f)
            u.encoding = 'latin1'
            self.trajectory = u.load()

        self.trajectory_location_label['text'] = file[-20:]
        self.plot_trajectory_button['state'] = 'normal'

        self.checkIfProcessingIsPossible()

    def openStoryData(self):
        file = self.onOpen([('MATLAB files', '*.mat'), ('All files', '*')])

        self.story_data_location = file

        s3 = scipy.io.loadmat(file, squeeze_me=True)
        self.story_data = s3['words']

        self.story_data_location_label['text'] = file[-20:]

        self.checkIfProcessingIsPossible()

    def plotTrajectoryExternal(self):
        plt.plot(self.trajectory)
        plt.ylabel('Emotional Response')
        plt.show()

    def openAnatomy(self):
        file = self.onOpen([('NIFTI files', '*.nii;*nii.gz'), ('HDR files', '*.hdr'), ('All files', '*')])

        self.anatomy_location = file
        self.anatomy_data = None

        self.anatomy_location_label['text'] = file[-20:]
        self.plot_anatomy_button['state'] = 'normal'
        self.plot_external_results['state'] = 'normal'

        self.checkIfProcessingIsPossible()

    def openBold(self):
        file = self.onOpen([('NIFTI files', '*.nii;*nii.gz'), ('All files', '*')])

        self.bold_location = file

        #don't load the bold data yet
        self.bold_data = None

        self.bold_location_label['text'] = file[-20:]

        self.checkIfProcessingIsPossible()

    def plotAnatomyExternal(self):
        plotting.plot_anat(self.anatomy_location, title='Anatomy')
        plt.show()

    def startProcessing(self):

        if self.trajectory_location is None:
            print("no trajectory file supplied")
            return
        if self.story_data_location is None:
            print("no Story data file supplied")
            return
        if self.anatomy_location is None:
            print("no anatomy file supplied")
            return
        if self.bold_location is None:
            print("no BOLD file supplied")
            return

        correlation_matrix = self.computeCorrelation(
            self.trajectory_location,
            self.story_data_location,
            self.anatomy_location,
            self.bold_location,
            self.mask_location
            )

        #create a dataset from the correlation matrix
        self.correlation_dataset = Dataset(correlation_matrix)
        ds = fmri_dataset(self.bold_location, mask=self.mask_location)
        self.overlay_data = map2nifti(ds, self.correlation_dataset)


        self.plot_processing_results['state'] = 'normal'
        self.export_processing_results['state'] = 'normal'
        
    def plotProcessingResultsExternal(self):
        print("plotting results")

        self.plotCorrelationResults(self.anatomy_location, self.overlay_data, self.bold_location)

    def exportProcessingResults(self):
        print("exporting results")
        f = filedialog.asksaveasfilename(defaultextension=".nii")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        self.overlay_data.to_filename(f)

    def plotExernalResults(self):
        file = self.onOpen([('NIFTI files', '*.nii;*nii.gz'), ('All files', '*')])

        self.plotCorrelationResults(self.anatomy_location, file, file)
        

    def plotCorrelationResults(self, background, overlay, desired_resolution_file_location):
        image_to_resample = nibabel.load(background)
        image_to_use_for_sample = image.index_img(desired_resolution_file_location, 0)
        resampled_background = resample_img(image_to_resample,target_affine = image_to_use_for_sample.get_affine(), target_shape=image_to_use_for_sample.shape)

        mri_args = {
            'background' : resampled_background,
            'cmap_bg' : 'gray',
            'cmap_overlay' : 'PiYG', # YlOrRd_r # pl.cm.autumn
            'interactive' : cfg.getboolean('examples', 'interactive', True),
            }

        plot_lightbox(overlay=overlay, vlim=(-1.0, 1.0), do_stretch_colors=True, **mri_args)

    def checkIfProcessingIsPossible(self):

        #easiest to check string
        if self.trajectory_location is None:
            return
        if self.story_data_location is None:
            return
        if self.anatomy_location is None:
            return
        if self.bold_location is None:
            return

        #if it passed all the above, then we have the data
        self.start_processing_button['state'] = 'normal'


    def computeCorrelation(self, trajectory_location, story_data_location, anatomy, bold_location, mask_location):

        original_dataset = fmri_dataset(bold_location, mask=mask_location)

        #get the trajectory
        with open(trajectory_location, 'rb') as f:
            u = pickle._Unpickler(f)
            u.encoding = 'latin1'
            original_trajectory = u.load()

        #downsample the trajectory to fit match the number of fMRI sample
        resampled_trajectory = resample(original_trajectory, len(original_dataset.samples))

        #convert both datasets to a 1D array
        array1 = original_dataset[:, 0].samples.ravel()
        array2 = resampled_trajectory.ravel()

        correlation_results = []

        range_max = original_dataset.nfeatures

        #convert the story trajectory to a list
        trajectory_list = resampled_trajectory.ravel()

        for num in range(0, range_max):
            # self.processing_progress = "{}/{}".format(num, range_max)

            # if(num > 1000):
            #     correlation_results.append(0)
            #     continue

            sample_list = original_dataset[:, num].samples.ravel()
            correlation_result = numpy.corrcoef(trajectory_list, sample_list)[1,0]
            correlation_results.append(correlation_result)

        #replace NaN with 0s
        correlation_results = np.nan_to_num(correlation_results)

        #use numpy to convert the array to a 2d array - enabling us to create a Dataset
        correlation_matrix = np.reshape(correlation_results,(-1,len(correlation_results)))

        return correlation_matrix

def main():
  
    root = Tk()
    # root.geometry("500x400+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()