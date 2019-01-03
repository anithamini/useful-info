import os
import time

def LaunchSettings():
    os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    time.sleep(1)

def KillSettings():
    os.system("adb shell am force-stop com.android.settings.AIRPLANE_MODE_SETTINGS")
    
def Latching():
    for i in range(0,2):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    for i in range(0,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
"""
def switch_LTE():
    os.system("adb shell input keyevent 66")

def switch_3G():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
def switch_2G():
    os.system("adb shell input keyevent 20")
    
    os.system("adb shell input keyevent 66")    
"""

    
KillSettings()
LaunchSettings()
Latching()            
