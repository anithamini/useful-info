import os
import time
import re
def kill_playstore():
    os.system("adb shell am force-stop com.android.vending")
def launch_playstore():
    os.system("adb shell am start -n com.android.vending/com.android.vending.AssetBrowserActivity")
def installapk():
    os.system("adb shell input keyevent 84")
    time.sleep(1)
    #str2=input("enter the apk to be downloaded")
    str2="ola"
    os.system("adb shell input text "+str2)
    os.system("adb shell input keyevent 66")
    time.sleep(5)
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
def checking():
    os.system("adb shell dumpsys activity >download.txt")
    fp=open("download.txt","r")
    buf=fp.read()
    fp.close()
    return buf
def downloading():
    buf=checking()
    while(re.search(":com.android.vending/u0a27 s1/1 u0/1 +",buf)==None):
        buf=checking()
    print("download started")
    print(time.asctime())
    buf=checking()
    while(re.search("DOWNLOAD_COMPLETE",buf)==None):
        buf=checking()
    print("downloaded successfully")
    print(time.asctime())
def launch_dnapk():
    print("waiting to launch")
    #str1=input("enter the package name")
    str1="com.olacabs.customer/com.olacabs.customer.ui.SplashActivity"
    os.system("adb shell am start -n "+str1)
def checking_data():
    os.system("adb shell dumpsys telephony.registry >tel.txt")
    fs=open("tel.txt","r")
    bug=fs.read()
    if(re.search("mDataConnectionState=2",bug)):
        return True
    else:
        return False
def checking_wifi():
    os.system( "adb shell dumpsys wifi > wifi.txt")
    wf = open("wifi.txt","r")
    buffer = wf.read();
    wf.close()
    Enabled = re.search('curState=CompletedState', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

    
kill_playstore()
time.sleep(5)
launch_playstore()
time.sleep(5)
if(checking_data() or checking_wifi()):
    installapk()
    downloading()
    time.sleep(5)
    launch_dnapk()

else:
    print("data or wifi is not enabled")
