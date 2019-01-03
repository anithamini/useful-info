'''
Created on Jul 24, 2018

@author: akesiboyina
'''

import datetime
from Creat_alarm import alarm,func
from time import strftime,sleep
import os
from common import constants
LaunchPassCnt=0
LaunchFailCnt=0
Ring_pass_cnt=0
Ring_fail_cnt=0
KillPassCnt=0
KillFailCnt=0

print("---------------Alarm-----------------")

def Validate(s1,n):
    os.system( "adb shell dumpsys activity > alarm.txt")
    with open("alarm.txt","r") as fh:
            buff=fh.read()
            if(n=="Alarm"):
                if(s1 in buff):
                    return(True)
                else:
                    return(False)
            if(n=="KillAlarm"):
                if(s1 in buff):
                    return(False)
                else:
                    return(True)
                
def kill_alarm():
    global KillPassCnt
    global KillFailCnt
    global fileobj_logsummary
    os.system("adb shell am force-stop com.google.android.deskclock")
    if(Validate("packageName=com.google.android.deskclock processName=com.google.android.deskclock","KillAlarm")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "Killalarm"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "Killalarm"+"\t"+"FAIL\n")
        KillFailCnt+=1

def Launch_alarm():
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logsummary
    os.system("adb shell am start -n com.google.android.deskclock/com.android.deskclock.DeskClock")
    sleep(2)
    if(Validate("packageName=com.google.android.deskclock processName=com.google.android.deskclock","Alarm")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "launchalarm"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "launchalarm"+"\t"+"FAIL\n")
        LaunchFailCnt+=1

def Checkalarmstate(timee):
    os.system( "adb shell dumpsys alarm > aaaa.txt")
    with open("aaaa.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1=timee
            s2="user:0 pendingSend:false time:"
            if((s1 in line) or (s2 in line)):
                return(True)
        return(False)
    
def set_alarm():
    global Ring_pass_cnt
    global Ring_fail_cnt
    global fileobj_logsummary
    timee=datetime.datetime.now().strftime('%H:%M:%S')
    reg=timee.split(':')
    a=reg[1]
    hr=reg[0]
    minu=(int(a)+2 )
    alarm(hr,minu)
    data=str(hr)+':'+str(minu)
    print(data)
    print("Alarm is ON")
    while(Checkalarmstate(timee)):
        pass
    if(Checkalarmstate(timee)):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "settingalarm"+"\t"+"FAIL\n")
        Ring_fail_cnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "settingalarm"+"\t\t"+"PASS\n")
        Ring_pass_cnt+=1
        print("Alarm is ringing")
        os.system("adb shell input keyevent 3")
        sleep(2)
        os.system("adb shell input tap 804 375")

def TestAlarmSanity_Setup(): 
      
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nAlarm_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")

def TestAlarmSanity_testsuit():
    kill_alarm()
    Launch_alarm()
    set_alarm()
    
def Alarm_sanity_summary_log():
    global LaunchPassCnt
    global LaunchFailCnt
    global Ring_pass_cnt
    global Ring_fail_cnt
    global KillPassCnt
    global KillFailCnt
    global fileobj_logsummary
    print("Launch Pass count:",LaunchPassCnt,",Fail Count:",LaunchFailCnt)
    print("Alarm Ringing pass_cnt:",Ring_pass_cnt,",Alarm Ringing fail_cnt:",Ring_fail_cnt)
    print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nAlarm_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(KillPassCnt+KillFailCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt)+"\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str( Ring_pass_cnt+ Ring_fail_cnt)+"\t" + str( Ring_pass_cnt) +"\t"+ str( Ring_fail_cnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    Ring_pass_cnt=0
    Ring_fail_cnt=0
    KillPassCnt=0
    KillFailCnt=0

def TestAlarmSanity_main():
    global pCount
    global fCount
    print("entry of TestAlarmSanity_main")
    TestAlarmSanity_Setup()
    TestAlarmSanity_testsuit()
    Alarm_sanity_summary_log()

