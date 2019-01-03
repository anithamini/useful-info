import os
import unittest
import time
import re

iterations=1
pass_cnt=0
fail_cnt=0


def enable_hotspot():
    os.system("adb shell am start -n com.android.settings/.TetherSettings")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    print("enabled")
def disable_hotspot():
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    print("disabled")
def check_hotspot():
        os.system("adb shell dumpsys wifi > hotspot.txt")
        with open("hotspot.txt","r+") as fp:
            lines=fp.read()
            Enabled = re.search('curState=ApEnabledState',lines,re.I)
            if Enabled:
                    return 1
            else:
                    return 0
def kill_hotspot():
    os.system("adb shell am start -a android.settings.SETTINGS")
    os.system("adb shell input keyevent 3")
    time.sleep(4)
kill_hotspot()
enable_hotspot()
for i in range(int(iterations)):
	os.system("adb shell input keyevent 66")
	result=check_hotspot()
	time.sleep(2)
	if result:
    		print("hotspot is enabled")
    		pass_cnt+=1
    		disable_hotspot()   
	else:
    		fail_cnt+=1
    		os.system("adb shell input keyevent 66")
kill_hotspot()

print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)
         

    
