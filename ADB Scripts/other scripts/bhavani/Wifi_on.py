import os
import time
import sys
import re

Iterations = 3
print("Iterations:",Iterations)

def launch_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
def toggle_wifi():
    os.system("adb shell input tap 250 220")

def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    bt_log = open("wifi_log.txt","r+")
    buffer = bt_log.readline();
    bt_log.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)
launch_wifi()
for n in range(int(Iterations)):
    state = Checkwifistate()
    if state:
        print("wifi enabled")
    else:
        print("wifi disabled")
    time.sleep(5)
    toggle_wifi()

 
