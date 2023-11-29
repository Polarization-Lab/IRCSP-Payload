

import os, datetime, time
import h5py
import sys
from flirpy.camera.boson import Boson
import numpy as np

def main():


    start = datetime.datetime.now()

    #Create Timestamp for File Creation Tracking
    try:
       now = datetime.datetime.now()
       OS_time = now.strftime("%m.%d.%H.%M.%S")
       
    
       camera1 = Boson(port='/dev/ttyACM0') #transmission or reflection
       camera3 = Boson(port='/dev/ttyACM2')
       camera2 = Boson(port='/dev/ttyACM3')

        #set FFC to manual
       camera1.set_ffc_auto()
       camera2.set_ffc_auto()
       camera3.set_ffc_auto() 

        #get FPA temperature
       temp1 = camera1.get_fpa_temperature()
       temp2 = camera2.get_fpa_temperature()
       temp3 = camera3.get_fpa_temperature()
       
       
       print(temp1)
       print(temp2)
       print(temp3)

        #Take Image
       

       im3 = camera3.grab(device_id = 0)
              
       im1 = np.zeros((1,256,320))
       im2 = np.zeros((1,256,320))
    
       #im1 = camera1.grab(device_id = 0)
       #im2 = camera2.grab(device_id = 0)
       
       for i in range(1):
           im1[i] = camera1.grab(device_id = 1)
        
       for j in range(1):
           im2[j] = camera2.grab(device_id = 2)

    except:
        print('error in image aquisition')
        #Close Camera
        camera1.close()
        camera2.close()
        camera3.close()
        
    
    try:
        path = '/mnt/sdcard/image_data/'
        filename = "dummyimage" + str(OS_time) + ".hdf5"
         
        with h5py.File(path + filename,"a") as h5:
            h5["image1"] = im1
            h5["image2"] = im2
            h5["image3"] = im3
            h5["temp1"] = temp1
            h5["temp2"] = temp2
            h5["temp3"] = temp3
            h5.close()

          
        temps = [temp1,temp2,temp3] #add temp3
        filenames = ["FPAtemp1","FPAtemp2","FPAtemp3"]
        
        for NN in range(len(temps)):
            f = open('/mnt/sdcard/image_data/'+ filenames[NN] +".txt","w+")
            f.write(str(temps[NN]))
            f.close()
        
        print('image data saved')

        camera1.close()
        camera2.close()
        camera3.close()
        time.sleep(25)
    except:
        print('error in saving image data')
        camera1.close()
        camera2.close()
        camera3.close()
        exit()
#============================

#def main():

#    cwd = os.getcwd()
#    directory = os.listdir(cwd)
#    path = '/mnt/sdcard/image_data/'
#    directory = os.listdir(path)

#    count = 0
#    name = "Capture" + str(count) + ".hdf5"
     
   # while name in directory:
     #   count +=1
    # name = "Capture" + str(count) + ".hdf5"

   # else:
    #    while name not in directory:
   #         name = "Capture" + str(count) + ".hdf5"
  #          filename = os.path.join(path,name)
 #           take_image(filename)
 #           count +=1


if __name__ == '__main__':
    main()
