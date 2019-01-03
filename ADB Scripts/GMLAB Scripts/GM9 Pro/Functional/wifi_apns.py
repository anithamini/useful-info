import os
import re


def wifi_on():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    os.system("adb shell input tap 960 390")
def wifistate():
    os.system("adb shell dumpsys wifi >wifi.txt")
    fd=open("wifi.txt","r")
    buf=fd.read()
    if("Wi-Fi is enabled" in buf):
        fd.close()
        return True
    else:
        return False
def list_apn():
    cnt=0
    fd=open("wifi.txt","r")
    buf=fd.readline()
    while (1):
        if("Networks filtered out due to low signal strength:" in buf):
            cnt+=1
        
        if("WifiScoreReport:" in buf):
            break
        buf=fd.readline()
    if(cnt>=0):
        print("no of apn's available",cnt)
    else:
        print("no apn's found")
        
    

wifi_on()
if (wifistate()):
    list_apn()
else:
    print("wifi is disabled")
