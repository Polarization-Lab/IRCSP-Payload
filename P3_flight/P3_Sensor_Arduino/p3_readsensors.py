"""
function that reads BME sensors and thermisters
output: "BME1 Pressure (mbar),BME1 Humdity(%),BME1 Temp *C,BME2 Pressure (mbar),BME2 Humdity(%),BME2 Temp *C,Thermister Temp (*C)"
to use this function, in the main Python include "from p3_readsensors import *"

written by Grady Morrissey - 06/06/2022

"""

import time
import serial
import numpy as np
import json #this is how we will save/read data to/from a file in Python

def p3_readsensors(): #no inputs, but could have an input by a filename to save to or similar
    try:
        #ser = serial.Serial('/dev/tty.usbmodem141201',9600,timeout=10)
        ser = serial.Serial('/dev/tty.usbmodem144201',9600,timeout=1,rtscts=True)  #change this port to wherever the Arduino is

        time.sleep(1) #to help bootloader
        
        for HH in range(10): #10 is safe, 5 is probably fine
            temp = ser.readline() #this dumps garbage data from reading before line is done writing
            
        vallist = [float('%.2f'%(float(item))) for item in ser.readline().decode().strip().split(",")]
        
        #convert therm_V to temp
        therm_V = float(vallist[6])
        known_R = 10000
        therm_R_at25C = 10000
        therm_R = known_R/((1023/therm_V)-1)
        #set R->temp fit params
        if therm_R >= 32770:
            a,b,c,d = 3.3570420E-03,2.5214848E-04,3.3743283E-06,-6.4957311E-08
        elif therm_R >= 3599:
            a,b,c,d = 3.3540170E-03, 2.5617244E-04, 2.1400943E-06, -7.2405219E-08
        elif therm_R >= 681.6:
            a,b,c,d = 3.3530481E-03 , 2.5420230E-04, 1.1431163E-06, -6.9383563E-08
        else:
            a,b,c,d = 3.3536166E-03, 2.5377200E-04, 8.5433271E-07, -8.7912262E-08
        therm_temp = 1/(a+b*np.log(therm_R/therm_R_at25C)+c*np.log(therm_R/therm_R_at25C)**2+d*np.log(therm_R/therm_R_at25C)**3) #in K
        therm_temp -= 273 #in C
        
        #return list of sensor values
        fin_list = vallist
        fin_list[6] = round(therm_temp,3)
        ser.close()
        return fin_list
    except:
        return p3_readsensors()

##for testing
#t1=[]
#t2=[]
#t3=[]
#nlist=[]
#for n in range(400):
#    dat = p3_readsensors()
#    print(n, dat)
#    t1.append(dat[2])
#    t2.append(dat[5])
#    t3.append(dat[6])
#    nlist.append(n)
#
#import matplotlib.pyplot as plt
#
#plt.figure(0)
#plt.scatter(nlist,t1,color='r',label="BME1")
#plt.scatter(nlist,t2,color='b',label="BME2")
#plt.scatter(nlist,t3,color='y',label="thermister")
#
#plt.title("temp comparisons")
#plt.xlabel("time")
#plt.ylabel("deg C")
#plt.legend()
#
#plt.savefig("plots/tempcmpr1")
#
#plt.show()

"""
#can use this to save data to a file

        #now save data
        filename = "sensordat.json"
        with open(filename, 'w') as outfile:
            json.dump(fin_list, outfile)

        with open(filename, 'r') as json_file:
            test = json.load(json_file)

        print(test)
"""
