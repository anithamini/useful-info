import os
import time
import re
import sys
iterations =sys.argv[1]
print("Iterations:",iterations)
pass_cnt=0
fail_cnt=0

print("--------------Wifi ON/OFF----------------")

def launch_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
def toggle_wifi():
    os.system("adb shell input tap 940 368")
    time.sleep(5)
def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    bt_log = open("wifi_log.txt","r+")
    buffer = bt_log.readline()
    bt_log.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

def kill_wifi():
    os.system("adb shell am force-stop com.android.settings")


launch_wifi()
for n in range(int(iterations)):
	state = Checkwifistate()
	if state:
	    print("wifi enabled")
	    toggle_wifi()
	    time.sleep(2)
	    toggle_wifi()
	else:
	    print("wifi disabled")
	    toggle_wifi()
	    state = Checkwifistate()
	if state:
	    print("wifi enabled")
	    pass_cnt+=1            
	else:
	    print("wifi disabled")
	    fail_cnt+=1
		
	time.sleep(5)
	toggle_wifi()
print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)



 
