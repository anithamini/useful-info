'''
Created on 13-Apr-2018

@author: galluri
'''
import os, time, re
from common import constants

pCount=0
fCount=0


def AirplaneModeOn():
    os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    time.sleep(2)
    os.system("adb shell input keyevent 23")
    time.sleep(5)


def AirplaneModeOff():
    global fCount
    global pCount
    os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    time.sleep(2)
    os.system("adb shell input keyevent 23")
    time.sleep(5)    
    

def CheckAirplanestate():
    os.system( "adb shell dumpsys wifi > airplane_log.txt")
    with open("airplane_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="mAirplaneModeOn true"
            if(string1 in line):
                print("Airplane mode is ON!")
                return(True)
        print("Airplane mode is OFF!")    
        return(False)
        
def EnableAirplane():
    global fCount
    global pCount
    print ("Pre-check if Airplane mode status is already enabled: ")
    status = CheckAirplanestate()
    print ("Disable if it is already enabled")
    if (status == True):
        AirplaneModeOff()
        time.sleep(5)
    status = CheckAirplanestate()
    if (status == False):
        print("calling toggle to turn on airplanemode")
        AirplaneModeOn()
        time.sleep(5)
        status = CheckAirplanestate()
        if (status == True):
            global fileobj_logfile
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestAirplaneON"+"\t"+"PASS\n")
        pCount=pCount+1
    else:
        fileobj_logfile.write("TC_3" +"\t"+ "TestAirplaneON"+"\t"+"FAIL\n")
        fCount=fCount+1
            
def DisableAirplane():
    global fCount
    global pCount
    print ("Pre-check if Airplane mode status is already disabled:")
    status = CheckAirplanestate()
    time.sleep(5)
    print ("enabled if already disabled")
    if (status == False):
        AirplaneModeOn()
        time.sleep(5)
    status = CheckAirplanestate()
    if (status == True):
        print("calling toggle to turn OFF Airplane Mode")
        AirplaneModeOff()
        time.sleep(5)
        status = CheckAirplanestate()
        if (status == False):
            fileobj_logfile.write("TC_4" +"\t"+ "TestAirplaneOFF"+"\t"+"PASS\n")
        pCount=pCount+1
    else:
        fileobj_logfile.write("TC_4" +"\t"+ "TestAirplaneOFF"+"\t"+"FAIL\n")
        fileobj_logfile.write("---------------------------------------------------\n")
        global fCount
        fCount=fCount+1
    fileobj_logfile.close()   

def Airplane_sanity_summary_log():
    global fCount
    global pCount
    print ("Pass : ", pCount)
    print ("Fail : ", fCount )
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    global fileobj_logsummary
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nAirplane_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(pCount+fCount)+"\t" + str(pCount) +"\t"+ str(fCount))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    
def Airplanesanity_setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nAirplane_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    state = CheckAirplanestate()
    if state == "Enabled":
        DisableAirplane()
        
                            
def AirplaneTest_Testsuite():
    EnableAirplane()
    DisableAirplane()

def Airplanetest_Main():
    Airplanesanity_setup()
    AirplaneTest_Testsuite()
    Airplane_sanity_summary_log()
    pCount=0
    fCount=0

