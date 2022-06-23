

import os, datetime, time, h5py
from flirpy.camera.boson import Boson


def take_image(filename):
    """take_image: The function will create a Operating System timestamp variable (OS_time), configure
                the 2 IRCSP cameras and context camera to take three images (image1, image2, image3) and store the FPA temperatures
                (temp1,temp2,temp3) into an HDF5 File format with a unique naming convention.
    Parameters:
                filename - the filename of the HDF5 file.
    Returns: HDF5 file with 3 FLIR Boson Images, 3 FPA Temperatures & OS_time string.
    """

    # Time/Speed Test - Start
    start = datetime.datetime.now()

    #Create Timestamp for File Creation Tracking
    try:
        now = datetime.datetime.now()
        OS_time = now.strftime("%H:%M:%S")

        camera1 = Boson(port='/dev/ttyACM0') #find which one is transmission and which one is reflection
        camera2 = Boson(port='/dev/ttyACM1')
        camera3 = Boson(port= '/dev/ttyACM2')

        #set FFC to manual
        camera1.set_ffc_manual()
        camera2.set_ffc_manual()
        camera3.set_ffc_auto() #why auto not manual, check auto function of flirpy

        #get FPA temperature
        temp1 = camera1.get_fpa_temperature()
        temp2 = camera2.get_fpa_temperature()
        temp3 = camera3.get_fpa_temperature()
        print(temp1)
        print(temp2)
        print(temp3)

        #Take Image
        image1 = camera1.grab(device_id = 0)
        image2 = camera2.grab(device_id = 1)
        image3 = camera3.grab(device_id = 2) #check this


    except:
        print('error in image aquisition')
        #Close Camera
        camera1.close()
        camera2.close()
        camera3.close()
        time.sleep(5)
    
    finally:
        # Open as Read-Write ("a" - creates file if doesn't exist)
        with h5py.File(filename, "a") as h5:
            h5.attrs["OS_time"] = OS_time
            h5["image1"] = image1
            h5["image2"] = image2
            h5["image3"] = image3
            h5["temp1"] = temp1
            h5["temp2"] = temp2
            h5["temp3"] = temp3

        #Close Camera
        camera1.close()
        camera2.close()
        camera3.close()


        #Time/Speed Test - Finish
        finish = datetime.datetime.now()
        print("Image Capture File: ", filename," created in " , finish - start)

        #Adjust Sleep for File Creation Rate - (File/Seconds)
        time.sleep(10)

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
    path = '/mnt/sdcard/image_data/'
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
