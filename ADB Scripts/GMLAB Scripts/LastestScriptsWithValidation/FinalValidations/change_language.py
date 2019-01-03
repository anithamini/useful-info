import os
import time
import sys

pass_cnt=0
fail_cnt=0
iterations=sys.argv[1]

print("----------------Change Language Settings--------------")

def launch_settings():
    os.system("adb shell am start -a android.settings.SETTINGS")

def validation():
    os.system("adb shell dumpsys settings > lang_log.txt")
    fp=open("lang_log.txt","r+")
    buff=fp.read()
    str1="value:com.google.android.inputmethod.japanese"
    if str1 in buff:
        print(str1)
        return 1
    else:
        return 0

def f():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def change_language_settings():
    os.system("adb shell input tap 293 170")
    os.system("adb shell input text 'languages'")
    os.system("adb shell input keyevent 66")
    for i in range(0,4):
        f()
    time.sleep(2)
    os.system("adb shell input keyevent 66")
    

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")


for i in range(int(iterations)):
    kill_settings()
    launch_settings()
    change_language_settings()
    if(validation()):
            pass_cnt+=1  
    else:
        kill_settings()
        launch_settings()
        change_language_settings()
        if(validation()):
            pass_cnt+=1  
        else:
            fail_cnt+=1
    os.system("adb shell input keyevent 66")
print("pass_cnt=",pass_cnt)
print("fail_cnt=",fail_cnt)
