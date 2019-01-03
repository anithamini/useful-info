                #camera picture delete


import os
#import sys
print("=======================================================================")
print("Camera picture deletion")
print("=======================================================================")
Iterations = 2
def camera_deletion():
#killing camera application
    print("=======================================================================")
    print("Killing background process of Camera")
    print("=======================================================================")
    os.system("adb shell am force-stop com.android.camera")
    #launch camera
    print("=======================================================================")
    print("Launching Camera")
    print("=======================================================================")
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
    os.system("adb shell input keyevent KEYCODE_CAMERA")
    os.system("adb shell input tap 171 1176")
    os.system("adb shell input tap 393 862")
    os.system("adb shell input tap 425 1192")
    os.system("adb shell input tap 478 1182")
    os.system("adb shell input keyevent 3")
for n in range(int(Iterations)):
    camera_deletion()
    print("saved picture "+str(n)+" got deleted")    
