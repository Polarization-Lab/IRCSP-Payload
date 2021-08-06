'''
Program: image_capture.py
Author: Eduardo D Contreras
Date: 04/20/2021
Class: ENGR498 - Design of Payload for near-space deployment of IR Optics
Project Sponsors: Kira Hart & Meredith Kupinski
Mentor: Catherine Merrill
Team Members: Nayleth Ramirez, Jeremy Parkinson, Jaclyn John, Thor Niel, Wassim Khawam
Description: The program is designed to automate image capturing using the FLIR Boson
cameras in the IRCSP. The program will continuously perform image acquisition with FPA
temperatures and store them with the Operating System Timestamp at time of creation in
order to create a tracking system for each file created during the flight mission.
'''

import os, datetime, time, h5py

def take_image(filename):
    """take_image: The function will create a Operating System timestamp variable (OS_time), configure
                the 2 IRCSP cameras to take an image (image1 & image2) and store the FPA temperatures
                (temp1 & temp2) into an HDF5 File format with a unique naming convention.
    Parameters:
                filename - the filename of the HDF5 file.
    Returns: HDF5 file with 2 FLIR Boson Images, 2 FPA Temperatures & OS_time string.
    """

    # Time/Speed Test - Start
    start = datetime.datetime.now()

    #Create Timestamp for File Creation Tracking
    try:
        now = datetime.datetime.now()
        OS_time = now.strftime("%H:%M:%S")

        #get FPA temperature
        temp1 = 35
        temp2 = 35
        print(temp1)
        print(temp2)

       

    except:
        print('error in image aquisition')
        
    finally:
        # Open as Read-Write ("a" - creates file if doesn't exist)
        with h5py.File(filename, "a") as h5:
            h5.attrs["OS_time"] = OS_time
            h5["temp1"] = temp1
            h5["temp2"] = temp2


        

        #Time/Speed Test - Finish
        finish = datetime.datetime.now()
        print("Image Capture File: ", filename," created in " , finish - start)

        #Adjust Sleep for File Creation Rate - (File/Seconds)
        time.sleep(1)

#==========================================================
def main():
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
    path ='/Users/kirahart/Dropbox/GitHub/IRSCP-Payload/IRCSP-Payload/data/'
    directory = os.listdir(path)
    
    print()
    print("Directory Path %r : \n" % (path))
    print("List of File Names: %s \n" % (directory))
    
    
    #File Name - Control Variable
    count = 0
    #Set to work on .hdf5 file type extension.
    name = "Capture" + str(count) + ".hdf5"
    
    #Increments File Name, If File Already Exist!
    while name in directory:
        count+=1
        name = "Capture" + str(count) + ".hdf5"
    else:
        #Creates New File with next available value!
        while name not in directory:
            name = "Capture" + str(count) + ".hdf5"
            filename = os.path.join(path,name)
            take_image(filename)
            count += 1


if __name__ == '__main__':
    main()
