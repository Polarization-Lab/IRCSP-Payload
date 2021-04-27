'''
Author: Eduardo D Contreras
Date: 01/30/2021
Class: ENGR498 - Design of Payload for near-space deployment of IR Optics
Project Sponsors: Kira Hart & Meredith Kupinski

Mentor: Catherine Merrill

Team Members: Nayleth Ramirez, Jeremy Parkinson, Jaclyn John, Thor Niel, Wassim Khawam

Description: The purpose of this program is
'''

# put all of your import statements below this line and then delete this comment
import os
import h5py

# put all of your function definitions below this line and then delete this comment

def traverse_datasets(hdf5_file):

    """Traverse all datasets across all groups in HDF5 file."""

    def h5py_dataset_iterator(g, prefix=''):
        for key in g.keys():
            item = g[key]
            path = '{}/{}'.format(prefix, key)
            if isinstance(item, h5py.Dataset):  # test for dataset
                yield (path, item)
            elif isinstance(item, h5py.Group):  # test for group (go down)
                yield from h5py_dataset_iterator(item, path)

    with h5py.File(hdf5_file, 'r') as f:
        print("Filename: ", f)
        print("Timestamp: ", f.attrs["OS_time"])
        for (path, dset) in h5py_dataset_iterator(f):
            print(path, dset)

    return None



        #==========================================================
def main():
    '''
    Main function currently executes a print statement which shows files in the current working directory.
    Utilized for cross-referencing. Main function traverse all datasets across all groups in the given HDF5 file.
    Opens up the given HDF5 file and prints the datasets with File Size in the HDF5 file.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment

    #Check Current Working Directory (cwd)
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))
    print()
    for filename in files:
        if filename.endswith(".hdf5"):
    #Open the test file in Current Working Directory
            traverse_datasets(filename)
            print()
            print(os.stat(filename).st_size, "bytes \n") #344200 bytes = 0.3442 Megabyte


if __name__ == '__main__':
    main()

