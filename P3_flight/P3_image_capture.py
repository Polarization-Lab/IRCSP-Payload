# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:46:32 2022

@author: jaclynjohn
"""


from   flirpy.camera.boson import Boson 
import matplotlib.pyplot as plt
import h5py
import numpy as np
import time 

#from datetime import datetime


def P3_image_capture():
    
    frame_avg = 10

    """DO NOT CHANGE"""
    camera1 = Boson(port='COM15')
    camera2 = Boson(port='COM16')

    #set FFC to manual
    camera1.set_ffc_manual() 
    camera2.set_ffc_manual()

    img1 = np.zeros((256,320))
    img2 = np.zeros((256,320))
    im1 = np.zeros((frame_avg,256,320))
    im2 = np.zeros((frame_avg,256,320))
    
    t1 = camera1.get_fpa_temperature()
    t2 = camera2.get_fpa_temperature()
    
    print('cam 1 at ' + str(t1))
    print('cam 2 at ' + str(t2))

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
    
    
    return im1,im2,t1,t2
           
    camera1.close()
    camera2.close()
    
    

        
        
