import os
import sys
import time
import re

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
def mobiledata_off():
    os.system("adb shell svc data disable")
    time.sleep(1)
def checkmobiledata():
    os.system("adb shell getprop>mobiledata.txt")
    fp=open("mobiledata.txt","r+")
    buff=fp.read()
    str1="[gsm.defaultpdpcontext.active]: [true]"
    if str1 in buff:
        print str1
        return 1
    else:
        return 0
# below one foryoutube and playing video

def killyoutube():
    os.system("adb shell am force-stop com.google.android.youtube")
    print "youtube killed"
    
def launch_youtube():
    os.system("adb shell am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity")
    return(True)
    return(False)

def searchvideo():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text hawahawa")
    os.system("adb shell input keyevent 66")
    time.sleep(20)
    os.system("adb shell input tap 550 350")
    #os.system("adb shell input keyevent 20")
    #os.system("adb shell input keyevent 66")
    print "video is playing"
    
def offlinevideos():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text Nachange")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 650 360")
    print "video is palying"
    
def checkyoutubeplaying():
    os.system("adb shell dumpsys audio>youtube_log.txt")
    you_log=open("youtube_log.txt","r+")
    buff=you_log.read()
    #print buff
    enable=re.search("com.google.android.youtube",buff,re.I)
    if enable:
        return(True)
    else:
        return(False)


#below one for launch youtube and playing video using mobiledata
res=sim_test()
if res:
    print "sim is present"
    switch_mobiledata()
    pre=checkmobiledata()
    if pre:
        print "mobile data on"
        time.sleep(10)
        killyoutube()
        result=launch_youtube()
        time.sleep(5)
        if result:
            print "youtube launched"
            searchvideo()
            time.sleep(5)
            check=checkyoutubeplaying()
            if check:
                print("video is playing")
                time.sleep(20)
            else:
                print("video is not playing")
            #time.sleep(20)
        else:
            print "youtube not launched"

        killyoutube()
        pre=mobiledata_off()
        if not pre:
            print "mobile data off"
        else:
            print "mobile data on"
    else:
        print "mobile data off"
#below one for if mobile data off 
    launch_youtube()
    time.sleep(5)

    if result:
        print "youtube launched"
        offlinevideos()
        time.sleep(5)
        check=checkyoutubeplaying()
        if check:
            print("video is playing")
            time.sleep(10)
        else:
            print("video is not playing")
        killyoutube()
    else:
        print "youtube not launched"
            
    
else:
    print "sim not present"

