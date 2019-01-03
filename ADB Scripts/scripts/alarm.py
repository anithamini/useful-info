import os
from time import sleep
print("=======================================================================")
print("Alaram enable disable test started")
print("=======================================================================")
def kill_alaram():
    os.system("adb shell am force-stop com.google.android.deskclock")
def Checkalarmstate():
    os.system( "adb shell dumpsys alarm > aaaa.txt")
    with open("aaaa.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1="18:00:00"
            if(s1 in line):
                return(True)
        return(False)
def Launch_alarm():
    os.system("adb shell am start -n com.google.android.deskclock/com.android.deskclock.DeskClock")
def f1():
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 67")
    os.system("adb shell input keyevent 67")
    
def Create_alarm():
    os.system("adb shell input tap 375 1250")
    for i in range(0,2):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    f1()
    os.system("adb shell input text 18")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 22")
    f1()
    os.system("adb shell input text 00")
    os.system("adb shell input tap 557 915")
         
kill_alaram()
Launch_alarm()
Create_alarm()
print("Alarm is ON")
while(Checkalarmstate()):
    pass
print("Alarm is ringing")
os.system("adb shell input keyevent 3")
os.system("adb shell input touchscreen swipe 363 917 635 914")

