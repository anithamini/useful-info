import os
import sys
import time
import re

def kill_bt():
    os.system("adb shell am force-stop com.android.bluetooth")
def lanch_bt():
    #os.system("adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
    """os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input touchscreen swipe 516 1278 516 667")
    os.system("adb shell input touchscreen swipe 600 677 600 677 1000")"""
    os.system("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")
    os.system("adb shell input tap 667 203")
def search_bt():
    time.sleep(2)
    os.system("adb shell input tap 346 1230")
def pair_bt():
    os.system("adb shell input tap 316 853")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
def connect_bt():
    os.system("adb shell input tap 355 677")


kill_bt()
lanch_bt()
search_bt()
#pair_bt()
connect_bt()
