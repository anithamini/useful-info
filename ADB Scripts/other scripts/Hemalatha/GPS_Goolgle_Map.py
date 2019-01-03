import os
import re
from time import sleep
def kill_map():
    os.system("adb shell am force-stop com.google.android.apps.maps")
    sleep(1)
def Google_map_launch():
    os.system("adb shell am start -n com.google.android.apps.maps/com.google.android.maps.MapsActivity")
def search_location():
    os.system("adb shell input tap 349 109")
    sleep(2)
    string1=input("Enter the destination location....")
    os.system("adb shell input text " + string1)
    os.system("adb shell input keyevent 66")
def check_GPS():
    os.system("adb shell dumpsys locationpolicy>gps.txt")
    str1="mLocationMode=3"
    with open("gps.txt","r") as fd:
        buf=fd.read()
    if(re.search(str1,buf,re.I)):
        return(True)
    else:
        return(False)
def check_data():
    os.system("adb shell dumpsys network_management>data.txt")
    string="networkCount=1"
    with open("data.txt","r") as fd:
        buff=fd.read()
    if(re.search(string,buff,re.I)):
        return(True)
    else:
        return(False)
def GPS_ON_OFF():
    os.system("adb shell input touchscreen swipe 655 25  625 1000")
    os.system("adb shell input touchscreen swipe 585 888 96 849")
    os.system("adb shell input touchscreen swipe 343 939 359 22")
    os.system("adb shell input tap 279 555")
    sleep(2)
    os.system("adb shell input keyevent 3")
def data_ON_OFF():
    os.system("adb shell input touchscreen swipe 655 25  625 1000")
    os.system("adb shell input touchscreen swipe 585 888 96 849")
    os.system("adb shell input tap 72 551")
    sleep(2)
    os.system("adb shell input keyevent 3")

data_ON_OFF()
sleep(1)
GPS_ON_OFF()
kill_map()
Google_map_launch()
sleep(2)
search_location()
if(check_data()==0):
    print("U are offline...Please enable mobile data....")
    if(check_GPS()==0):
        print("GPS is disabled...Please enable GPS.....")
else:
    print("Location searched successfully....")
    
