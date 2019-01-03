import os,time
from sys import argv
passcnt=0
failcnt=0
Iterations=2#argv[1]
def OpenRecentApps():
    os.system("adb shell input keyevent KEYCODE_APP_SWITCH")
    time.sleep(2)
def OpenRandomAPP_RecentApps():
    for i in range(0,3):
        os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
        time.sleep(2)
    os.system("adb shell input keyevent KEYCODE_ENTER")
    time.sleep(2)
    
def DeleteRandomApp_RecentApps():
    for j in range(0,3):
        os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
        time.sleep(2)
    os.system("adb shell input keyevent KEYCODE_DEL")
    time.sleep(2)
    os.system("adb shell input keyevent 3")
for i in range(int(Iterations)):    
    OpenRecentApps()
    OpenRandomAPP_RecentApps()
    OpenRecentApps()
    DeleteRandomApp_RecentApps()
print("Pass count,Fail count:",passcnt,failcnt)
