import os
import sys
import time
import re
import unittest,time

#Before running the script make sure QR and barcode scanner app installed
print("=======================================================================")
print("Wifi enable disable test started")
print("=======================================================================")
from sys import argv
Iterations = argv[1] 

QRcam_pass_TC_count = 0
QRcam_fail_TC_count = 0
Native_pass_TC_count = 0
Native_fail_TC_count = 0
#Device 0 is back camera and this log may vary from device to device
Camsearchitem = "Device 0 is open"
print("Iterations:",Iterations)

def Launch_QRandBarcodecamera():
    os.system("adb shell am start -n com.gamma.scan/com.gamma.barcodeapp.ui.BarcodeCaptureActivity")
    

def Launch_Nativecamera():
    os.system("adb wait-for-device shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
    
def Checkcameralaunchstatus():
    os.system("adb shell dumpsys media.camera > cam.txt")
    time.sleep(5)
    with open('cam.txt') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        if Camsearchitem in line:
            return(True)
        else:
            return(False)

def Checkcameralaunchstatus1():
    os.system( "adb shell dumpsys media.camera > cam1.txt")
    with open("cam1.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="Device 0 is open"
            if(string1 in line):
                #print("connected")
                return(True)   
            else:
                return(False) 
for n in range(int(Iterations)):
    #launch barcode camera
    Launch_QRandBarcodecamera()
    time.sleep(5)
    Camerastatus = Checkcameralaunchstatus1()
    if Camerastatus:
        print("Launch QR scanner camera successfully for iteration:", n)
        QRcam_pass_TC_count = QRcam_pass_TC_count+1
    else:
        print("Launch QR scanner camera failed for iteration:", n)
        QRcam_fail_TC_count = QRcam_fail_TC_count+1    
    Launch_Nativecamera()
    time.sleep(5)
    Camerastatus = Checkcameralaunchstatus1()
    if Camerastatus:
        print("Launch Native camera successfully for iteration:", n)
        Native_pass_TC_count = Native_pass_TC_count+1
    else:
        print("Launch Native camera failed for iteration:", n)
        Native_fail_TC_count = Native_fail_TC_count+1    