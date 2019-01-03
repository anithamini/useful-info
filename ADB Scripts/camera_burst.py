import os
import sys
import time
import re
import unittest,time
Iterations = 3
PC_CNT=0
FC_CNT=0
print("=======================================================================")
print("Selecting Camera burst mode")
print("=======================================================================")

#os.system("adb shell")
#os.system("dumpsys window windows |grep -E 'mCurrentFocus'")
os.system("adb shell am start -n com.android.camera/com.android.camera.CameraPreferenceActivity")
#os.system("adb shell input swipe 301 736 365 127")
os.system("adb shell input tap 344 1075")
os.system("adb shell input keyevent 20")
os.system("adb shell input keyevent 66")
os.system("adb shell input keyevent 3")
for n in range(int(Iterations)):
    #killing camera application
    print("=======================================================================")
    print("Killing background process of Camera")
    print("=======================================================================")
    os.system("adb shell am force-stop com.android.camera")
    #launch camera
    print("=======================================================================")
    print("Launching Camera")
    print("=======================================================================")
    #os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")

    print("=======================================================================")
    print("Capturing Images in Burst mode")
    print("=======================================================================")
    os.system("adb shell input  touchscreen swipe 349 1169 349 1169 2000")
    os.system("adb shell input keyevent 3")
    print("Images captured successfully for iteration:",n)
    n=n+1
    PC_CNT=PC_CNT+1
if (PC_CNT!=0):
    print("Total no.of Iterations captured successfully:",PC_CNT)
else:
    print("Total no.of Iterations failed:",FC_CNT)

