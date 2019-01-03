import os
import sys
import time
import re
import unittest,time
iterations=3
pass_cnt=0
fail_cnt=0
def kill_playstore():
    os.system("adb shell am force-stop com.android.vending ")
    
def launch_playstore():
    os.system("adb shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
    
def search_app():
    os.system("adb shell input tap 184 90")
    time.sleep(3)
    os.system("adb shell input text facebook")
    
kill_playstore()
launch_playstore()
#time.sleep(3)
#search_app()
for n in range(int(iterations)):
    time.sleep(3)
    search=search_app()
    if search:
        print("serached the app successfully for iterations",n)
        pass_cnt+=1
    else:
        print("couldn't search successfully for iterations",n)
        fail_cnt+=1
    kill_playstore()
    launch_playstore()
    n+=1
print("Searching passed:",pass_cnt)
print("searching failed:",fail_cnt)
 
