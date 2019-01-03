import os
import re
from time import sleep

def GPS_ON():
        print("Enabling GPS.........")
        os.system("adb shell settings put secure location_providers_allowed +gps")

def GPS_OFF():
        print("Disabling GPS.........")
        os.system("adb shell settings put secure location_providers_allowed -gps")

def validation():
    os.system("adb shell dumpsys location>text.txt")
    str1="mStarted=false"
    with open("text.txt","r") as fd:
        buf=fd.read()
    if(re.search(str1,buf,re.I)):
        return(True)
    else:
        return(False)

#To check whether GPS is ON or OFF just to print the statement
if(validation()):
    print("GPS is diabled.....So enabling GPS now")
    GPS_ON()
    sleep(5)
    print("GPS is enabled....So disabling GPS now")
    GPS_OFF() 
else:
    print("GPS is enabled....So disabling GPS now")
    GPS_OFF()

