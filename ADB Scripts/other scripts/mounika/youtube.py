import os
import sys
import re
import time
"""playing video status"""
def checkyoutubeplaying():
    os.system("adb shell dumpsys audio>youtube_log.txt")
    you_log=open("youtube_log.txt","r+")
    buff=you_log.read()
    print buff
    enable=re.search("com.google.android.youtube",buff,re.I)
    if enable:
        return(True)
    else:
        return(False)


def checkwifistate():
    os.system("adb shell dumpsys wifi>wifi_log.txt")
    wifi_log=open("wifi_log.txt","r+")
    buffer=wifi_log.read();
    wifi_log.close()
    enabled=re.search('Wi-Fi is enabled',buffer,re.I)
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
    



#driver program
#killing youtube
killyoutube()

#checking wifi status 
state=checkwifistate()
print state
if state:
    print "wi-fi connected"
    launch=launchyoutube()
    if launch:
        print "youtube launched"
        time.sleep(2)
        #searching the video for palying
        searchvideo()
        check=checkyoutubeplaying()
        if check:
            print("video is playing")
        else:
            print("video is not playing")
       
    else:
        print "youtube not launched"
        
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
    

