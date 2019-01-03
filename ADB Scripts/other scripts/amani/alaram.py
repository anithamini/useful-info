import os
import sys
import time
import re


print("==============================
=========================================")
print("Alaram enable disable test started")
print("=======================================================================")

def kill_alaram():
    os.system("adb shell am force-stop com.yulong.android.xtime")
def lanch_alaram():
    os.system("adb shell am start -n com.yulong.android.xtime/yulong.xtime.ui.main.XTimeActivity")
def dn_right_enter():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")

def set_alaram():
    os.system("adb shell input tap 358 1209")
    #os.system("adb shell input touchscreen swipe 218 331 215 430")
    os.system("adb shell input touchscreen swipe 371 331 362 221")
    os.system("adb shell input touchscreen swipe 371 331 362 221")
    #os.system("adb shell input touchscreen swipe 491 336 505 430")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    for i in range (0,5):
        os.system("adb shell input keyevent 66")
        os.system("adb shell input keyevent 22")
    os.system("adb shell input tap 324 812")
    os.system("adb shell input text mrng")
    dn_right_enter()
    os.system("adb shell input tap 617 921")
    os.system("adb shell input tap 351 1036")
    dn_right_enter()
    os.system("adb shell input tap 312 1144")
    os.system("adb shell input tap 126 642")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 4")
    dn_right_enter()
    
    
def delete_alaram():
    os.system("adb shell input touchscreen swipe 279 232 279 232 1000")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    dn_right_enter()
    os.system("adb shell input keyevent 3")
"""def onoff_alaram():
    os.system("adb shell input touchscreen swipe 284 262 284 262 1000")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")"""
    

def toggle_alaram():
     os.system("adb shell input tap 622 246")    
def snooze_alaram():
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 66")
def turnoff_alaram():
    os.system("adb shell input touchscreen swipe 248 1211 485 1218 1000")



kill_alaram()
lanch_alaram()
#onoff_alaram()
set_alaram()
time.sleep(62)
print "enter option for selection of snooze or turnoff alarm"
if(input("enter 1 for snooze 0 for turnoff :")):
    snooze_alaram()
else:
    turnoff_alaram()
#toggle_alaram()
delete_alaram()


