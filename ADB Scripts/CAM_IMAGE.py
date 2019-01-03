import os
import sys
import time
#CAMERA IMAGE CAPTURING
#killing camera application
#os.system("adb shell am force-stop com.android.camera")
#launch camera
#os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 1")
#for backcam
"""
os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
#os.system("adb shell input keyevent 23")
#os.system("adb shell input keyevent 66")
os.system("adb shell input keyevent KEYCODE_CAMERA")
#for frontcam
os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 1")
"""
os.system("adb shell input keyevent KEYCODE_CAMERA")
#os.system("adb shell input keyevent 23")
#os.system("adb shell input keyevent 66")
time.sleep(5)
#os.system("adb shell input keyevent 4")
os.system("adb shell am force-stop com.android.camera")
"""
#kill camera
os.system("adb shell am force-stop com.android.camera")
"""
