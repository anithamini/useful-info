import os
import sys
import time

os.system("adb shell input keyevent 3")
os.system(" adb shell am start -a android.intent.action.CALL -d tel:+919666848739")
os.system("adb shell input keyevent 20")
os.system("adb shell input keyevent 20")
os.system("adb shell input keyevent 66")
time.sleep(20)
os.system("adb shell input keyevent 6")
os.system("adb shell input keyevent 3")
