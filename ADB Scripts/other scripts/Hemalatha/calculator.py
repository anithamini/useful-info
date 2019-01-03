import os
import sys
import time
import re
import unittest,time
Iterations=3
def launch_calc():
    print("=======================================================================")
    print("Launching Calculator application")
    print("=======================================================================")
    os.system("adb shell am start -n com.wingtech.calc/com.wingtech.calc.Calculator")
def Standard_mode():
    print("=======================================================================")
    print("Changing to Standard Mode")
    print("=======================================================================")
    os.system("adb shell input tap 107 418")
    time.sleep(2)
    os.system("adb shell input keyevent 8")
    os.system("adb shell input keyevent 8")
    os.system("adb shell input keyevent 67")
    os.system("adb shell input tap 609 887")
    os.system("adb shell input keyevent 10")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 107 580")
def Scientific_mode():
    print("========================================================================")
    print("Changing to Scientific Mode")
    print("========================================================================")
    os.system("adb shell input tap 186 451")
    time.sleep(2)
    os.system("adb shell input keyevent 8")
    os.system("adb shell input keyevent 8")
    os.system("adb shell input keyevent 67")
    os.system("adb shell input tap 609 887")
    os.system("adb shell input keyevent 10")
    os.system("adb shell input keyevent 66")
def kill_calc():
    print("========================================================================")
    print("Killing Calculator application")
    print("========================================================================")
    os.system("adb shell am force-stop com.wingtech.calc")
for n in range(int(Iterations)):
    launch_calc()
    print("For iteration:",n+1)
    Standard_mode()
    Scientific_mode()
    kill_calc()

    
