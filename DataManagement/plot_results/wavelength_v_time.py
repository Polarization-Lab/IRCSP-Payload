#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:15:33 2021

@author: kirahart
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#user input
wavelength = 9;


#filenames
fn1 = '/Volumes/KESU/SQL_Queries/raw_data/' + str(wavelength)+'micron_camera1.csv'
fn2 = '/Volumes/KESU/SQL_Queries/raw_data/' + str(wavelength)+'micron_camera2.csv'

#create databases 
df1 = avg_monthly_precip = pd.read_csv(fn1)
df2 = avg_monthly_precip = pd.read_csv(fn2)