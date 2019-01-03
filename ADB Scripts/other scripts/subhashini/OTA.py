import os
import time
def launch_OTA():
    os.system("adb shell am start -a android.settings.SETTINGS")
    time.sleep(2)
    os.system("adb shell input swipe 548 1268 329 184")
    os.system("adb shell input tap 398 1236")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
def kill_settings():
    os.system("adb shell am force-stop com.android.settings")
def update_system():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    time.sleep(10)  #delay based on network speed
    print("system updated.........")
    os.system("adb shell input keyevent 3")
kill_settings()
launch_OTA()
update_system()
