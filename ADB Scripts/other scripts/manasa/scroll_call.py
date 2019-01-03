import os
import sys
import time
import re
import unittest,time


def launch_contacts():
    print(".......Opening Contacts......")
    os.system("adb shell input keyevent KEYCODE_CALL")
    #os.system("adb shell input keyevent KEYCODE_DPAD_RIGHT")


def scroll_check():
    print(".......Scrolling the contacts.....")
    print("....checking Scroll Down....")
    os.system("adb shell input swipe 702 184 677 1177")
    print("....checking Scroll Up.....")
    os.system("adb shell input swipe 702 1135 689 162")


def end_contacts():
    print("....Closing Contacts.....")
    os.system("adb shell am force-stop com.android.contacts")


launch_contacts()
scroll_check()
end_contacts()
    
    
