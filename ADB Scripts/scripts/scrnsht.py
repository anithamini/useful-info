import os
import time

pass_cnt=0
fail_cnt=0

def scrsht():
	os.system("adb shell screencap /sdcard/screen.png")
"""
def test(): 
    os.system("adb shell logcat >scrn.txt")
    with open("scrn.txt","r+") as fh:
            lines= fh.readlines()
            for line in lines:
                    string="com.android.systemui/.screenshot.TakeScreenshotService"
                    if (string in line):
                            return 1
                            break
            else:
                    return 0

for i in range(1,6):
	scrsht()
	result=test()
	if result:
                pass_cnt+=1
        else:
                fail_cnt+=1
"""

 