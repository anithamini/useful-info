import os
import sys
import time
import re

def killsettings():
    os.system("adb shell am force-stop com.android.settings")
def launchsettings():
    os.system("adb shell am start -n com.android.settings/com.android.settings.HWSettings")

def advanced_settings():
    ser="Advanced"
    os.system("adb shell input tap 550 300")
    time.sleep(2)
    os.system("adb shell input text " +ser)
    os.system("adb shell input tap 525 1070")
def language_settings():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 550 450")
    os.system("adb shell input tap 1030 150")
    os.system("adb shell input text english")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")#here language is changed
    
    
killsettings()
print "settings killed"
launchsettings()
print "settigns opened"
advanced_settings()
language_settings()
killsettings()

