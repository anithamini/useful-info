import os
import sys
import time
import re
import unittest,time


print("----------------")
print("Wifi enable disable test started")
print("-----------------")
from sys import argv
Iterations = 2

def Killwhatsapp():
    os.system( "adb shell am force-stop com.whatsapp")

def Launchwhatsapp():
    os.system( "adb shell am start -n com.whatsapp/.Main")
def Whatsapp_searh():
     
    os.system( "adb shell input tap 190 30")
    os.system( "adb shell input text raushan")
    os.system( "adb shell input tap 260 150")
def Whatsapp_message():   
    os.system( "adb shell input text Message")
    os.system( "adb shell input tap 450 600")
    

Killwhatsapp()
Launchwhatsapp()
Whatsapp_search()
for n in range(int(Iterations)):
    Whatsapp_message()
    n+1
    
