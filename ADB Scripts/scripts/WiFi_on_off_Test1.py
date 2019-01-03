import os, time, re
from Utility import Utility

def ToggleWifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 23")
    time.sleep(5)

def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wlan_log.txt")
    wlan_log = open("wlan_log.txt","r+")
    buffer = wlan_log.readline();
    wlan_log.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)
    
def EnableWifi():
    print ("pre check if status is already enabled")
    status = Checkwifistate()
    print ("disable if already enabled")
    if (status == True):
        ToggleWifi()
    status = Checkwifistate()
    if (status == False):
        print("calling toggle to turn on wifi")
        ToggleWifi()
        if (status == True):
            print("EnableWifi pass")
        else:
            print("EnableWifi fail") 
            
def DisableWifi():
    print ("pre check if status is already disabled")
    status = Checkwifistate()
    print ("enabled if already disabled")
    if (status == False):
        ToggleWifi()
    status = Checkwifistate()
    if (status == True):
        print("calling toggle to turn OFF wifi")
        ToggleWifi()
        if (status == False):
            print("DisableWifi pass")
        else:
            print("DisableWifi fail") 
                        
def WifiTest_Testsuit():
    EnableWifi()
    DisableWifi()
    #WifiScan()
    #Wifi_presavedconnect()
    
    

def Wifitest_Main():
    Devicelist = Utility.DeviceStatus()
    if (Devicelist == 0):
        print ("No device detected")
        exit
    else:
        print ("calling testsuit")
        WifiTest_Testsuit()

Wifitest_Main()