import time
import os
import sys



#for forwarding the message
def msg_forward():
    os.system("adb shell am start -n com.android.mms/com.android.mms.ui.MmsTabActivity")
    os.system("adb shell input tap 340 760")
    os.system("adb shell input touchscreen swipe 340 760 340 760 1000")
    os.system("adb shell input tap 320 1770")
    time.sleep(1)
    os.system("adb shell input text N")
    time.sleep(1)
    os.system("adb shell input tap 580 321")
    os.system("adb shell input tap 1020 1820")
    for i in range(2):
        os.system("adb shell input keyevent 4")



#for deleting the message
def msg_delete():

    os.system("adb shell am start -n com.android.mms/com.android.mms.ui.MmsTabActivity")
    
    os.system("adb shell input tap 340 760")
    os.system("adb shell input touchscreen swipe 340 760 340 760 1000")
    os.system("adb shell input tap 646 1770")

    os.system("adb shell input tap 1020 1820")
    for i in range(2):
        os.system("adb shell input keyevent 4")



msg_forward()
msg_delete()
