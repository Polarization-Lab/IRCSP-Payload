import serial


serial_port = '/dev/ttyACM2'
baud_rate = 9600

ser = serial.Serial(serial_port,baud_rate)
for i in range(3):     
    line = ser.readline().decode('utf-8')
    if line:
        txt = str(line.strip())
        x = txt.split(" ")
        if len(x) ==3:
                ft=open("/mnt/sdcard/image_data/temp.txt","w+")
                fh=open("/mnt/sdcard/image_data/hum.txt","w+")
                fp=open("/mnt/sdcard/image_data/pres.txt","w+")
                ft.write(x[0])
                fh.write(x[1])
                fp.write(x[2])
                ft.close()
                fh.close()
                fp.close()
ser.close()
