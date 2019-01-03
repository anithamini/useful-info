import os
import sys
import time

os.system("adb shell am start -a android.intent.action.CALL -d tel:+919640281782")
time.sleep(15)
os.system("adb shell input keyevent 6")














"""
os.system("adb shell input keyevent 5")
os.system("adb shell input tap 203 942")
os.system("adb shell input tap 155 205")
os.system("adb shell input text Hemalatha")
os.system("adb shell input tap 358 311")
os.system("adb shell input tap 317 916")
time.sleep(10)
os.system("adb shell input keyevent 6")
time.sleep(10)
os.system("adb shell input keyevent 4")
time.sleep(10)
os.system("adb shell input keyevent 4")


"""
