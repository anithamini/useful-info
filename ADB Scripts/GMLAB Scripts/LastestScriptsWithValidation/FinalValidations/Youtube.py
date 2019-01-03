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
print("-----------------youtube-----------------")

def LaunchYoutube():
    os.system("adb shell monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1")
    sleep(5)
    
def Play():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text dhee%s10")
    for i in range(0,2):
        os.system("adb shell input keyevent 66")
        sleep(5)
        
def Pause():
    os.system("adb shell input keyevent 85")
    sleep(5)
"""
    for i in range(0,2):
        os.system("adb shell input tap 567 380")

"""    
def Validate(s1,s2):
        os.system("adb shell dumpsys "+s2+" > gmmusic.txt")
        with open("gmmusic.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if(s1 in buf):
                                return(True)
                        
def KillYoutube():
    os.system("adb shell am force-stop com.google.android.youtube")

for i in range(int(iterations)):
    KillYoutube()
    LaunchYoutube()
    if(Validate("packageName=com.google.android.youtube processName=com.google.android.youtube","activity")):
            LaunchPassCnt+=1
    else:
            LaunchFailCnt+=1
    Play()
    sleep(5)
    if(Validate("state:started -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x200 tags= bundle=null","audio")):
            PlayPassCnt+=1
    else:
            PlayFailCnt+=1
    Pause()
    if(Validate("state:paused -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x200 tags= bundle=null","audio")):
            PausePassCnt+=1
    else:
            PauseFailCnt+=1
    sleep(2)
KillYoutube()

print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
print("Play Pass Count=",PlayPassCnt,",PlayFail Count=",PlayFailCnt)
print("Pause Pass Count=",PausePassCnt,",Pause Fail Count=",PauseFailCnt)






