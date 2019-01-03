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
Iterations = 2 

def Killwhatsapp():
    os.system( "adb shell am force-stop com.whatsapp")

def Launchwhatsapp():
    os.system( "adb shell am start -n com.whatsapp/.Main")
def Whatsapp_searchcontact():
    #coordinates to touch search 
    os.system( "adb shell input tap 60 90")
    os.system( "adb shell input text Yoga@")
    ##coordinates to touch 1st contact displayed after search 
    os.system( "adb shell input tap 363 502")
    os.system( "adb shell input tap 266 1212")
def Whatsapp_sendmessage():   
    os.system( "adb shell input text Hello")
    os.system( "adb shell input tap 1010 1213")
  
    #os.system( "adb shell input tap 1030 147")
    #os.system( "adb shell input tap 666 315")
    #os.system( "adb shell input tap 336 1877")
    #os.system( "adb shell input tap 1010 1213")
  #  for n in range(4):
    #    os.system( "adb shell input keyevent 4")
 
# Killing whatsapp to make sure home screen is launched while launching
Killwhatsapp()
Launchwhatsapp()
Whatsapp_searchcontact()
for n in range(int(Iterations)):
    Whatsapp_sendmessage()
    n+1
os.system( "adb shell input keyevent 3")   
    
 
