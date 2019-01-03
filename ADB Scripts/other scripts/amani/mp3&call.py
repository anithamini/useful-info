import os
import sys
import time
import re
import unittest,time

from sys import argv
Iterations = 1 #argv[1] 

def Killmusic():
    os.system( "adb shell am force-stop com.coolpad.music")
    print ("music is killed")

def auto_answer():
    os.system("adb shell am start -n com.android.phone/com.yulong.settings.CallAutoAnswer")
    os.system("adb shell input tap 641 217")
    os.system("adb shell input keyevent 4")
    
def end_mtcall():
    os.system("adb shell input tap 351 1178")
    print ("music is resumed")


def Launchmusic():
    os.system( "adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Music/Sega/Merupunu.mp3 -t audio/mp3")
    os.system("adb shell dumpsys audio > aud.txt")
    print("music is playing")
    auto_answer()
    time.sleep(30)
    os.system("adb shell dumpsys telephony.registry >mtcall.txt")
    with open("mtcall.txt","r+") as fp:
        lines=fp.readlines()
        for line in lines:
            #print(line)
            string1="mCallState=2"
            if(string1 in line):
                print("music is paused")
                time.sleep(10)
                end_mtcall()
    auto_answer()           
    

    

    

Killmusic()
Launchmusic()
time.sleep(5)
Killmusic()

