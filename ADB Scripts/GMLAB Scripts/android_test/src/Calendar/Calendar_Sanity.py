'''
Created on Jul 26, 2018

@author: hnagella
'''
import os
from time import sleep
from common import constants
LaunchPassCnt=0
LaunchFailCnt=0
EventPassCnt=0
EventFailCnt=0
KillPassCnt=0
KillFailCnt=0

def Validate(s1,s2):
    os.system('adb shell dumpsys '+s2+' > calendar.txt')
    with open("calendar.txt","r") as fh:
        while 1:
            buf=fh.readline()
            if (buf==""):
                break
            if(s1 in buf):
                return(True)
            else:           
                return(False)     

def kill_Calendar():
    global KillPassCnt
    global KillFailCnt
    os.system("adb shell input keyevent 3")
    os.system("adb shell am force-stop com.google.android.calendar")
    sleep(4)
    if(Validate("I=com.android.launcher3/com.android.searchlauncher.SearchLauncher",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillCalendar"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillCalendar"+"\t"+"FAIL\n")
        KillFailCnt+=1

def launch_Calendar():
    global LaunchPassCnt
    global LaunchFailCnt
    os.system("adb shell monkey -p com.google.android.calendar -c android.intent.category.LAUNCHER 1")
    sleep(2)
    if(Validate("A=google.android.task.calendar",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchCalendar"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchCalendar"+"\t"+"FAIL\n")
        LaunchFailCnt+=1
def EventValidate():
    os.system('adb shell dumpsys activity > calendar11.txt')
    with open("calendar11.txt","r") as fh:
        buf=fh.read()
        #for line in buf:
        if("act=android.intent.action.PACKAGE_RESTARTED dat=package:com.google.android.calendar" in buf):
            return(True)
        else:           
            return(False) 
def Create_Event():
    global EventPassCnt
    global EventFailCnt
    os.system("adb shell input tap 935 1878")
    os.system("adb shell input tap 950 1900")
    sleep(2)
    os.system("adb shell input tap 362 357")
    os.system("adb shell input text TestingEvent")
    sleep(3)
    os.system("adb shell input tap 987 1963")
    sleep(2)
    os.system("adb shell input tap 1010 161")
    sleep(2)
    if(EventValidate()):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestCreateEvent"+"\t"+"PASS\n")
        EventPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestCreateEvent"+"\t"+"FAIL\n")
        EventFailCnt+=1
    os.system("adb shell am force-stop com.google.android.calendar")

def TestCalendarSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nCalendar_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestCalendarSanity_testsuit():
    kill_Calendar()
    launch_Calendar()
    Create_Event()

def Calendar_sanity_summary_log():
    global LaunchPassCnt
    global LaunchFailCnt
    global KillPassCnt
    global KillFailCnt
    global EventPassCnt
    global EventFailCnt
    global fileobj_logsummary
    print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
    print("Kill Pass Count=",KillPassCnt,",KillFail Count=",KillFailCnt)
    print("Event Pass Count=",EventPassCnt,",Event Fail Count=",EventFailCnt)

    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nCalendar_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str(KillPassCnt+KillFailCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt)+"\n")
    fileobj_logsummary.write(str(EventPassCnt+EventFailCnt)+"\t" + str(EventPassCnt) +"\t"+ str(EventFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    EventPassCnt=0
    EventFailCnt=0
    KillPassCnt=0
    KillFailCnt=0
    
def TestCalendarSanity_main():
    print("Entry of TestCalendarSanity_main")
    TestCalendarSanity_Setup()
    TestCalendarSanity_testsuit()
    Calendar_sanity_summary_log()


