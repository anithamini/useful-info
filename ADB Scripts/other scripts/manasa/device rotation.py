import os
import sys
import time
import re
import unittest,time

def Protrait_mode():
    print("setting the device into Protrait mode")
    os.system("adb shell settings put system user_rotation 0")
    time.sleep(5)
    print("setting the device into Protrait reverse mode")
    os.system("adb shell settings put system user_rotation 2")

def Landscape_mode():
    print("setting the device into Landscape mode")
    os.system("adb shell settings put system user_rotation 1")
    time.sleep(5)
    print("setting the device into Landscape reverse mode")
    os.system("adb shell settings put system user_rotation 3")

def launch_statusbar():
    print("dragging statusbar")
    os.system("adb shell service call statusbar 1")

def close_statusbar():
    print("collapsing the statusbar")
    os.system("adb shell service call statusbar 2")

def screen_rotation():   
    print("checking the screen rotation enable and disable in status bar")
    launch_statusbar()
    print("screen  auto rotation is enabled")
    os.system("adb shell settings put system accelerometer_rotation 1")
    gallery_launcher()
    kill_gallery()
    print("screen auto rotation is disabled")
    os.system("adb shell settings put system accelerometer_rotation 0")
    close_statusbar()

def gallery_launcher():
    print("Opening the Gallery")
    os.system("adb shell monkey -p com.android.gallery3d 1")
    print("selecting image from album")
    os.system("adb shell input tap 530 340")

def kill_gallery():
    print("exiting the gallery")
    os.system( "adb shell am force-stop com.android.gallery3d")


gallery_launcher()
time.sleep(5)
Protrait_mode()
time.sleep(5)
Landscape_mode()
kill_gallery()
#screen rotation will only work manually i.e., when device is rotated by end-user the images will be rotated
screen_rotation() 


    



