import os
import sys
from time import sleep
iterations=2#sys.arv[1]
LaunchPassCnt=0
LaunchFailCnt=0
EventPassCnt=0
EventFailCnt=0
def launch_Calendar():
    os.system("adb shell monkey -p com.google.android.calendar -c android.intent.category.LAUNCHER 1")

def kill_Calendar():
        os.system("adb shell am force-stop com.google.android.calendar")

def Validate(s1):
        os.system("adb shell dumpsys activity > calendar.txt")
        with open("calendar.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if(s1 in buf):
                                return(True)
                       
                return(False)     

def Create_Event():
    os.system("adb shell input tap 935 1878")
    os.system("adb shell input tap 951 1890")
    sleep(2)
    os.system("adb shell input text TestingEvent")
    sleep(3)
    os.system("adb shell input tap 987 1963")
    sleep(2)
    os.system("adb shell input tap 1010 161")


kill_Calendar()
for i in range(int(iterations)):
    sleep(4)
    launch_Calendar()
    if(Validate("packageName=com.google.android.calendar processName=com.google.android.calendar")):
            LaunchPassCnt+=1
    else:
            LaunchFailCnt+=1
    Create_Event()
    if(Validate("Waiting to send non-key event")):
            EventPassCnt+=1
    else:
            EventFailCnt+=1
print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
print("Event Pass Count=",EventPassCnt,",EventFail Count=",EventFailCnt)


