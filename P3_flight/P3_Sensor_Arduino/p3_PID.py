"""
function that reads/writes to PID

written by Grady Morrissey - 05/24/2022

"""

import serial

ser = serial.Serial(port='/dev/tty.usbserial-14230', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

command=input("cmd: ")
while command != "stop":
    ser.write(command.encode())
    received1 = ser.readline()
    received2 = ser.readline()
    msg1 = received1.decode()
    msg2 = received2.decode()
    print(msg1,"\n",msg2)
    command=input("cmd: ")

