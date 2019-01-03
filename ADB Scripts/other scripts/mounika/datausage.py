import os
import sys
import time
import re
#To verify that user is able to Swicth on data usage and use it

def sim_test():
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
                return 1
        else:
                print("sim not present, please insert the sim and start the test")
                return 0


def switch_mobiledata():
    os.system("adb shell svc data enable")
    time.sleep(3)
    os.system("adb shell getprop>mobiledata.txt")
    fp=open("mobiledata.txt","r+")
    buff=fp.read()
    str1="[gsm.defaultpdpcontext.active]: [true]"
    if str1 in buff:
        print str1
        return 1
    else:
        return 0

def mobiledata_off():
    os.system("adb shell svc data disable")
    time.sleep(3)
    os.system("adb shell getprop>mobiledata.txt")
    fp=open("mobiledata.txt","r+")
    buff=fp.read()
    str1="[gsm.defaultpdpcontext.active]: [false]"
    if str1 in buff:
        print str1
        return 1
    else:
        return 0
    
# below one for using chrome to download image using data and wifi
def kill_chrome():
    os.system("adb shell am force-stop com.android.chrome")
  

def launch_google():
    os.system("adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main")

def browse_chrome():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text cutebabies")
    os.system("adb shell input keyevent 66")

def download_image():
    # below one for searching paricular website for download image
    i=0
    while(i<16):
        os.system("adb shell input keyevent 20")
        i=i+1
    
    #os.system("adb shell input tap 500 1778")
    time.sleep(5)
    #below one for selctt image and download
    os.system("adb shell input tap 430 1469")
    os.system("adb shell input swipe 520 780 520 780 2000")
    os.system("adb shell input tap 430 1469")
    os.system("adb shell input tap 815 1966")
    print "image downloaded"
    


    
#sim present or not checking      
pre=sim_test()
print pre
if pre:
    print "sim is present now you can able to switch to data"
    #mobiledata checking and test mobile data on or not
    res=switch_mobiledata()
    if res:
        print "mobile data on now you can able to browse"
        kill_chrome()
        print "chrome killed"
        launch_google()
        print "chrome is launched"
        time.sleep(2)
        browse_chrome()
        time.sleep(20)
        #download_image()
        kill_chrome()
    else:
        print "mobile data off your in offline"
else:
    print "sim not present"

#checking mobile data on or off
res=mobiledata_off()
if  res:
    print("mobile data off")
else:
    print("mobile data on")






