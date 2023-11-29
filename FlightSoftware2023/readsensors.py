import time
import serial
import numpy as np

def readsensors(): #no inputs, but could have an input by a filename to save to or similar
    try:
        port_name = '/dev/ttyACM1'
        
        ser = serial.Serial(port_name,9600,timeout=1,rtscts=True)  #change this port to wherever the Arduino is
        time.sleep(1) #to help bootloader
     
        for HH in range(10): #10 is safe, 5 is probably fine
            temp = ser.readline()#this dumps garbage data from reading before line is done writing
        
        vallist = [float('%.2f'%(float(item))) for item in ser.readline().decode().strip().split(",")]
         
        therm_V = float(vallist[11])
        context_V = float(vallist[9])
        lens_V = float(vallist[10])
        heat_V = float(vallist[12])
        known_R = 9800 #housing and context camera thermistor
        lens_known_R = 9800
        therm_R_at25C = 10000
        therm_R = known_R/((1023/therm_V)-1)
        heat_R = known_R/((1023/heat_V)-1)
        context_R = known_R/((1023/context_V)-1)
        try:
            lens_R = lens_known_R/((1023/lens_V)-1)
            lens_B = 3455
            lens_temp = (lens_B*25)/(lens_B + (25*np.log(lens_R/10000)))
        except:
            lens_temp = float('NaN');
        
        #set R->temp fit params
        #thermistor
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

        heat_temp = 1/(a+b*np.log(heat_R/therm_R_at25C)+c*np.log(heat_R/therm_R_at25C)**2+d*np.log(heat_R/therm_R_at25C)**3)
        heat_temp -= 273 

        #context camera and lens heater thermistor
      
        context_B = 3750
        context_temp = (context_B*25)/(context_B + (25*np.log(context_R/10000)))
      
         
        #return list of sensor values
        fin_list = vallist
        fin_list.append(round(therm_temp,3))
        fin_list.append(round(context_temp,3))
        fin_list.append(round(lens_temp,3))
        fin_list.append(round(heat_temp,3))
        fin_list[0] = round((fin_list[0]*.01),6)
        fin_list[3] = round((fin_list[3]*.01),6)
        #fin_list[6] = round((fin_list[6]*.01),6)
        ser.close()
    
        #write to txt files
        filenames = ["press1", "hum1","temp1","press2","hum2","temp2","press3","hum3","temp3","contextVal","lensVal","thermVal","heat_V","thermtemp1","context_temp","lens_temp","heat_temp"]
        dir_name = "/mnt/sdcard/image_data/"
        for NN in range(len(fin_list)):
            f = open(dir_name+filenames[NN]+".txt","w+")
            f.write(str(fin_list[NN]))
            f.close()

        print(fin_list)
    except:
        print('error reading sensors')
        pass

readsensors()

