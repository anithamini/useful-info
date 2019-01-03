import os
import sys
import time
import re
import unittest,time

print("=======================================================================")
print("Wifi enable disable test started")
print("=======================================================================")
Iterations = 2

pass_TC_count = 0
fail_TC_count = 0
print("Iterations:",Iterations)

def Checkstate_wifi():
    os.system("adb shell dumpsys wifi>wifi_log.txt")
    wifi_fd=open("wifi_log.txt","r+")
    buffer=wifi_fd.readline()
    wifi_fd.close()
    enable=re.search('Wi-Fi is enabled',buffer,re.I)
    if enable:
        return(True)
    else:
        return False
def toggle_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings ")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
def checkwifi_connection():
    os.system("adb shell input tap 313 407")
    time.sleep(10)
    os.system("adb shell dumpsys wifi>wifi_log.txt")
    with open("wifi_log.txt","r+")as fd:
        lines=fh.readlines()
        for line in lines:
            
state=Checkstate_wifi()
print(state)
if state:
    toggle_wifi()

for n in range(int(Iterations)):
    toggle_wifi()
    time.sleep(5)
    connectstate=checkwifi_connection()
