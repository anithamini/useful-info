import os
import sys
import time
import re
os.system("adb shell am start -a android.settings.SETTINGS")
os.system("adb shell input tap 430 300")
os.system("adb shell input keyeevnt 84")
os.system("adb shell input text Advanced")
os.system("adb shell input tap 500 1050")
os.system("adb shell input keyevent 20")
os.system("adb shell input keyevent 20")
os.system("adb shell input keyevent 66")
os.system("adb shell input tap 300 300")
os.system("adb shell input tap 425 440")
os.system("adb shell input keyevent 20")
os.system("adb shell input tap 500 470")
os.system("adb shell input tap 1020 175")
os.system("adb shell input text english")#here searching the language
os.system("adb shell input keyevent 20")# this event goes to down
os.system("adb shell input keyevent 66")#enter means select the language to add the language list
os.system("adb shell input keyevent 20")# to goes to down select the language
os.system("adb shell input tap 460 470")

