import os
import time
import sys
import re

# audio testing
def audio_app_launch():
    os.system("adb shell am start -n com.miui.player/com.miui.player.ui.MusicBrowserActivity")
def audio_ogg():
    os.system("adb shell input tap 1000 150")
    time.sleep(1)
    os.system("adb shell input text .ogg")
    time.sleep(1)
    os.system("adb shell input tap 500 270")
def mp3song():
    os.system("adb shell input tap 1000 150")
    time.sleep(1)
    os.system("adb shell input text .mp3")
    time.sleep(1)
    os.system("adb shell input tap 500 270")
def stop_music():
    for i in range(2):
        os.system("adb shell input keyevent 4")
    os.system("adb shell input tap 650 1890")
def check_play():
    os.system("adb shell dumpsys audio >ad.txt")
    time.sleep(2)
    fp=open("ad.txt","r")
    time.sleep(1)
    buffer=fp.read()
    time.sleep(1)
    fp.close()
    r=re.search("com.miui.player",buffer)
    if r:
        return True
    else:
        return False
audio_app_launch()
assogg=0
afogg=0
assmp3=0
afmp3=0
for i in range(10):
    time.sleep(1)
    audio_ogg()
    time.sleep(3)
    if check_play():
        assogg+=1
        stop_music()
    else:
        afogg+=1
    time.sleep(1)
    mp3song()
    time.sleep(3)
    if check_play():
        assmp3+=1
        stop_music()
    else:
        afmp3+=1
           
os.system("adb shell input keyevent 3")
time.sleep(2)
print("video testing")
#checking the different formats of video
def video_app_launch():
    os.system("adb shell am start -n com.mxtech.videoplayer.ad/com.mxtech.videoplayer.ad.ActivityMediaList")
    
def video_v_3gp():
    os.system("adb shell input tap 900 150")
    time.sleep(1)
    os.system("adb shell input text v.3gp")
    time.sleep(1)
    os.system("Adb shell input tap 500 300")
    os.system("Adb shell input tap 500 300")

def video_play():
    os.system("adb shell dumpsys audio >vd.txt")
    time.sleep(1)
    vf=open("vd.txt","r")
    buf=vf.read()
    time.sleep(1)
    vf.close()
    #r=re.search("com.google.android.music",buf,re.I)
    r1=re.search("com.mxtech.videoplayer.ad",buf,re.I)
    #print(r)
    print(r1)
    if (r1):
        return (True)
    else:
        return (False)

def video_v_mp4():
    os.system("adb shell input tap 900 150")
    time.sleep(1)
    os.system("adb shell input text v.mp4")
    time.sleep(1)
    os.system("Adb shell input tap 500 300")
    os.system("Adb shell input tap 500 300")

video_app_launch()
time.sleep(1)
#video_v_ogg()
vs3gp=0
vf3gp=0
vsmp4=0
vfmp4=0
for j in range(10):
    video_v_3gp()
    time.sleep(1)
    if video_play():
        vs3gp+=1
        os.system("adb shell input keyevent 4")
        os.system("adb shell input keyevent 4")
    else:
        vf3gp+=1
       
    video_v_mp4()
    time.sleep(1)
    if video_play():
        vsmp4+=1
        os.system("adb shell input keyevent 4")
        os.system("adb shell input keyevent 4")
    else:
        vfmp4+=1
print("the audio reports are:")
print("assogg=",assogg)
print("afogg=",afogg)
print("assmp3=",assmp3)
print("afmp3=",afmp3)
print("the video reports are:")
print("vs3gp=",vs3gp)
print("vf3gp=",vf3gp)
print("vsmp4=",vsmp4)
print("vfmp4=",vfmp4)
