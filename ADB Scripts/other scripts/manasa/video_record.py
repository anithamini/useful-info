import os
import sys
import re
import unittest,time


def launchvideo():
    print("*********** Opening Video *****************")
    os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")  #launches videorecorder
    print("*********** Recording video ***************")
    os.system("adb shell input keyevent KEYCODE_CAMERA")                   #starts playing video
    time.sleep(30)                                                         #video records for 30 sec
    os.system("adb shell input keyevent KEYCODE_DPAD_CENTER")              #video recording will be off
    os.system("adb shell input keyevent KEYCODE_DPAD_RIGHT")               #select save or cancelling the video
    os.system("adb shell input keyevent KEYCODE_ENTER")

    
def killvideo():
    print("*********** Closing the Video *************")
    os.system("adb shell am force-stop com.android.camera")


launchvideo()
time.sleep(2)                                                              #2 sec delay before killing application
killvideo()
