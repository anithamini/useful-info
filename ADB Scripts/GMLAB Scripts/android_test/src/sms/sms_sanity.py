'''
Created on Jul 30, 2018

@author: akesiboyina
'''

import os
import time
from common import constants
i=0
LaunchPassCnt=0
LaunchFailCnt=0
SmsPassCnt=0
SmsFailCnt=0
MultiSmsPassCnt=0
MultiSmsFailCnt=0
DeletePassCnt=0
DeleteFailCnt=0
SimPassCnt=0
SimFailCnt=0
KillPassCnt=0
KillFailCnt=0
ForwardPassCnt=0
ForwardFailCnt=0
print("Working with Messages application")

def Validate(s1,s2):
        os.system("adb shell dumpsys activity "+s2+" > Sms.txt")
        with open("Sms.txt","r") as fh:
                buf=fh.read()
                if(s1 in buf):
                        return(True)

def sim_test():
    global SimPassCnt
    global SimFailCnt
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="[gsm.sim.state]: [READY,READY]"
            string2 = "[gsm.sim.state]: [READY,NOT_READY]"
            string3 = "[gsm.sim.state]: [NOT_READY,READY]"
            string4 = "[gsm.sim.state]: [ABSENT,READY]"
            string5 = "[gsm.sim.state]: [READY,ABSENT]"
            if (string1 in line or string2 in line or string3 in line or string4 in line or string5 in line):
                print("Sim present, so procedding the test")
                fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
                fileobj_logfile.write("TC_1" +"\t"+ "TestSimPresence"+"\t"+"PASS\n")
                SimPassCnt+=1
                return 1
        else:
                fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
                fileobj_logfile.write("TC_1" +"\t"+ "TestSimPresence"+"\t"+"FAIL\n")
                print("sim not present, please insert the sim and start the test")
                SimFailCnt+=1
                return 0
                
def sending():
    os.system("adb shell input tap 958 1096")
    time.sleep(3)
    for i in range(0,2):
        os.system("adb shell input keyevent 4")

def page_open():
    global LaunchPassCnt
    global LaunchFailCnt
    os.system("adb shell monkey -p com.google.android.apps.messaging 1")
    time.sleep(2)
    if(Validate("packageName=com.google.android.apps.messaging processName=com.google.android.apps.messaging"," ")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchSms"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchSms"+"\t"+"FAIL\n")
        LaunchFailCnt+=1
        
def page_kill():
    global KillPassCnt
    global KillFailCnt
    os.system("adb shell am force-stop com.google.android.apps.messaging")
    time.sleep(2)
    if(Validate("I=com.android.launcher3/com.android.searchlauncher.SearchLauncher",'recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_6" +"\t"+ "TestKillSMS"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_6" +"\t"+ "TestKillSMS"+"\t"+"FAIL\n")
        KillFailCnt+=1
def f():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    
def sms():
    global SmsPassCnt
    global SmsFailCnt
    os.system("adb shell input tap 910 1880")
    os.system("adb shell input text 9100205456")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input text Hai")
    sending()
    if(Validate("realActivity=com.google.android.apps.messaging/.ui.conversation.ConversationActivity","activities")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestSmsSending"+"\t"+"PASS\n")
        SmsPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestSmsSending"+"\t"+"FAIL\n")
        SmsFailCnt+=1

def Forward_sms():
    global ForwardPassCnt
    global ForwardFailCnt
    page_open()
    os.system("adb shell input tap 447 396")
    os.system("adb shell input touchscreen swipe 930 1670 930 1670 1000")
    os.system("adb shell input tap 513 155")
    for i in range(0,2):
        os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 950 1870")
    for i in range(0,2):
        os.system("adb shell input keyevent 4")
    time.sleep(5)
    if(Validate("cmp=com.google.android.apps.messaging/.ui.conversation.ConversationActivity"," ")):
        ForwardPassCnt+=1
    else:
        ForwardFailCnt+=1
        
def sms_multiplepeople():
    global MultiSmsPassCnt
    global MultiSmsFailCnt
    os.system("adb shell monkey -p com.google.android.apps.messaging 1")
    os.system("adb shell input tap 910 1880")
    list=["9100205456","9640281782","9100205816"]
    for number in list:
        os.system("adb shell input text "+number)
        os.system("adb shell input keyevent 66")
        os.system("adb shell input tap 734 368")
    os.system("adb shell input tap 1008 1939")
    os.system("adb shell input text SMS%sto%sMultiple%scontacts....")
    sending()
    time.sleep(3)
    if(Validate("keysPaused=false inHistory=true visible=true","activities")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_5" +"\t"+ "TestSmsMultiple"+"\t"+"PASS\n")
        MultiSmsPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_5" +"\t"+ "TestSmsMultiple"+"\t"+"FAIL\n")
        MultiSmsFailCnt+=1
        

def Delete_sms():
    global DeletePassCnt
    global DeleteFailCnt
    os.system("adb shell monkey -p com.google.android.apps.messaging 1")
    os.system("adb shell input touchscreen swipe 450 700 450 700 1000")    
    time.sleep(5)
    os.system("adb shell input tap 725 137")
    time.sleep(2)
    f()
    time.sleep(3)
    if(Validate("com.google.android.apps.messaging/com.google.android.apps.messaging.wearable.WearableReceiver"," ")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_4" +"\t"+ "TestDeleteSms"+"\t"+"PASS\n")
        DeletePassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_4" +"\t"+ "TestDeleteSms"+"\t"+"FAIL\n")
        DeleteFailCnt+=1   
    for i in range(0,2):
        os.system("adb shell input keyevent 4")
        
def TestSmsSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nSms_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    os.system("adb shell am force-stop com.google.android.apps.messaging")
    
def TestSmsSanity_testsuit():
    if(sim_test()):
        page_open()
        sms()
        Delete_sms()
        sms_multiplepeople()
        Forward_sms()
    page_kill()
        
def Sms_sanity_summary_log():
    global SimPassCnt
    global SimFailCnt
    global LaunchPassCnt
    global LaunchFailCnt
    global SmsPassCnt
    global SmsFailCnt
    global MultiSmsPassCnt
    global MultiSmsFailCnt
    global DeletePassCnt
    global DeleteFailCnt
    global KillPassCnt
    global KillFailCnt
    global ForwardPassCnt
    global ForwardFailCnt
    global fileobj_logsummary
    print("Sim Pass Count=",SimPassCnt,",Sim Fail Count=",SimFailCnt)
    print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
    print("Sms Pass Count=",SmsPassCnt,",Sms Fail Count=",SmsFailCnt)
    print("MultipleSms Pass Count=",MultiSmsPassCnt,",MultipleSms Fail Count=",MultiSmsFailCnt)
    print("Delete Pass Count=",DeletePassCnt,",Delete Fail Count=",DeleteFailCnt)
    print("Forward Pass count",ForwardPassCnt,"Forward Fail count",ForwardFailCnt)
    print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)
    
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nCalculator_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(SimPassCnt+SimFailCnt)+"\t" + str(SimPassCnt) +"\t"+ str(SimFailCnt)+"\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str(SmsPassCnt+SmsFailCnt)+"\t" + str(SmsPassCnt) +"\t"+ str(SmsFailCnt)+"\n")
    fileobj_logsummary.write(str(DeletePassCnt+DeleteFailCnt)+"\t" + str(DeletePassCnt) +"\t"+ str(DeleteFailCnt)+"\n")
    fileobj_logsummary.write(str(MultiSmsPassCnt+MultiSmsFailCnt)+"\t" + str(MultiSmsPassCnt) +"\t"+ str(MultiSmsFailCnt)+"\n")
    fileobj_logsummary.write(str(ForwardPassCnt+ForwardFailCnt)+"\t" + str(ForwardPassCnt) +"\t"+ str(ForwardFailCnt)+"\n")
    fileobj_logsummary.write(str(KillPassCnt+KillFailCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt)+"\n")
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    SmsPassCnt=0
    SmsFailCnt=0
    MultiSmsPassCnt=0
    MultiSmsFailCnt=0
    DeletePassCnt=0
    DeleteFailCnt=0
    KillPassCnt=0
    KillFailCnt=0
    SimPassCnt=0
    SimFailCnt=0
    
def TestSmsSanity_main():
    print("Entry of TestSmsSanity_main")
    TestSmsSanity_Setup()
    TestSmsSanity_testsuit()
    Sms_sanity_summary_log()
    
    
    