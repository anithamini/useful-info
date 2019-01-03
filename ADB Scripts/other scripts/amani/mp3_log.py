import os
import sys
import time
import re
import unittest,time

from sys import argv
Iterations = 1 #argv[1] 

def Killmusic():
    os.system( "adb shell am force-stop com.google.android.music")

def Launchmusic():
    os.system( "adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Music/druva/Choosa-choosa.mp3 -t audio/mp3")
    os.system("adb shell dumpsys audio > aud.txt")
def launchvedio():
    os.system("adb shell am start -a android.intent.action.VIEW -d file:/storage/emulated/0/video/Idiot.mp4 -t video/mp4")
    os.system("adb shell dumpsys media.player > ved.txt")
    time.sleep(5)
    os.system("adb shell input tap 635 677")
    os.system("adb shell input tap 635 677")
def killvideo():
    os.system( "adb shell am force-stop com.yulong.android.videoplayer")


Killmusic()
Launchmusic()
Killmusic()
launchvedio()
killvideo()
