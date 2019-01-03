             #camera burst mode

import os
import time
import re
print("=======================================================================")
print("Camera burst mode")
print("=======================================================================")
Iterations = 2
def kill_camera():
     print("Killing background process of Camera")
     os.system("adb shell am force-stop com.android.camera")
def launch_camera():     
     os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
def checkcamera_mode():    
    os.system("adb shell dumpsys media.camera > cam.txt")
    with open("cam.txt","r") as fp:
        str1=fp.read()
        if(("Device 0 is open" in str1)or("Device 1 is closed" in str1)):
            return True   
        return False
def camera_burst():    
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
    os.system("adb shell am start -n com.android.camera/com.android.camera.CameraPreferenceActivity")
    os.system("adb shell input tap 148 1168")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 3")
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
    print("Capturing Images in Burst mode")
    os.system("adb shell input  touchscreen swipe 349 1169 349 1169 2000")
    os.system("adb shell input keyevent 3")
launch_camera()
if(checkcamera_mode()):
    camera_burst()       
else:
    print("burst mode is not possible in front camera..... so change into back camera")
    camera_burst()
kill_camera()



