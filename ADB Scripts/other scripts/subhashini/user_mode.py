import os
import time
import unittest,time


def user_launch():
    os.system("adb shell am start -a android.settings.SETTINGS")
    os.system("adb shell input swipe 356 1000 349 144")
    os.system("adb shell input tap 433 232")
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
    
def kill_settings():
    os.system("adb shell am force-stop com.android.settings")
def create_user():
    os.system("adb shell input keyevent 23")
    for i in range(1,5):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")

def launch_guest():
    print(".....launching guest.....")
    os.system("adb shell input tap 433 232")
    os.system("adb shell input text Subhashini")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")


kill_settings()
user_launch()
create_user()
launch_guest()
time.sleep(5)
kill_settings()
