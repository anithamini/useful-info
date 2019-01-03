import os
import sys
import time

def kill_whatsapp():
    os.system("adb shell am force-stop com.whatsapp")
def lanch_whatsapp():
    os.system("adb shell am start -n com.whatsapp/.Main")
    time.sleep(3)
def search_whatsapp():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text sairam.innominds")
    os.system("adb shell input tap 270 350")
    time.sleep(2)
def send_whatsapp():
    os.system("adb shell input text gudmng")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input tap 990 1650")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input keyevent 4")
    #os.system("adb shell input keyevent 4")
def forward_whatsapp():
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text BEAUTIFUL")
    os.system("adb shell input tap 235 203")
    time.sleep(2)
    os.system("adb shell input keyevent 19")
    os.system("adb shell input touchscreen swipe 366 350 366 350 1000")
    os.system("adb shell input tap 694 108")
    os.system("adb shell input tap 405 111")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text sairam.innominds")
    os.system("adb shell input tap 295 315")
    os.system("adb shell input keyevent 28")
    os.system("adb shell input text batch")
    os.system("adb shell input tap 295 315")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input tap 638 1198")
    
    

kill_whatsapp()
lanch_whatsapp()
search_whatsapp()
send_whatsapp()
kill_whatsapp()
lanch_whatsapp()
forward_whatsapp()
