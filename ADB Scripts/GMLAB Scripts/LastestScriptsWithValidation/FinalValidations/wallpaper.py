import os
import time
import sys
pass_cnt=0
fail_cnt=0
iterations=sys.argv[1]

print("-----------WALLPAPER------------")

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")

def wallpaper_setting():  
    os.system("adb shell am start -a android.settings.SETTINGS")
    for i in range(0,7):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    for i in range(0,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")   
    for i in range(0,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 22")
    time.sleep(2)
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input tap 517 88")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    

def validate():
    s1="packageName=com.android.wallpaperpicker processName=com.android.wallpaperpicker"
    os.system("adb shell dumpsys activity >wall.txt")
    with open("wall.txt","r+") as fh:
        buf=fh.read() 
        if s1 in buf:
            return 1
        else:
            return 0
    
kill_settings()
for i in range(int(iterations)):
    wallpaper_setting()
    if(validate()):
        pass_cnt+=1
    else:
        fail_cnt+=1
    kill_settings()
print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)
