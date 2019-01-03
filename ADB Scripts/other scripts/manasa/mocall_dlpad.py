import os
import sys
import time
import re
import unittest,time

def launch_contacts():
    print(".......Opening Contacts......")
    os.system("adb shell input keyevent KEYCODE_CALL")

def connect_call():
    os.system("adb shell input text 9966292291")
    #os.system("adb shell input keyevent KEYCODE_DEL")
    os.system("adb shell input keyevent KEYCODE_ENTER")
    os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
    os.system("adb shell input keyevent KEYCODE_ENTER")
    time.sleep(10)
    print(".....ending the MOcall......")
    os.system("adb shell input keyevent KEYCODE_ENDCALL")
    time.sleep(10)
    os.system("adb shell input keyevent KEYCODE_ENTER")
    
def end_contacts():
    os.system("adb shell am force-stop com.android.contacts")

def checkconnect_call():
    os.system("adb shell dumpsys telephony.registry > gsm1.txt")
    with open("gsm1.txt","r+") as fp:
        lines=fp.readlines()
        for buf in lines:
            string1="mCallState=2"
            if string1 in buf:
                print("Call already connected and in progress...\n")
                print("Ending the call \n")
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                time.sleep(10)
                os.system("adb shell input keyevent KEYCODE_ENTER")
                
                
checkconnect_call()
end_contacts()
launch_contacts()
connect_call()
end_contacts()
    
    
