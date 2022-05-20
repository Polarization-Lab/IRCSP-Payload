"""
Created on Fri May 20 12:25:25 2022

@author: jaclynjohn
"""

def main():
    
    from instrument_control import P3_image_capture
    import time 
    
    wait = 60 #seconds
    i = 0;
    while i < 240: #over 4 hours later: each loop will be a little over than 30 seconds 
    #since it will wait 30 seconds before doing everything again
    
        P3_image_capture()
        #saves 10 frames, two temperatures, and a timestamp into h5 file on Hamilton laptop
        #displays temperature of FPA
        #displays image for each camera that is average of 10 frames to show SaSa students
        
        #P3_read_BME()
        #will save pres,temp,hum from each sensor into one h5 file on Hamilton laptop
        #will label it BME_1..2...3 etc to match meas_1...2...3 from image capture
        #will print out info so I can monitor
        
        #P3_read_therm()
        #will save temperature from each thermistor into one h5 file
        #will label it therm_1..2...3 etc to match meas_1...2...3 from image capture
        #will print out info so I can monitor

        

        time.sleep(wait)
        i +=1
        
