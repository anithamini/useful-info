import os
import time
from sys import argv
passcnt=0
failcnt=0
Iterations=argv[1]
def LaunchMXPlayer():
    os.system("adb shell monkey -p com.mxtech.videoplayer.ad -c android.intent.category.LAUNCHER  1")
    time.sleep(5)
    
def KillMXPlayer():
    os.system("adb shell am force-stop com.mxtech.videoplayer.ad")
    
def PlayVideo():
    os.system("adb shell input tap 570 470")
    os.system("adb shell input tap 486 619")
    os.system("adb shell input tap 570 1349")
    for i in range(2):
        time.sleep(5)
        os.system("adb shell input keyevent 85")
            
for i in range(int(Iterations)):
    KillMXPlayer()
    LaunchMXPlayer()
    PlayVideo()
    time.sleep(5)
KillMXPlayer()
    
print("Pass Count,Fail Count: ",passcnt,failcnt)

#os.system("adb shell dumpsys media.player > audio.txt")
