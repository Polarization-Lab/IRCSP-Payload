import time 
import datetime
import os

try:
    now = datetime.datetime.now()
    OS_time = now.strftime("%H.%M.%S")
    print(OS_time)

except:
    print("error")
