import os
import sys
from time import sleep
iterations=1#sys.arv[1]
LaunchPassCnt=0
LaunchFailCnt=0
EventPassCnt=0
EventFailCnt=0
KillPassCnt=0
KillFailCnt=0

print("--------------Calendar---------------")

def launch_Calendar():
    os.system("adb shell monkey -p com.google.android.calendar -c android.intent.category.LAUNCHER 1")
    sleep(2)
def kill_Calendar():
        os.system("adb shell am force-stop com.google.android.calendar")
        sleep(4)
def Validate(s1,n):
    os.system( "adb shell dumpsys activity > calendar.txt")
    with open("calendar.txt","r+") as fh:
            buff=fh.read()
            if(n=="Calendar"):
                if(s1 in buff):
                    return(True)
                else:
                    return(False)
            if(n=="KillCalendar"):
                if(s1 in buff):
                    return(False)
                else:
                    return(True)

def Create_Event():
    os.system("adb shell input tap 935 1878")
    os.system("adb shell input tap 951 1890")
    sleep(2)
    os.system("adb shell input text TestingEvent")
    sleep(3)
    os.system("adb shell input tap 987 1963")
    sleep(2)
    os.system("adb shell input tap 1010 161")
    sleep(4)


for i in range(int(iterations)):
    kill_Calendar()
    sleep(5)
    res=Validate("packageName=com.google.android.calendar processName=com.google.android.calendar","KillCalendar")
    print("====",res)
    if(res):
        KillPassCnt+=1
    else:
        KillFailCnt+=1
    sleep(4)
    launch_Calendar()
    if(Validate("packageName=com.google.android.calendar processName=com.google.android.calendar","Calendar")):
            LaunchPassCnt+=1
    else:
            LaunchFailCnt+=1
   
kill_Calendar()
os.system( "adb shell dumpsys activity > calendar11.txt")
print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
print("Event Pass Count=",EventPassCnt,",EventFail Count=",EventFailCnt)
print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)

"""
 Create_Event()
    if(Validate("com.google.android.calendar.APPWIDGET_CALLER_IS_SYNCADAPTER","Calendar")):
            EventPassCnt+=1
    else:
            EventFailCnt+=1

"""
