import os
import time
import sys
import re

def checkdatastate():
    os.system( "adb shell getprop > data_log.txt")
    data_log = open("data_log.txt","r+")
    with open("data_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="[gsm.defaultpdpcontext.active]: [true]"
            if(string1 in line):
                print("data enabled")
                return(True)
        else:
            print("data disabled")
            return(False)

def toggle_data():
    os.system("adb shell am start -n com.android.settings/.Settings")
    #time.sleep(2)
    os.system("adb shell input tap 650 550")
    os.system("adb shell input keyevent 4")

def kill_chrome():
    os.system("adb shell am force-stop com.android.chrome")
def launch_chrome():
    os.system("adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity")
def browse_websites(i):
    os.system("adb shell input tap 597 121")
    os.system("adb shell input tap 65 121")
    os.system("adb shell input keyevent 84")
    if i==0:
        os.system("adb shell input text www.indiabix.com")
        print("opening browser1...........")
    elif i==1:
        os.system("adb shell input text www.innominds.com")
        print("opening browser2...........")
    else:
        os.system("adb shell input text www.gmail.com")
        print("opening browser3...........")
    os.system("adb shell input keyevent 66")
    time.sleep(5)  
    
state = checkdatastate()
print(state)
if not state:
    print("data enabling....")
    toggle_data()
    time.sleep(5)
    state = checkdatastate()
kill_chrome()
launch_chrome()
for n in range(0,3):
    browse_websites(n)
    time.sleep(5)
kill_chrome()


    
