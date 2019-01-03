pass_cnt=0
fail_cnt=0
import os
from time import sleep
def validate():
    os.system( "adb shell dumpsys activity > game.txt")
    with open("game.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1="packageName=com.imangi.templerun processName=com.imangi.templerun"
            if(s1 in line):
                return(True)
        return(False)

def LaunchYoutube():
    os.system("adb shell monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1")
    sleep(5)
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text Songs")
    os.system("adb shell input keyevent 66")
    sleep(5)
    os.system("adb shell input tap 740 363")
    for i in range(0,2):
        sleep(5)
        os.system("adb shell input keyevent 85")
        
def KillYoutube():
    os.system("adb shell am force-stop com.google.android.youtube")

KillYoutube()
LaunchYoutube()
if(validate()):
        pass_cnt+=1
else:
        fail_cnt+=1
KillYoutube()
print("pass_cnt:",pass_cnt)
print("fail_cnt",fail_cnt)

com.android.server.audio.PlaybackActivityMonitor
