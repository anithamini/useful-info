import os
import time

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")

def wallpaper_setting():  
    os.system("adb shell am start -a android.settings.SETTINGS")
    for i in range(0,5):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    for i in range(0,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")   
    for i in range(0,2):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    for i in range(0,2):
        os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 162 127")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    kill_settings()

kill_settings()
for i in range(0,3):
    wallpaper_setting()
