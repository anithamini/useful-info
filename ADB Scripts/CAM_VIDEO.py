import os
import sys
import time
#CAMERA VIDEO RECORDING
#killing camera application
os.system("adb shell am force-stop com.android.camera")
#launch video camera
os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")
#for back 
#os.system("adb shell am start -a android.media.action.STILL_VIDEO_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
os.system("adb shell input keyevent KEYCODE_CAMERA")
time.sleep(5)
os.system("adb shell input keyevent KEYCODE_CAMERA")
#for front
#os.system("adb shell am start -a android.media.action.STILL_VIDEO_CAMERA --ei android.intent.extras.CAMERA_FACING 1")
os.system("adb shell input keyevent 22")
os.system("adb shell input keyevent 66")
os.system("adb shell input keyevent KEYCODE_CAMERA")
time.sleep(5)
os.system("adb shell input keyevent KEYCODE_CAMERA")
