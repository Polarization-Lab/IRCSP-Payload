"""
function that reads BME sensors and thermisters
output: "BME1 Pressure (mbar),BME1 Humdity(%),BME1 Temp *C,BME2 Pressure (mbar),BME2 Humdity(%),BME2 Temp *C,Thermister Temp (*C)"
to use this function, in the main Python include "from p3_readsensors import *"

written by Grady Morrissey - 05/24/2022

"""

import time
import serial
import numpy as np
import json #this is how we will save/read data to/from a file in Python

def p3_readsensors(): #no inputs, but could have an input by a filename to save to or similar
    
    try:  #this try except statement is just in case the code errors, probably isn't necessary but would avoid a crash if it happened
        while True:
            #time.sleep(.1)
            ser = serial.Serial('/dev/tty.usbmodem141201',9600)
            line = ser.readline()
            str = line.decode()
            stripped_str = str.strip()
            vallist = stripped_str.split(",")
            vallist = [float(item) for item in vallist]
            if len(vallist) == 7:  #recursively looks for sensor vals until it works
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
                fin_list[6] = therm_temp
                return fin_list
                break
        ser.close()
    except:
        return [None for YY in range(7)]
            
            
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
