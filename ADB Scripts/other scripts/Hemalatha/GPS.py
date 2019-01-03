import os
import re
from time import sleep
def GPS_ON_OFF():
    os.system("adb shell input touchscreen swipe 655 25  625 1000")
    os.system("adb shell input touchscreen swipe 585 888 96 849")
    os.system("adb shell input touchscreen swipe 343 939 359 22")
    os.system("adb shell input tap 279 555")
    sleep(2)
    os.system("adb shell input keyevent 3")
def validation():
    os.system("adb shell dumpsys locationpolicy>text.txt")
    str1="mLocationMode=3"
    with open("text.txt","r") as fd:
        buf=fd.read()
    if(re.search(str1,buf,re.I)):
        return(True)
    else:
        return(False)
#To check whether GPS is ON or OFF just to print the statement
if(validation()):
    print("Disabling GPS....")
else:
    print("Enabling GPS....")
GPS_ON_OFF()
if(validation()):
    print("GPS is Enabled successfully........")
else:
    print("GPS is Disabled successfully..........")
sleep(1)
if(validation()):
    print("Disabling GPS....")
else:
    print("Enabling GPS....")
GPS_ON_OFF()
