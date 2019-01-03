import os
import time
def OpenNotificationBar():
    os.system("adb shell input swipe 0 0 0 300")
    time.sleep(1)
def ClearSingleNotification():
    os.system("adb shell input swipe 0 400 500 0")
    time.sleep(1)
def CloseNotificationBar():
    os.system("adb shell input swipe 0 400 300 0")
    time.sleep(1)
    
OpenNotificationBar()
ClearSingleNotification()
CloseNotificationBar()
