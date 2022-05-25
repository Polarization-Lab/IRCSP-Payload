# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:25:25 2022

@author: jaclynjohn
"""
from   flirpy.camera.boson import Boson 
import matplotlib.pyplot as plt
import h5py
import numpy as np
import time 
import serial
import csv


def get_timestamp():
    t = time.localtime()
    return time.strftime('%H.%M.%S', t)


def main():
    
    from p3_readsensors import p3_readsensors
    from P3_image_capture import P3_image_capture
    
    
    save_path = 'C:\\Users\\khart\\Documents\\Summer2022Campaign\\IRCSP1\\TestRuns\\streamingdata\\'

    wait = 5 #seconds
    i = 0;
    while i < 40: 

        timestamp = get_timestamp() #take time at start of measurement 
        epoch = time.time()
        
        IRCSPdata = P3_image_capture()
        
        im1 = IRCSPdata[0]
        im2 = IRCSPdata[1]
        t1 = IRCSPdata[2]
        t2 = IRCSPdata[3]

    
        sensordata = p3_readsensors()
        sensordata.append(timestamp)
        
        
        with h5py.File(save_path +  'meas_' + str(i) + '.h5', 'w') as h5:
            h5.attrs["timestamp"] = timestamp
            h5.attrs['epochtime'] = epoch
            h5["image1"] = im1
            h5["image2"] = im2
            h5["temp1"] = t1
            h5["temp2"] = t2
        
    
        print('h5 file meas_' + str(i) + ' created')

        with open(save_path + 'telemetry.csv', 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(sensordata)
        
        time.sleep(wait)
        i +=1
        
