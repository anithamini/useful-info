import os
import time
import re
from common import constants
from common import *


pCount=0
fCount=0
 
def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wlan_log.txt")
    wlan_log = open("wlan_log.txt","r+")
    buffer = wlan_log.readline();
    wlan_log.close()
    Enabled = re.search(constants.wifi_enabledstring, buffer, re.I)
    if Enabled:
        return("Enabled")
    else:
        Disabled = re.search(constants.wifi_disabledstring, buffer, re.I) 
        if Disabled:
            return("Disabled")
     
def Toggle_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 23")
    time.sleep(5)
 
def CheckwifiConnectedstate():
    os.system( "adb shell dumpsys wifi > wlan_log.txt")
    with open("wlan_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1= constants.ssid
            if(string1 in line):
                #print("connected")
                return(True)
 
def TestWifiSanity_Setup():
     
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nwifi_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    state = Checkwifistate()
    if state == "Enabled":
        Toggle_wifi()
         
def TestWifiON():
    global fCount
    global pCount
    Toggle_wifi()
    result = Checkwifistate()
    print("current state after ON", result)
    if(result == "Enabled"):
        global fileobj_logfile
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestWifiON"+"\t"+"PASS\n")
        pCount=pCount+1
    else:
        fileobj_logfile.write("TC_1" +"\t"+ "TestWifiON"+"\t"+"FAIL\n")
        fCount=fCount+1
 
def TestWifiOFF():
    global fCount
    global pCount
    Toggle_wifi()
    result = Checkwifistate()
    print("current state after OFF", result)
    if(result == "Disabled"):
        fileobj_logfile.write("TC_2" +"\t"+ "TestWifiOFF"+"\t"+"PASS\n")
        pCount=pCount+1
    else:
        fileobj_logfile.write("TC_2" +"\t"+ "TestWifiOFF"+"\t"+"FAIL\n")
        fileobj_logfile.write("---------------------------------------------------\n")
        global fCount
        fCount=fCount+1
    fileobj_logfile.close()    
     
def TestWifiSanity_testsuit():
    TestWifiON()
    TestWifiOFF()

def Wifi_sanity_summary_log():
    global fCount
    global pCount
    print ("Pass : ", pCount)
    print ("Fail : ", fCount )
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    global fileobj_logsummary
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nWifi_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(pCount+fCount)+"\t" + str(pCount) +"\t"+ str(fCount))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    pCount=0
    fCount=0
    
def TestWifiSanity_main():
    global pCount
    global fCount
    print("entry of TestWifiSanity_main")
    TestWifiSanity_Setup()
    TestWifiSanity_testsuit()
    Wifi_sanity_summary_log()
