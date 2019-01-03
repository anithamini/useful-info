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

def mo_call_test():
    print ("music is paused")
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="[gsm.sim.state]: [READY,READY]"
            string2 = "[gsm.sim.state]: [READY,NOT_READY]"
            string3 = "[gsm.sim.state]: [NOT_READY,READY]"
            string4 = "[gsm.sim.state]: [ABSENT,READY]"
            string5 = "[gsm.sim.state]: [READY,ABSENT]"
            if (string1 in line or string2 in line or string3 in line or string4 in line or string5 in line):
                print("Sim present, so procedding the test")
                break
        else:
            print("sim not present, please insert the sim and start the test")
    os.system("adb wait-for-device shell input keyevent 82")
    os.system("adb wait-for-device shell input keyevent 3")
    os.system( "adb shell dumpsys telephony.registry > mCallState.txt")
    time.sleep(5)
    with open("mCallState.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="mCallState=2"
            if(string1 in line):
                print("Call already connected and in progress...\n")
                print("Ending the call \n")
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                break
    print("Connecting the call to MT_num...\n")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:8919366256")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    time.sleep(10)
    os.system("adb shell dumpsys telephony.registry > mCallState1.txt")
    time.sleep(5)
    with open("mCallState1.txt", "r+") as fh:
        lines = fh.readlines()
        for line in lines:
            # print(line)
            #print("checking for call status")
            string2 = "mCallState=2"
            if (string2 in line):
                print("Call successfully connected and in progress...\n")
                print("Ending the call \n")
                time.sleep(5)
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                print("Call successfully disconnected ...\n")
                test=1
                #break
                return 1
        else:
            print("Unable to connect the call, so test case is failed")
            return 0
    


def Launchmusic():
    os.system( "adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Music/Sega/Merupunu.mp3 -t audio/mp3")
    os.system("adb shell dumpsys audio > aud.txt")
    print("music is playing")
    time.sleep(20)
    mo_call_test()
    print ("music is resumed")

    

    

Killmusic()
Launchmusic()
time.sleep(5)
Killmusic()

