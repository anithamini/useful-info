import os
import sys
import time
import re
import unittest


print("=======================================================================")
print("Alaram enable disable test started")
print("=======================================================================")

def kill_alaram():
    os.system("adb shell am force-stop com.google.android.deskclock")


def Checkalarmstate():
    os.system( "adb shell dumpsys alarm > alarmon_log.txt")
    with open("alarmon_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="tag=*walarm*:android.content.syncmanager.SYNC_ALARM"
            if(string1 in line):
                print("enabled")
                return(True)
        return(False)
    
def Launch_alarm():
    os.system("adb shell am start -n com.google.android.deskclock/com.android.deskclock.DeskClock")
def Create_alarm():
    os.system("adb shell input tap 375 1250")
    os.system("adb shell input touchscreen swipe 289 807 341 675")
    os.system("adb shell input tap 375 568")
    os.system("adb shell input tap 570 1046")

def toggle_alarm():
     os.system("adb shell input tap 649 327")

kill_alaram()
Launch_alarm()
state = Checkalarmstate()
print(state)
if state:
    toggle_alarm()
Create_alarm()
