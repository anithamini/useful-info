'''
Created on Jul 30, 2018

@author: hnagella
'''
import os
from time import sleep
from common import constants

DataOnPassCnt=0
DataOnFailCnt=0
DataOffPassCnt=0
DataOffFailCnt=0

def checkmobiledata():
    os.system("adb shell getprop >mobiledata.txt")                               #to get log information of mobile data
    fp=open("mobiledata.txt","r+")
    buff=fp.read()
    if("[gsm.defaultpdpcontext.active]: [true]" in buff):
        return 1
    else:
        return 0

def Mobiledata_ON():
    global DataOnPassCnt
    global DataOnFailCnt
    global fileobj_logsummary
    os.system("adb shell svc data enable")                                       #to enable mobile data
    sleep(3)
    if(checkmobiledata()):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "Test EnableMobileData"+"\t"+"PASS\n")
        DataOnPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "Test EnableMobileData"+"\t"+"FAIL\n")
        DataOnFailCnt+=1

def Mobiledata_OFF():
    global DataOffPassCnt
    global DataOffFailCnt
    global fileobj_logsummary
    os.system("adb shell svc data disable")                                      #to disable mobile data
    sleep(3)
    if(checkmobiledata()):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "Test DisableMobileData"+"\t"+"FAIL\n")
        DataOffFailCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "Test DisableMobileData"+"\t"+"PASS\n")
        DataOffPassCnt+=1
        
def TestMobileDataSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nMobileData_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestMobileDataSanity_testsuit(): 
    Mobiledata_ON()
    Mobiledata_OFF()

def MobileData_sanity_summary_log():
    global DataOnPassCnt
    global DataOnFailCnt
    global DataOffPassCnt
    global DataOffFailCnt
    global fileobj_logsummary
    print("DataOn PassCnt:",DataOnPassCnt," DataOn FailCnt:",DataOnFailCnt)
    print("DataOff PassCnt:",DataOffPassCnt,"DataOff FailCnt:",DataOffFailCnt)
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nMobileData_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(DataOnPassCnt+DataOnFailCnt)+"\t" + str(DataOnPassCnt) +"\t"+ str(DataOnFailCnt)+"\n")
    fileobj_logsummary.write(str(DataOffPassCnt+DataOffFailCnt)+"\t" + str(DataOffPassCnt) +"\t"+ str(DataOffFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    DataOnPassCnt=0
    DataOnFailCnt=0
    DataOffPassCnt=0
    DataOffFailCnt=0
    
def TestMobileDataSanity_main():
    print("Entry of TestMobileDataSanity_main")
    TestMobileDataSanity_Setup()
    TestMobileDataSanity_testsuit()
    MobileData_sanity_summary_log()
