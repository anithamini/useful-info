import os
import sys
import time
import re
import unittest,time

from sys import argv
Iterations = 1 #argv[1] 

def Killcam():
    os.system( "adb shell am force-stop com.android.camera")

def Launchcam():
    os.system( "adb shell am start -a android.media.action.IMAGE_CAPTURE")
    os.system("adb shell dumpsys media.camera > cam1.txt")
def capture():
    os.system("adb shell input keyevent 125")
    os.system("adb shell input keyevent 27")
    os.system("adb shell dumpsys media.camera > cam2.txt")
Killcam()
Launchcam()
for n in range(int(Iterations)):
    capture()
