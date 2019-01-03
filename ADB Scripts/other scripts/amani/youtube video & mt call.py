import os
import sys
import re
import time
"""playing video status"""
def checkyoutubeplaying():
    os.system("adb shell dumpsys audio>youtube_log.txt")
    you_log=open("youtube_log.txt","r+")
    buff=you_log.read()
    #print buff
    enable=re.search("com.google.android.youtube",buff,re.I)
    print enable
    if enable:
        return(True)
    else:
        return(False)


def checkdatastate():
    os.system("adb shell dumpsys telephony.registry>data_log.txt")
    wifi_log=open("data_log.txt","r+")
    buffer=wifi_log.read();
    wifi_log.close()
    enabled=re.search('mDataConnectionPossible=true',buffer,re.I)
    if enabled:
        return(True)
    else:
        return(False)

def killyoutube():
    os.system("adb shell am force-stop com.google.android.youtube")
    print "youtube killed"
    
def launchyoutube():
    os.system("adb shell am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity")
    return(True)

def searchvideo():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text hawahawa")
    os.system("adb shell input keyevent 66")
    time.sleep(10)
    os.system("adb shell input tap 550 350")
    print "video is playing"

def offlinevideos():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text Nachange")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 650 360")
    print "video is palying"
    
def auto_answer():
    os.system("adb shell am start -n com.android.phone/com.yulong.settings.CallAutoAnswer")
    os.system("adb shell input tap 641 217")
    os.system("adb shell input keyevent 4")
    
def end_mtcall():
    os.system("adb shell input keyevent 6")
    print ("video is resumed")



#driver program
#killing youtube
killyoutube()

#checking wifi status 
state=checkdatastate()
print state
if state:
    print "data connected"
    auto_answer()
    launch=launchyoutube()
    time.sleep(2)
    if launch:
        print "youtube launched"
        time.sleep(2)
        #searching the video for palying
        searchvideo()
        time.sleep(5)
        check=checkyoutubeplaying()
        if check:
            print("video is playing")
            time.sleep(30)
            os.system("adb shell dumpsys telephony.registry >mtcall.txt")
            with open("mtcall.txt","r+") as fp:
                lines=fp.readlines()
                for line in lines:
                    #print(line)
                    string1="mCallState=2"
                    if(string1 in line):
                        print("video is paused")
                        time.sleep(10)
                        end_mtcall()           
        else:
            print("video is not playing")
       
    else:
        print "youtube not launched"
    auto_answer()   
else:
    launch=launchyoutube()
    if launch:
        print "youtube launched"
    print "you are in offline"
    offlinevideos()
    
    check=checkyoutubeplaying()
    if check:
        print("video is playing")
    else:
        print("video is not playing")
time.sleep(3)    
killyoutube()
