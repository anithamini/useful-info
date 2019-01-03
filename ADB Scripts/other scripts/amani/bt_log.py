import os
import sys
import time
import re
import unittest,time


print("=======================================================================")
print("Bluetooth enable disable test started")
print("=======================================================================")
from sys import argv
Iterations = 3#argv[1] 

pass_TC_count = 0
fail_TC_count = 0
print("Iterations:",Iterations)
def Checkbtstate():
    os.system( "adb shell dumpsys bluetooth_manager > bt_log.txt")
    bt_log = open("bt_log.txt","r+")
    buffer = bt_log.readline();
    buffer = bt_log.readline();
    bt_log.close()
    enabled = re.search('enabled: true', buffer, re.I)
    print enabled
    if enabled:
        return(True)
    else:
        return(False)

def CheckbtConnectedstate():
    os.system("adb shell input tap 342 671")
    time.sleep(20)
    os.system( "adb shell dumpsys bluetooth_manager > bt_log.txt")
    with open("bt_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1=" mPhoneState: com.android.bluetooth.hfp.HeadsetPhoneState@8796769"
            if(string1 in line):
                #print("connected")
                return(True)

def Toggle_bt():
    os.system("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")
    os.system("adb shell input tap 667 203")
    #os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings")
    #os.system("adb shell input tap 662 207")
    #os.system("adb shell input  23")
    #time.sleep(5)
#Turn OFF wifi before starting testcases
#checking for wifi state
state = Checkbtstate()
print(state)
if state:
    Toggle_bt()
    
for n in range(int(Iterations)):
    Toggle_bt()
    time.sleep(10)
    Connectedstate = CheckbtConnectedstate()
    if Connectedstate:
        print("Connected to paired device successfully for iteration:", n)
        pass_TC_count = pass_TC_count+1
    else:
        print("Not connected to paired device  for iteration:", n)
        fail_TC_count = fail_TC_count+1
    Toggle_bt()
print("Bluetooth preset connection Passed:",pass_TC_count )
print("Bluetooth preset connection Failed:",fail_TC_count )
