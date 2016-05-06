#import os
import numpy as np
#import mvpa2
import nibabel
import pickle
import gzip
from mvpa2.suite import *


def remove_samples(bold_path, mask_path, removal_tansform):

    ds = fmri_dataset(bold_path, mask=mask_path)

    detrender = PolyDetrendMapper(polyord=1)
    ds = ds.get_mapped(detrender)

    if len(ds) != len(removal_tansform):
        raise Exception("Dataset and removal transform were not the same size.")

    ds.sa['important'] = removal_tansform

    ds_split = ds[ds.sa.important == '+']

    return ds_split