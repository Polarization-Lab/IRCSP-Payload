"""
function that reads/writes to PID
assumes standard PID output of form "Tz=+19.00 P= 0.00 I= 0.00 D=20.00 T=-15...+30 Tr=+43.34 OC=1 PW=+100"

This code can read output, but as of June 8 readline does not return anything. Once the PID can be read again the commented lines in this code are very useful

written by Grady Morrissey - 06/3/2022

"""

import serial
import time
import re

def p3_PID(set_temp): #null input for simple lineread

    try:
        port_name = '/dev/tty.usbserial-144130'
        ser = serial.Serial(port=port_name, baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=0, rtscts=0)
        time.sleep(1)
        s = "<"+str(set_temp)+" 20 0 0 -15 30>"
        ser.write(s.encode())
    except:
        print ("PID write failed")
    
    #there is an error with not being able to read output from the PID, so instead we will just write to the PID and assume it writes correctly (evidence shows it does)
    
    """
    print(ser.write("R".encode())) #starts PID output
    
    #get a list of previous PID output
    temp1 = ser.readline()
    print(temp1)
    temp2 = ser.readline()
    
    prev_dat = ser.readline().decode()
    #prev_dat="Tz=+19.00 P=20.00 I= 0.00 D= 0.00 T=-15...+30 Tr=+26.42 OC=0 PW=-100"
    print ("prev", prev_dat)
    
    def PIDout_to_lst(prev_dat): #takes decoded output from PID
    
        prev_dat_lst = []
        HH = 0
        while HH < len(prev_dat):
            if prev_dat[HH] == "=" or prev_dat[HH] == ".":
                prev_dat_lst.append(prev_dat[HH+1])
                HH+=2
                while ((HH < len(prev_dat)) and prev_dat[HH] not in ["P","I","D","T","O"]):
                    if prev_dat[HH] == "." and prev_dat[HH+1] == ".":  #if we've hit the ellipsis
                        HH+=2
                        break
                    else:
                        prev_dat_lst[len(prev_dat_lst)-1] = prev_dat_lst[len(prev_dat_lst)-1]+prev_dat[HH]
                        HH+=1
            else:
                HH+=1
    
        prev_dat_lst = [float(item) for item in prev_dat_lst]

        return prev_dat_lst
    
    prev_dat_lst = PIDout_to_lst(prev_dat)
    print (prev_dat_lst)
    
    if (set_temp):  #overwrite temp if given
        s = str(set_temp)
        for item in prev_dat_lst[0:6]:
            s += " "+str(item)
        s='<'+s+'>'
        print (s)
        ser.write(s.encode())
    
    ser.close() #cycle serial
    time.sleep(1)
    ser = serial.Serial(port=port_name, baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
    time.sleep(1)
    ser.write("R".encode())
    time.sleep(1)
    temp=ser.readline()
    temp=ser.readline()
    new_dat = ser.readline().decode()
    print("new",new_dat)
    ser.close() #cycle serial
    
    
    
    return PIDout_to_lst(new_dat)
    """

p3_PID(20)
