                     #bt on or off during a call

import os
import re
import time
def check_btstate():
    os.system("adb shell dumpsys bluetooth_manager >btlog.txt")
    with open("btlog.txt","r")as fp:
        buff=fp.read()
    if(re.search('enabled: true',buff,re.I)):
        return(True)
    else:
        return(False)
def check_btconnectedstate():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings")
    os.system("adb shell input tap 411 508")
    time.sleep(10)
    os.system("adb shell dumpsys bluetooth_manager >bt.txt")
    with open("bt.txt","r")as fs:
        buffer=fs.read()
    if(re.search('subbu',buffer,re.I)):
        print("connected to the paired device")       
    else:
        print("not connected to the paired device")
    check_callstate()
    time.sleep(5)
    change_btmode()        
def change_btmode():
     os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings")
     os.system("adb shell input keyevent 20")
     os.system("adb shell input keyevent 66")
def check_callstate():
    os.system( "adb shell dumpsys telephony.registry > mCallState.txt")
    time.sleep(5)
    with open("mCallState.txt","r+") as fh:
        lines=fh.read()
        string2="com.android.incallui"
        if(re.search(string2,lines,0)):
            print("Call already connected and in progress irrespective of bt behaviour...\n")
        else:
            print("call not connected....")
#make a call
os.system("adb shell am start -a android.intent.action.CALL -d tel:+919640281782")
time.sleep(10)
os.system("adb shell input keyevent 3")
state=check_btstate()
if(state==0):
    change_btmode()
check_btconnectedstate()
print("Ending the call \n")
os.system("adb shell input keyevent KEYCODE_ENDCALL")
