import os
import sys
import time
import re
import unittest,time


print("=======================================================================")
print("Wifi enable disable test started")
print("=======================================================================")
from sys import argv
Iterations = argv[1] 

pass_TC_count = 0
fail_TC_count = 0
print("Iterations:",Iterations)

def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wlan_log.txt")
    wlan_log = open("wlan_log.txt","r+")
    buffer = wlan_log.readline();
    wlan_log.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

def CheckwifiConnectedstate():
    os.system( "adb shell dumpsys wifi > wlan_log.txt")
    with open("wlan_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="SSID: IM_Mobiles"
            if(string1 in line):
                #print("connected")
                return(True)

def Toggle_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 23")
    time.sleep(5)
#Turn OFF wifi before starting testcases
#checking for wifi state
state = Checkwifistate()
print(state)
if state:
    Toggle_wifi()
    
for n in range(int(Iterations)):
    Toggle_wifi()
    time.sleep(5)
    Connectedstate = CheckwifiConnectedstate()
    if Connectedstate:
        print("Connected to presaved wifi successfully for iteration:", n)
        pass_TC_count = pass_TC_count+1
    else:
        print("Not connected to presaved wifi  for iteration:", n)
        fail_TC_count = fail_TC_count+1
    n+1
    Toggle_wifi()
print("Wifi preset connection Passed:",pass_TC_count )
print("Wifi preset connection Failed:",fail_TC_count )
