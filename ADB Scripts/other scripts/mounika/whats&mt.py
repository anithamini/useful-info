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

def search_contact():
    os.system("adb shell input tap 620 1215 ")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text amani@innominds")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input tap 570 370")
    
def send_msg():
    os.system("adb shell input text hello ")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 4")
    
def whats_call():
    os.system("adb shell input tap 920 180")
    time.sleep(20)
    #below one for while ringing the phone
    os.system("adb shell dumpsys telephony.registry >tele_logr.txt")
    fp=open("tele_logr.txt","r+")
    buff=fp.read()
    res=re.search("mCallState=1",buff,re.I)
    if res:
        return True
    else:
        return False
    
def mtcall_receive():
    print "below tap for receiving the call"
    os.system("adb shell input keyevent 5")
    time.sleep(2)
    os.system("adb shell dumpsys telephony.registry>tele_log.txt")
    fp=open("tele_log.txt","r+")
    buff=fp.read()
    res=re.search("mCallState=2",buff,re.I)
    if res:
        return True
    else:
        return False
    
def end_mtcall():
    os.system("adb shell input keyevent 6")
    print "call ended"

    
killwhatsapp()

launchwhatsapp()

search_contact()

send_msg()

time.sleep(2)

ena=whats_call()
print ena
if ena:
    print "phone is ringing we need to receive call"
    res=mtcall_receive()
    if res:
        print "call received and whatsapp call closed"
        time.sleep(5)
        end_mtcall()
    else:
        print "call not received" 
    
    
killwhatsapp()



