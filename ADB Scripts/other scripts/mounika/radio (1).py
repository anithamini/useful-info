import os
import sys
import time
import re
"""def killradio():
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 3")"""
def killradio1():
    os.system("adb shell am force-stop com.mediatek.fmradio")
    os.system("adb shell input keyevent 3 ")
def checkstate():
    os.system("adb logcat -b radio -v time -d > radiofile2.log")
    radio_log=open("radiofile2.log","r")
    buffer=radio_log.read();
    print buffer
    radio_log.close()
    enabled=re.search("RadioState is RADIO_ON",buffer,re.I)
    if enabled:
        return(True)
    else:
        return(False)
def launchradio():
    enabled=input("enter the 1 for enabled 0 for disbaled radio")
    if enabled:
        os.system("adb shell input touchscreen swipe 710 713 28 642 1000")
        os.system("adb shell input tap 458 158")
        os.system("adb shell input tap 375 390")
    else:
        os.system("adb shell input touchscreen swipe 710 713 28 642 1000")
        os.system("adb shell input tap 458 158")
        os.system("adb shell input tap 375 390")
        os.system("adb shell input tap 80 120")
killradio1()
state=checkstate()
print state
if state:
    launchradio()
    state=checkstate()
    print state
else:
    time.sleep(2)
    launchradio()
    state=checkstate()
    print state

