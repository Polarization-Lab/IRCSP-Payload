
import os, datetime,time
#==========================================================
def find_file():
    '''
    Main function currently executes a print statement which shows files in the current working directory.
    Utilized for cross-reference to ensure HDF5 file exist in the same directory as python program.
    The function checks if the file name already exist and will increment the file naming count variable
    until the next available file name is found. Once the next available name is found, the program will
    continue to execute the image capture function and create a new HDF5 file with the next most available
    file name.
    '''

    #Check Current Working Directory (cwd)
    cwd = os.getcwd()
    directory = os.listdir(cwd)

    #Check Destination Directory (path)
    path = '/mnt/sdcard/image_data/'
    directory = os.listdir(path)

    
    print()
    print("Directory Path %r : \n" % (path))
    print("List of File Names: %s \n" % (directory))
    
     
    #File Name - Control Variable
    for i in range(100000000):
    
    #Set to work on .hdf5 file type extension.
        name = "Capture" + str(i) + ".hdf5"
    
    #Increments File Name, If File Already Exist!
        if name in directory:
            pass
        else:
            #Creates New File with next available value!
            #while name not in directory:
            print(i)
            return i


find_file();
