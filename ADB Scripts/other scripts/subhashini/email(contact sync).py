import os
import re
import time
def kill_mail():
        os.system("adb shell am force-stop com.google.android.gm")
def launch_mail():
        os.system("adb shell am start -n com.google.android.gm/com.google.android.gm.ConversationListActivityGmail")
        time.sleep(5)
def create_account():
        os.system("adb shell input tap 58 121")
        time.sleep(2)
        os.system("adb shell input tap 560 285")
        time.sleep(2)
        os.system("adb shell input tap 323 404")
        os.system("adb shell input tap 341 264")
        time.sleep(10)
        os.system("adb shell input tap 355 867")
def user_id():
        username=raw_input("enter the user name")
        os.system("adb shell input text " +str(username))
        time.sleep(2)
        os.system("adb shell input tap 556 732")
        time.sleep(8)
def passwd():
        password=raw_input("enter password")
        os.system("adb shell input text " +str(password))
        os.system("adb shell input tap 556 732")
        time.sleep(2)
        os.system("adb shell input text 552 1246")
        time.sleep(10)
        print("account successfully created.........")
def launch_settings():
        os.system("adb shell am start -a android.settings.SETTINGS")
        time.sleep(10)
def contact_sync():
        os.system("adb shell input swipe 415 1273 359 151")
        time.sleep(5)
        os.system("adb shell input tap 346 342")
        time.sleep(5)
        print("syncing the contacts with gmail account")
        for i in range(1,3):
             for j in range(1,3):
                 os.system("adb shell input keyevent 20")
                 time.sleep(5)
             os.system("adb shell input keyevent 66")
             time.sleep(2)
        for i in range(1,3):
              os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
        os.system("adb shell input keyevent 66")
        print("gmail account is synced with contacts")
def kill_settings():
        os.system("adb shell am force-stop com.android.settings")
kill_mail()
launch_mail()
create_account()
user_id()
passwd()
time.sleep(15)
kill_mail()
kill_settings()
launch_settings()
contact_sync()
kill_settings()
