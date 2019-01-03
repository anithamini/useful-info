import os
import sys
import time
import re

#wifi settings

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")
    
def kill_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    time.sleep(1)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 66")
   
def checkwifistatus():
    os.system("adb shell dumpsys wifi>wifi_log.txt")
    wifi_log=open("wifi_log.txt","r+")
    buffer=wifi_log.read();
    wifi_log.close()
    enabled=re.search('Wi-Fi is enabled',buffer,re.I)
    if enabled:
        return(True)
    else:
        return(False)    

def launch_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")

    os.system("adb shell input keyevent 20")

    os.system("adb shell input keyevent 23")
    #time.sleep(2)
    check=checkwifistatus()
    if check:
        return(True)
    else:
        return(False)
    
# mobile data

def checkmobiledata():
    os.system("adb shell getprop>wi-fi_mobile.txt")
    fp=open("wi-fi_mobile.txt","r+")
    buff=fp.read()
    str1="[sys.defaultapn.enabled]: [false]" # it will appear when wifi and mobile data is on
    if str1 in buff:
        print str1
        return 1
    else:
        return 0

def switch_mobiledata():
    os.system("adb shell svc data enable")
    time.sleep(3)
    res=checkmobiledata()
    if res:
        return res
    
def mobiledata_off():
    os.system("adb shell svc data disable")
    time.sleep(2)
    
    

    
#if wifi is on then it will kill
res=checkwifistatus()
print res
if res:
    launch_wifi()
    time.sleep(3)
    check=checkwifistatus()
    print check
else:
    launch_wifi()
    time.sleep(3)
    check=checkwifistatus()
    print check
result=switch_mobiledata()
if result:
    print "mobile data on but wifi highest priority"
else:
    print "mobile data off"
mobiledata_off()
kill_wifi()
kill_settings()





    

