import os
import sys
import time
import re

def kill_camera():
    os.system("adb shell input keyevent 3")
def lanch_camera():
    os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
def capture_camera():
    os.system("adb shell input keyevent KEYCODE_FOCUS")
    os.system("adb shell input keyevent KEYCODE_CAMERA")
    os.system("adb shell input keyevent 66")
    #os.system("adb shell input keyevent 4")
def save_camera():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 3")
def video_camera():
    print("---------")
    os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")
    os.system("adb shell input keyevent KEYCODE_FOCUS")
    os.system("adb shell input keyevent 66")
    time.sleep(10)
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input keyevent 4")
kill_camera()
for i in range(0,3):

    lanch_camera()
    capture_camera()
    save_camera()
#video_camera()
