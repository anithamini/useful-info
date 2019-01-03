
                             #Chrome - To verify that user is able to open chrome and able to browse to different websites 


import os
import time
import unittest,time
def kill_chrome():
    print("=======================================================================")
    print("Killing background process of Chrome")
    print("=======================================================================")
    os.system("adb shell am force-stop com.android.chrome")
def launch_chrome():
    print("================== =====================================================")
    print("Launching chrome")
    print("=======================================================================")
    os.system("adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity")
    time.sleep(5)
def browse_websites(i):
    os.system("adb shell input tap 867 195")
    os.system("adb shell input tap 79 183")
    os.system("adb shell input keyevent 84")
    if i==0:
        os.system("adb shell input text amazon ")
        print("opening browser1...........")
    elif i==1:
        os.system("adb shell input text www.gmail.com")
        print("opening browser2...........")
    else:
        os.system("adb shell input text www.innominds.com")
        print("opening browser3...........")
    os.system("adb shell input keyevent 66")
    time.sleep(5)
    
kill_chrome()
launch_chrome()
for n in range(0,3):
    browse_websites(n)
    time.sleep(5)
os.system("adb shell input keyevent 3")



#AppBoosterService: NowApp: com.android.chrome foreground ? false
#ActivityManager: START u0 {cmp=com.android.chrome/org.chromium.chrome.browser.preferences.Preferences} from uid 10056 on display 0----opened
#MOVE TO FOREGROUND: com.android.chrome
