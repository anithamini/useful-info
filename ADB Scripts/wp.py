import os
import sys
import time
import re
import unittest,time

#Before running scripts make sure whatsapp is installed and has a contact with name mentioned in config file
print("=======================================================================")
print("Wifi enable disable test started")
print("=======================================================================")
from sys import argv
Iterations = 1

def Killwhatsapp():
    os.system( "adb shell am force-stop com.whatsapp")

def Launchwhatsapp():
    os.system( "adb shell am start -n com.whatsapp/.Main")
def Whatsapp_searchcontact():
    #coordinates to touch search
    #os.system( "adb shell input tap 603 95")
    os.system( "adb shell input keyevent 84")
    os.system( "adb shell input text Subha")
    #coordinates to touch 1st contact displayed after search 
    os.system( "adb shell input tap 187 318")
    
def Whatsapp_sendmessage():   
    os.system( "adb shell input text hii")
    os.system( "adb shell input keyevent 22")
    os.system( "adb shell input keyevent 22")
    os.system( "adb shell input keyevent 66")
    os.system( "adb shell input keyevent 111")
    #os.system( "adb shell input tap 660 718")
def Whatsapp_forward():
    os.system("adb shell input touchscreen swipe 558 1008 558 1008 1000")
    os.system( "adb shell input tap 658 133")
    os.system( "adb shell input keyevent 84")
    os.system( "adb shell input text Manasa")
    os.system( "adb shell input tap 163 312")
    os.system( "adb shell input tap 613 675")
#def Whatsapp_multifrwrd():
    
# Killing whatsapp to make sure home screen is launched while launching
Killwhatsapp()
Launchwhatsapp()
Whatsapp_searchcontact()
for n in range(int(Iterations)):
    Whatsapp_sendmessage()
    n+1
Whatsapp_forward()
# Whatsapp_multifrwrd()
