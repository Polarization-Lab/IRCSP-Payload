#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:19:08 2021

@author: kirahart
"""
import numpy as np
import h5py
from IRCSP.calibration.NUC.NUC_functions import pixel_registration
import scipy


#choose filepath to desired data
path = '/Volumes/KESU/may19/LUTS/'
#note cam definitions are flipped as of FLIRPY ffc fix 
cal_file2 =  '/Volumes/KESU/calibration_files/cam1pixel.h5'
cal_file1 =  '/Volumes/KESU/calibration_files/cam2pixel.h5'

waves= np.linspace(7,12,61)
TEMPS = np.linspace(25,80,12)


'''LOAD slope from 2 point NUC'''
#choose filepath to desired data
save_path =   '/Volumes/KESU/calibration_files/'
name =  "NUC.h5" 

hf = h5py.File(save_path+name, 'r')
M1 = hf.get('M1')
M2 = hf.get('M2')
T1 = hf.get('Tref1')
T2 = hf.get('Tref2')
ROI1 = hf.get('ROI1')
ROI2 = hf.get('ROI2')