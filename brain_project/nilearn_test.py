import matplotlib.pyplot as plt
from nilearn import image
from nilearn import plotting

def __main__():
    volume = image.index_img("E:\\Users\\Niall\\Documents\\Computer Science\\FinalYearProject\\data\\ds105_raw\\ds105\\sub001\\BOLD\\task001_run001\\bold.nii.gz", 0)
    smoothed_img = image.smooth_img(volume, fwhm=5)

    # print("Read the images");

    plotting.plot_glass_brain(volume, title='plot_glass_brain',
    black_bg=True, display_mode='xz')

    plt.show()

    # print("Finished");

__main__()