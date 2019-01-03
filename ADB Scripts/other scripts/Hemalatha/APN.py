import os
import time
def launch_wifi():
    os.system("adb shell am start -a android.settings.SETTINGS")
    os.system("adb shell input tap 110 170")
    os.system("adb shell input text Wi-fi")
    os.system("adb shell input touchscreen swipe 386 210 386 210")
def enable_wifi():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
def disable_wifi():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
def Checkwifistatus():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    with open("wifi_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="Wi-Fi is enabled"
            if line==string1:
                return(True)
            else:
                return(False)
def cnt_apns():
    cnt=0
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    with open("wifi_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="[ESS]"
            if(string1 in line):
                cnt=cnt+1
                print cnt
    return cnt

def kill_wifi():
    os.system("adb shell am force-stop com.android.settings")
kill_wifi()
launch_wifi()
enable_wifi()
time.sleep(10)
status = Checkwifistatus()
time.sleep(5)

print("Status of wifi:",status)
time.sleep(5)
apn=cnt_apns()
print("No.of devices scanned are:",apn)

print("Disable wifi...")
disable_wifi()

