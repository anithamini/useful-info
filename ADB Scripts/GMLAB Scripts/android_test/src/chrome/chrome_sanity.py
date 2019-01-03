'''
Created on Jul 24, 2018

@author: akesiboyina
'''
import os
import time
from common import constants
pass_cnt=0
fail_cnt=0
LaunchPassCnt=0
LaunchFailCnt=0
KillPassCnt=0
KillFailCnt=0

print("------------Chrome Application-------------")

def kill_chrome():
    os.system("adb shell am force-stop com.android.chrome")

def Validate(s1,n):
    os.system( "adb shell dumpsys activity > chrome.txt")
    with open("chrome.txt","r") as fh:
            buff=fh.read()
            if(n=="Chrome"):
                if(s1 in buff):
                    return(True)
                else:
                    return(False)
            if(n=="KillChrome"):
                if(s1 in buff):
                    return(False)
                else:
                    return(True)
            
def launch_chrome():
    os.system("adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity")
    time.sleep(5)
    
def browse_websites(i):
    os.system("adb shell input tap 867 195")
    os.system("adb shell input tap 79 183")
    os.system("adb shell input keyevent 84")
    if i==0:
        os.system("adb shell input text amazon ")
        print("opening browser1...........")
    elif i==1:
        os.system("adb shell input text www.gmail.com")
        print("opening browser2...........")
    else:
        os.system("adb shell input text www.innominds.com")
        print("opening browser3...........")
    os.system("adb shell input keyevent 66")
    time.sleep(5)

def TestchromeSanity_Setup():
     
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nchrome_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
        
def TestchromeSanity_testsuit():
    global pass_cnt
    global fail_cnt
    global LaunchPassCnt
    global LaunchFailCnt
    global KillPassCnt
    global KillFailCnt
    global fileobj_logfile
    kill_chrome()
    if(Validate("packageName=com.android.chrome processName=com.android.chrome","KillChrome")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "Kill_chrome"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "kill_chrome"+"\t"+"FAIL\n")
        KillFailCnt+=1
    launch_chrome()
    if(Validate("packageName=com.android.chrome processName=com.android.chrome","Chrome")):

        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "Launch_chrome"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "Launch_chrome"+"\t"+"FAIL\n")
        LaunchFailCnt+=1
    for n in range(0,3):
        browse_websites(n)
        time.sleep(5)
        if(Validate("realActivity=com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity","Chrome")):
            fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
            fileobj_logfile.write("TC_3" +"\t"+ "browse_websites"+"\t"+"PASS\n")
            pass_cnt+=1
        else:
            fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
            fileobj_logfile.write("TC_3" +"\t"+ "browse_websites"+"\t"+"FAIL\n")
            fail_cnt+=1
            print("unable to browse in chrome...")
        
    os.system("adb shell input keyevent 3")

def chrome_sanity_summary_log():
    global pass_cnt
    global fail_cnt
    global LaunchPassCnt
    global LaunchFailCnt
    global KillPassCnt
    global KillFailCnt
    print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
    print("Browse Pass Count:",pass_cnt,",Fail Count:",fail_cnt)
    print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)

    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    global fileobj_logsummary
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nchrome_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(pass_cnt+fail_cnt)+"\t" + str(pass_cnt) +"\t"+ str(fail_cnt)+"\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str(KillPassCnt+KillFailCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    pass_cnt=0
    fail_cnt=0

def TestChromeSanity_main():
   
    print("entry of TestchromeSanity_main")
    TestchromeSanity_Setup()
    TestchromeSanity_testsuit()
    chrome_sanity_summary_log()

