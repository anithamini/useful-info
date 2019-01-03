import os
import sys
import time
import re
import unittest
i=0
print("trying to launch facebook")

def launch_fb():
    os.system("adb shell am start -n com.facebook.katana/.LoginActivity")
    print("launched successfully")
    
def get_id():
    os.system("adb shell input tap 400 970")
    time.sleep(2)
    print("taking user id as email")
    os.system("adb shell input text diptendala007@gmail.com")

def get_password():
    os.system("adb shell input tap 1020 1840")
    time.sleep(2)
    print("taking password")
    os.system("adb shell input text dip@sasmal")
    
def fb_login():
    os.system("adb shell input tap 500 900")
    print("logged in successfully")
    
launch_fb()
time.sleep(4)
get_id()
get_password()
fb_login()
time.sleep(10)

while (i<40):
    os.system("adb shell input touchscreen swipe 500 1700 500 1200")
    print("scrolling down successfully for iteration",i)
    i+=1

