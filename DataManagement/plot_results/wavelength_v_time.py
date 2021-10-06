#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:15:33 2021

@author: kirahart
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


#user input
wavelength = 9;


#filenames
fn1 = '/Volumes/KESU/SQL_Queries/raw_data/' + str(wavelength)+'micron_camera1.csv'
fn2 = '/Volumes/KESU/SQL_Queries/raw_data/' + str(wavelength)+'micron_camera2.csv'

#create databases 
df1 = pd.read_csv(fn1)
df2 = pd.read_csv(fn2)

dftelem = pd.read_csv('/Volumes/KESU/SQL_Queries/Measurements.csv')


x1 = df1.query('position==125 & id>1366')['id']
y1 = df1.query('position==125 & id>1366')['val']
y2 = df1.query('position==120 & id>1366')['val']
plt.plot(x1,y1)
plt.plot(dftelem.query('meas_id>1366')['time'],df1.query('position==120 & id>1366')['val'])