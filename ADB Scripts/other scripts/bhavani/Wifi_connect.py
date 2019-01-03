import os
import time
import sys
import re

def launch_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
def toggle_wifi():
    #os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    os.system("adb shell input tap 250 220")

def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    bt_log = open("wifi_log.txt","r+")
    buffer = bt_log.readline();
    bt_log.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

def CheckwifiConnectedstate():
    print("......checking connection......")
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    with open("wifi_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="curState=OnlineState"
            if(string1 in line):
                print("connected")
                return(True)

def wifi_connecting():
    print("connecting to coolpad 3505l_01A3")
    os.system("adb shell input tap 370 840")
    os.system("adb shell input text amani1234")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(5)

launch_wifi()
state = Checkwifistate()
print(state)
if not state:
    toggle_wifi()
time.sleep(5)
Connectedstate = CheckwifiConnectedstate()
if Connectedstate:
    print("Connected to scaned network successfully ")
else:
    print("Not connected ")
    wifi_connecting()
    CheckwifiConnectedstate()


