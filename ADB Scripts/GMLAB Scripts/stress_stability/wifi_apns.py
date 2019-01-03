import os
import re
import sys
pass_cnt=0
fail_cnt=0
itr=int(sys.argv[1])
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
    global pass_cnt,fail_cnt
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
        pass_cnt+=1
    else:
        print("no apn's found")
        fail_cnt+=1
        
    

while(itr):
    wifi_on()
    if (wifistate()):
        list_apn()
        wifi_on()
    else:
        print("wifi is disabled")
        fail_cnt+=1
    itr-=1
print("pass_cnt",pass_cnt)
print("fail_cnt",fail_cnt)
