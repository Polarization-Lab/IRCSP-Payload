"""
Created on Wed May 11 15:46:32 2022

@author: jaclyn john
"""


from   flirpy.camera.boson import Boson 
import matplotlib.pyplot as plt
import h5py
import numpy as np
import time 
#from datetime import datetime

def get_timestamp():
    t = time.localtime()
    return time.strftime('%H_%M_%S', t)


def p3_image_capture():
    
    save_path = 'C:\\Users\\khart\\Documents\\Summer2022Campaign\\IRCSP1\\TestRuns\\StreamingDataTest\\'
    meas_num = 1
    frame_avg = 10

    """DO NOT CHANGE"""
    camera1 = Boson(port='COM15')
    camera2 = Boson(port='COM16')

    #set FFC to manual
    camera1.set_ffc_manual() 
    camera2.set_ffc_manual()


    for i in range(meas_num):
    
        img1 = np.zeros((256,320))
        img2 = np.zeros((256,320))
        im1 = np.zeros((frame_avg,256,320))
        im2 = np.zeros((frame_avg,256,320))
        
        t1 = camera1.get_fpa_temperature()
        t2 = camera2.get_fpa_temperature()
        
        print('cam 1 at ' + t1)
        print('cam 2 at ' + t2)
    
        for j in range(frame_avg):
    
                #take image
            im1[j,:,:] = camera1.grab(device_id = 1)
            im2[j,:,:] = camera2.grab(device_id = 2)
                
        img1[:,:] = np.mean(im1,axis = 0 )
        img2[:,:] = np.mean(im2,axis = 0 )
    
        fig, ax = plt.subplots(2,1)
        ax[0].imshow(img1[:,:])
        ax[1].imshow(img2[:,:])
        plt.show()
        
        time_stamp = get_timestamp()
        with h5py.File(save_path + 'meas_'  +  str(i+1) + '.h5', 'w') as h5:
            h5.attrs["time_stamp"] = time_stamp
            h5["image1"] = im1
            h5["image2"] = im2
            h5["temp1"] = t1
            h5["temp2"] = t2
    
        print('h5 file meas_ ' + str(i) + 'created')
        
        
       
    camera1.close()
    camera2.close()

        
