
"""
import os
import sys
import time
import re
#for launching the settings app
global buffer
os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.Settings")
os.system("adb shell input tap 300 260")
os.system("adb shell input text Bluetooth")
time.sleep(4)

#checking the bluetooth state
def Checkbtstate():
    print("in checkbtstate function")
    os.system( "adb shell dumpsys bluetooth_manager > Bt.txt")
    bt = open("Bt.txt","r")
    buffer = bt.read();
    #print(buffer)
    bt.close()
   
    Enable = re.search('enabled: true', buffer, re.I)
    if Enable:
        return(True)
    else:
        return(False)

os.system("adb shell input tap 300 300")
if Checkbtstate():
    print("bluetooth is enabled")
else:
    print("bluetooth is disabled")

for i in range(4):
    os.system("adb shell input keyevent 4")
time.sleep(1)
#checking the wifi state ------------------------------------------------
def Checkwifistate():
    print("in checkwifistate function")
    os.system( "adb shell dumpsys wifi > wifi.txt")
    wf = open("wifi.txt","r")
    buffer = wf.read();

    wf.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)
def WifiConnectedstate():
    print("in wifi connected func")
    os.system( "adb shell dumpsys wifi > wifi.txt")
    wf = open("wifi.txt","r")
    buffer = wf.read();

    wf.close()
   
    Enabled = re.search('curState=CompletedState', buffer, re.I)
    
    if Enabled:
        return(True)
    else:
        return(False)
def name():
    wf=open("wifi.txt","r")
    buffer=wf.read()
    wf.close()
    Enabled = re.search('ssid=[a-z]',buffer,re.I)
    print(Enabled)

    
os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.Settings")
os.system("adb shell input tap 300 260")
os.system("adb shell input text Wi-Fi")
time.sleep(4)


if Checkwifistate():
    print("wifi is enabled")
    if WifiConnectedstate():
        print("wifi is connected to some network")
        print("ssid=")
        name()
    else:
        print("wifi is enabled,but not connected to any network")
    
else :
    print("wifi is disabled")

os.system("adb shell input tap 300 300")

for i in range(4):
    os.system("adb shell input keyevent 4")
"""

"""

#for playing music and video
    

import os
import sys
import time
import re
import unittest,time

from sys import argv
Iterations = 1

def Killmusic():
    os.system( "adb shell am force-stop com.google.android.music")

def Launchmusic():
    os.system( "adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/SHAREit/audios/0_DARLING/darling-1hoshare.mp3 -t audio/mp3")
    os.system("adb shell input tap 220 1408")
    time.sleep(5)
    os.system("aadb shell input keyevent 121")
    os.system("adb shell dumpsys audio > aud.txt")
def launchvedio():
    os.system("adb shell am start -a android.intent.action.VIEW -d file:///mnt/sdcard/Nenlocal.mp4 -t video/mp4")
    os.system("adb shell dumpsys media.player > ved.txt")
    os.system("adb shell input tap 315 907")
Killmusic()
Launchmusic()
Killmusic()
#launchvedio()
"""


#mo_call and mt_call



import os
import time
import sys
import re

def mo_call_test():
    os.system("adb shell getprop> gsm.txt ")
    time.sleep(3)
    fh=open("gsm.txt","r") 
    lines=fh.read()
    #print(lines)
 
    fh.close()   
    e1=re.match("[DEVICE_PROVISIONED]: [1]",lines)
    print(e1)
    e2=re.search("[gsm.sim.state]: [READY,NOT_READY]",lines)
    print(e2)
    e3=re.search("[gsm.sim.state]: [NOT_READY,READY]",lines,re.I)
    e4=re.search("[gsm.sim.state]: [ABSENT,READY]",lines,re.I)
    e5=re.search("[gsm.sim.state]: [READY,ABSENT]",lines,re.I)
    print(e5)
    if(e1 or e2 or e3 or e4 or e5):
        print("sim prsent,proceed the test")
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
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9704708710")
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



print("in main")
mo_call_test()











    
