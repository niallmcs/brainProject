def open_pickle(pickle_location):
    with open(file, 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        trajectory = u.load()

    return trajectory

def open_nifti(file_loc):
    pass

def open_matlab(mat_location):
    s3 = scipy.io.loadmat(file, squeeze_me=True)
    story_data = s3['words']

    return story_data