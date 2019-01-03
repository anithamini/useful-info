import os
from sys import argv
from time import sleep
Frontpasscnt = 0
Frontfailcnt = 0
Rearpasscnt = 0
Rearfailcnt = 0
Iterations=argv[1]

def FrontCamera():
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 1 > camera.txt")
    print("Front Cam Opened...")
    sleep(5)
    
def RearCamera():
    os.system("adb wait-for-device shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0 > camera.txt")
    print("Rear Cam Opened...")
    sleep(5)
    
def Validate():
    os.system("adb shell dumpsys media.camera > cam.txt")
    fp=open("cam.txt","r")
    lines=fp.readlines()
    count=0
    for line in lines:
        s1="No active camera clients yet"
        if(s1 in line):
            count+=1
    if(count==1):
        print("Unable to launch Camera")
        return(False)
    else:
        print("Camera Preview")
        return(True)
    
for i in range(int(Iterations)):
    FrontCamera()
    if(Validate()):
        Frontpasscnt+=1
    else:
        Frontfailcnt+=1
    os.system("adb shell input keyevent 66")
    RearCamera()
    if(Validate()):
        Rearpasscnt+=1
    else:
        Rearfailcnt+=1
    os.system("adb shell input keyevent 66")
print("Front Camera==>Pass Count,Fail Count: ",Frontpasscnt,Frontfailcnt)
print("Rear Camera==>Pass Count,Fail Count: ",Rearpasscnt,Rearfailcnt)
