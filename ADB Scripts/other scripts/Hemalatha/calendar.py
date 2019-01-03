import os
import sys
import time
import re
import unittest,time
Iterations=3
def launch_calendar():
    print("=======================================================================")
    print("Launching Calendar applications")
    print("=======================================================================")
    os.system("adb shell am start -n com.android.calendar/com.android.calendar.homepage.AllInOneActivity")
def create_event(n1):
    print("=======================================================================")
    print("Creating event")
    print("=======================================================================")
    os.system("adb shell input tap 641 1204")
    os.system("adb shell input keyevent 21")
    if n1==0:
        os.system("adb shell input text Hema")
    elif n1==1:
        os.system("adb shell input text Anitha")
    else:
        os.system("adb shell input text Subhashini")
  
    os.system("adb shell input tap 639 94")
def delete_event():
    print("=======================================================================")
    print("Deleting event")
    print("=======================================================================")
    os.system("adb shell input tap 315 901")
    os.system("adb shell input tap 418 1184")
    os.system("adb shell input tap 528 1190")
def kill_calendar():
    print("========================================================================")
    print("Killing Calendar application")
    print("========================================================================")
    os.system("adb shell am force-stop com.android.calendar")    
for n in range(int(Iterations)):
    print("For iteration:",n+1)
    launch_calendar()
    create_event(n)
    delete_event()
    kill_calendar()

