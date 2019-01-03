import os
import sys
import time
import re

"""below function used for kill settings if open seyttings"""
def killsettings():
    os.system("adb shell am force-stop com.android.settings")
    
""" below function launching the settings"""
def launchsettings():
    os.system("adb shell am start -n com.android.settings/com.android.settings.HWSettings")

"""below function used for wallpaper will be open"""
def displaysearch():
    os.system("adb shell input tap 480 290")
    os.system("adb shell input text display")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")#set wallpaper settings
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 66")
"""below function for select the image for standard and
below function display for selecting normal image"""
def selectimage():
    os.system("adb shell input tap 540 1940")
    os.system("adb shell input tap 995 105")
    os.system("adb shell input tap 600 1785")
    print("your wallpaper is selected")
"""below fucntion for selecting image from gallery"""
def galleryimage():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 330 1958")
    os.system("adb shell input tap 160 1400")
    os.system("adb shell input tap 684 1440")
    os.system("adb shell input tap 1010 130")
    os.system("adb shell input tap 600 1785")
"""below function used for changing the wallpaper for every 5 mins"""
def randomhome():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    
    
killsettings()
print("settings killed")
launchsettings()
print("settigns launched")
time.sleep(2)
displaysearch()
print("wallpaper selected")
selectimage()
print("standard image selected")
time.sleep(3)
galleryimage()
time.sleep(2)
print("image selected from gallery")
randomhome()
print("randomly change home screen wallpaper is on")s
time.sleep(360)
print("image changed")
killsettings()

