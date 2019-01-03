import os
import sys
import time
import re
import unittest,time
print "hello moubnika"
print "wifi enable disable test started"
print "hhghghf"
from sys import argv
iterations=2
def killwhatsapp():
    os.system("adb shell am force-stop com.whatsapp")
    print "whatsapp killed"


def launchwhatsapp():
    os.system("adb shell am start -n com.whatsapp/.Main")

def whatsapp_searchcontact():
    #os.system("adb shell input keyevent 84")
    os.system("adb shell input tap 620 1215 ")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text mounika")
    os.system("adb shell input tap 360 405")
def whatsapp_sendmsg():
    os.system("adb shell input text hiiipotti")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    

killwhatsapp()
launchwhatsapp()
#time.sleep(3)
whatsapp_searchcontact()
for n in range(iterations):
    whatsapp_sendmsg()
    n=n+1
#killwhatsapp()
#launchwhatsapp()
os.system("adb shell input keyevent 4")
os.system("adb shell input keyevent 4")
os.system("adb shell input keyevent 84 ")
os.system("adb shell input text manasa@innominds")
os.system("adb shell input tap 350 482")
os.system("adb shell input touchscreen swipe 354 935 354 935 1000")
os.system("adb shell input tap 1000 185")
os.system("adb shell input keyevent 84")
os.system("adb shell input text manasa@innominds")
os.system("adb shell input tap 400 479")
#os.system("adb shell input keyevent KEYCODE_CLEAR")
#os.system("adb shell input keyevent 4")
os.system("adb shell input keyevent KEYCODE_ENTER")
#os.system("adb shell input keyevent 22")
#os.system("adb shell input keyevent 22")




