import os
import time
import sys

pass_cnt=0
fail_cnt=0

def launch_display_settings():
    print("............Opening the DISPLAY Settings............")
    os.system("adb shell am start -n com.android.settings/.DisplaySettings")

def change_sleep():
                                    #//////////////send message ////////////////
    os.system("adb shell am start -a android.intent.action.SENDTO -d sms:+919966292291 --es sms_body 'why so serious' --ez exit_on_sent true")
    time.sleep(2)
    os.system("adb shell input tap 980 1139")
    time.sleep(3)
    print("................closing sms app................")
    os.system("adb shell input keyevent 3")
    launch_display_settings()
    for i in range(1,6):
        os.system("adb shell input keyevent 20")
    for i in range(2):
        os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 967 1914")

def validation():
    os.system("adb shell dumpsys settings > sleep1_log.txt")
    fp=open("sleep1_log.txt","r+")
    buff=fp.read()
    str1="value:60000 default:60000"
    if str1 in buff:
        print(str1)
        return 1
    else:
        return 0
    
def kill_display():
    os.system("adb shell am force-stop com.android.settings")


print("...........Closing the Settings........")
kill_display()
launch_display_settings()
time.sleep(2)
change_sleep()
print("sleep is set for 1 sec delay")
if(validation()):
    pass_cnt+=1    
else:
    fail_cnt+=1    
print("pass_cnt=",pass_cnt)
print("fail_cnt=",fail_cnt)
