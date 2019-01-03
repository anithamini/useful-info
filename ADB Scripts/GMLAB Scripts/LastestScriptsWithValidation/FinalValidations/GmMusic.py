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

print("---------------GM Music Applications-----------")

def KillGmMusic():
    os.system("adb shell am force-stop com.generalmobile.app.musicplayer")


def LaunchGmMusic():
    os.system("adb shell monkey -p com.generalmobile.app.musicplayer -c android.intent.category.LAUNCHER  1")
    sleep(3)

def Validate(s1,s2):
        os.system("adb shell dumpsys "+s2+" > gmmusic.txt")
        with open("gmmusic.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if(s1 in buf):
                                return(True)
                       
def Play():
    os.system("adb shell input tap 536 1290")
    sleep(5)

def Pause():
    os.system("adb shell input keyevent 85")
    sleep(2)
    
for i in range(int(iterations)):
    KillGmMusic()
    LaunchGmMusic()
    if(Validate("packageName=com.generalmobile.app.musicplayer processName=com.generalmobile.app.musicplayer","activity")):
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
KillGmMusic()

print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
print("Play Pass Count=",PlayPassCnt,",PlayFail Count=",PlayFailCnt)
print("Pause Pass Count=",PausePassCnt,",Pause Fail Count=",PauseFailCnt)
