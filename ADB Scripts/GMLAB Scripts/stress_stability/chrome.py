
                             


import os
import time
import sys
#iterations=1
iterations=sys.argv[1]
pass_cnt=0
fail_cnt=0

def kill_chrome():
    print("=======================================================================")
    print("Killing background process of Chrome")
    print("=======================================================================")
    os.system("adb shell am force-stop com.android.chrome")

def check_chrome():
    os.system( "adb shell dumpsys activity > chrome.txt")
    with open("chrome.txt","r") as fh:
            buff=fh.read()
            s1="packageName=com.android.chrome processName=com.android.chrome"
            s2="realActivity=com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity"
            if((s1 in buff)or(s2 in buff)):
                return(True)
            else:
                return(False)

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
for i in range(int(iterations)):    
	kill_chrome()
	launch_chrome()
	for n in range(0,3):
	    browse_websites(n)
	    time.sleep(5)
	    res=check_chrome()
	    print(res)
	    if(res):
	        pass_cnt+=1
	    else:
	        fail_cnt+=1
	        print("unable to browse in chrome...")

	os.system("adb shell input keyevent 3")
print("pass_count is:",pass_cnt)
print("fail_count is:",fail_cnt)


