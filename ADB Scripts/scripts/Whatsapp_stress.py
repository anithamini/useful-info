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
Iterations = argv[1] 

def Killwhatsapp():
    os.system( "adb shell am force-stop com.whatsapp")

def Launchwhatsapp():
    os.system( "adb shell am start -n com.whatsapp/.Main")
def Whatsapp_searchcontact():
    #coordinates to touch search 
    os.system( "adb shell input tap 600 90")
    os.system( "adb shell input text ram")
    #coordinates to touch 1st contact displayed after search 
    os.system( "adb shell input tap 350 250")
def Whatsapp_sendmessage():   
    os.system( "adb shell input text Message")
    os.system( "adb shell input tap 660 790")
    
# Killing whatsapp to make sure home screen is launched while launching
Killwhatsapp()
Launchwhatsapp()
Whatsapp_searchcontact()
for n in range(int(Iterations)):
    Whatsapp_sendmessage()
    n+1
    