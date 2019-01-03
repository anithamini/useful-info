import os
import time
import sys
iterations=sys.argv[1]
pass_cnt=0
fail_cnt=0

def launch_display_settings():
    print("............Opening the DISPLAY Settings............")
    os.system("adb shell am start -n com.android.settings/.DisplaySettings")

def change_sleep():
    for i in range(1,6):
        os.system("adb shell input keyevent 20")
    for i in range(2):
        os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 359 987")

def validation():
    os.system("adb shell dumpsys settings > sleep_log.txt")
    fp=open("sleep_log.txt","r+")
    buff=fp.read()
    str1="value:60000 default:60000"
    if str1 in buff:
        print(str1)
        return 1
    else:
        return 0
    
def kill_display():
    os.system("adb shell am force-stop com.android.settings")

for i in range(int(iterations)):
	print("...........Closing the Settings........")
	kill_display()
	print("...........Opening the Settings........")
	launch_display_settings()
	change_sleep()
	print("sleep is set for 1 sec delay")
	if(validation()):
	    pass_cnt+=1   
	else:
	    fail_cnt+=1
    
print("pass_cnt=",pass_cnt)
print("fail_cnt=",fail_cnt)


    
    
