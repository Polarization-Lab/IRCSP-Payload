import h5py
import os 
import sys
import pandas as pd
import numpy as np


    

def print_groups(fn):
    #print current datasets
    print('file ' + fn + ' \n')
    with h5py.File(fn,'r') as hf:
        dataset_names = list(hf.keys())
        
        
        ds = []
        allsizes = []
        names = []

        for d in dataset_names:
            size = 0
            dataset_count = 0

            if isinstance(hf[d], h5py.Dataset):
                    size += hf[d].size
                    dataset_count += 1
            
            allsizes.append(size)
            ds.append(dataset_count)
            
    info = pd.DataFrame({'group name': dataset_names,'size (bytes)': allsizes,'datasets': ds})
            
    print(info)
    print('\n')
    print("%i MB in %i datasets out of %i items in hdf5 file." % (sum(allsizes)*1e-6, sum(ds), len(dataset_names)))
  


        
# EXAMPLE USE

fn = '/Volumes/KESU/image_data/Capture300.hdf5'
print_groups(fn)

with h5py.File(fn,'r') as hf:
        image1 =np.mean( hf.open('image1'))