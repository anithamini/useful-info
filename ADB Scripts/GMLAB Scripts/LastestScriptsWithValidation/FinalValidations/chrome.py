import os
import time
import sys
iterations=1#sys.argv[1]
pass_cnt=0
fail_cnt=0
LaunchPassCnt=0
LaunchFailCnt=0
KillPassCnt=0
KillFailCnt=0

print("------------Chrome Application-------------")

def kill_chrome():
    os.system("adb shell am force-stop com.android.chrome")

def Validate(s1,n):
    os.system( "adb shell dumpsys activity > chrome.txt")
    with open("chrome.txt","r") as fh:
            buff=fh.read()
            if(n=="Chrome"):
                if(s1 in buff):
                    return(True)
                else:
                    return(False)
            if(n=="KillChrome"):
                if(s1 in buff):
                    return(False)
                else:
                    return(True)
            
def launch_chrome():
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
for i in range(int(iterations)):
    kill_chrome()
    if(Validate("packageName=com.android.chrome processName=com.android.chrome","KillChrome")):
        KillPassCnt+=1
    else:
        KillFailCnt+=1
    launch_chrome()
    if(Validate("packageName=com.android.chrome processName=com.android.chrome","Chrome")):
        LaunchPassCnt+=1
    else:
        LaunchFailCnt+=1
    for n in range(0,3):
        browse_websites(n)
        time.sleep(5)
        if(Validate("realActivity=com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity","Chrome")):
            pass_cnt+=1
        else:
            fail_cnt+=1
            print("unable to browse in chrome...")
    os.system("adb shell input keyevent 3")
print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
print("Browse Pass Count:",pass_cnt,",Fail Count:",fail_cnt)
print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)

