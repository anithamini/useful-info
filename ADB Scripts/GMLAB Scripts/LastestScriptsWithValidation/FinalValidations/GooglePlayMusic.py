    
import os
import sys
from time import sleep
iterations=sys.argv[1]
LaunchPassCnt=0
LaunchFailCnt=0
PlayPassCnt=0
PlayFailCnt=0
PausePassCnt=0
PauseFailCnt=0

print("------------Google Play Music Application--------------")

def LaunchGooglePlayMusic():
    os.system("adb shell monkey -p com.google.android.music -c android.intent.category.LAUNCHER  1")
    sleep(3)

def Play():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    sleep(5)

def Pause():    
        os.system("adb shell input keyevent 85")
        sleep(5)
    
def Validate(s1,s2):
        os.system("adb shell dumpsys "+s2+" > googleplay.txt")
        with open("googleplay.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if(s1 in buf):
                                return(True)
                       
def KillGooglePlayMusic():
    os.system("adb shell am force-stop com.google.android.music")

for i in range(int(iterations)):
    KillGooglePlayMusic()
    LaunchGooglePlayMusic()
    if(Validate("packageName=com.google.android.packageinstaller processName=com.google.android.packageinstaller","activity")):
            LaunchPassCnt+=1
    else:
            LaunchFailCnt+=1
    Play()
    if(Validate("state:started -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
            PlayPassCnt+=1
    else:
            PlayFailCnt+=1
    Pause()
    if(Validate("state:paused -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
            PausePassCnt+=1
    else:
            PauseFailCnt+=1
    sleep(2)
KillGooglePlayMusic()
print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
print("Play Pass Count=",PlayPassCnt,",PlayFail Count=",PlayFailCnt)
print("Pause Pass Count=",PausePassCnt,",Pause Fail Count=",PauseFailCnt)


