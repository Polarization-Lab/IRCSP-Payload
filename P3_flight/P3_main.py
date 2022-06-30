# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:25:25 2022

@author: jaclynjohn
"""
import h5py
import time 
import csv
import matplotlib.pyplot as plt
import timeit
import numpy as np


def get_timestamp():
    t = time.localtime()
    return time.strftime('%H.%M.%S', t)


def main():
    
    from P3_readsensors import p3_readsensors
    from P3_image_capture import P3_image_capture
    
    
    save_path = 'C:\\Users\\khart\\Documents\\Summer2022Campaign\\IRCSP2\\Flights\\TestFlight06302022\\'

    i = 0;
    time_start = timeit.timeit()
    cam1t = []
    cam2t = []
    ambient = []
    enclosure = []
    time_elapsed = []
    while True:
        
        try:
            timestamp = get_timestamp() #take time at start of measurement 
            cameradata = P3_image_capture()
            
            im1 = cameradata[0]
            im2 = cameradata[1]
            t1 = cameradata[2]
            t2 = cameradata[3]
            
        except:
            print('error with camera aquisition')
            t1 = None
            t2 = None
            pass
        
        try:     
            
            with h5py.File(save_path +  'meas_' + str(i) + '.h5', 'w') as h5:
                h5.attrs["timestamp"] = timestamp
                h5["image1"] = im1
                h5["image2"] = im2
                h5["temp1"] = t1
                h5["temp2"] = t2
             
            print('h5 file meas_' + str(i) + ' created')
         
        except: 
            print('h5 file could not be saved')
            
            
        try:
            sensordata = p3_readsensors()  
            sensordata.append(t1)
            sensordata.append(t2)
            sensordata.append(timestamp)
            sensordata.append(i) #measurement number
            print(sensordata)
       
        except:
            print('BME sensor error')
            sensordata = []
            pass
            
    
        try:
            with open(save_path + 'telemetry.csv', 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(sensordata)
        except:
            print('error writing csv')
            pass
            
            
        i +=1
        
        try:
            cam1t.append(t1)
            cam2t.append(t2)
            ambient.append(sensordata[6])
            enclosure.append(sensordata[2])
            time_elapsed.append(timeit.timeit()-time_start)
        except: 
            pass
            
        plt.plot(cam1t,label = "Camera 1")
        plt.plot(cam2t,label = "Camera 2")
        plt.plot(enclosure,label = "Enclosure")
        plt.plot(ambient,label = "Housing")
        plt.ylabel("Temperature [c]")
        plt.legend()
        plt.show()
            
     
