import os
import sys
import time

os.system("adb shell input keyevent 3")
"""os.system("adb shell input tap 453 1202")
os.system("adb shell input tap 381 201")
os.system("adb shell input text bhavani.vector")
time.sleep(3)
os.system("adb shell input tap 292 505")
os.system("adb shell input tap 292 505")
time.sleep(5)
os.system("adb shell input tap 239 1234")
time.sleep(3)
for i in range (0,2):
    os.system("adb shell input text msgapp")
    os.system("adb shell input tap 667 606")

"""
def send_sms():
    os.system("adb shell am start -a android.intent.action.SENDTO -d sms:918008182830 --es sms_body SMS --ez exit_on_sent true")
    os.system("adb shell input tap 560 1232")
    os.system("adb shell input tap 480 1234")
    os.system("adb shell input tap 662 1236")

send_sms()
