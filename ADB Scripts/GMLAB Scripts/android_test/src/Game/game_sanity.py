'''
Created on Jul 24, 2018

@author: hnagella
'''
import os
from time import sleep
from common import constants
LaunchPassCnt=0
LaunchFailCnt=0
KillPassCnt=0
KillFailCnt=0
PlayPassCnt=0
PlayFailCnt=0
i=0

def validate(s1,s2):
    os.system('adb shell dumpsys '+s2+' > game.txt')                                                 #For collecting activity logs
    with open("game.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            if(s1 in line):
                return(True)
        return(False)

def KillGame():
    global KillPassCnt
    global KillFailCnt
    global fileobj_logsummary
    os.system("adb shell am force-stop com.imangi.templerun")                                               #For killing the temple run apllication
    sleep(2)
    if(validate("I=com.android.launcher3/com.android.searchlauncher.SearchLauncher",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillGame"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillGame"+"\t"+"FAIL\n")
        KillFailCnt+=1

def LaunchGame():
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logsummary
    os.system("adb shell monkey -p com.imangi.templerun -c android.intent.category.LAUNCHER 1")             #For launching the Temple Run application
    sleep(20)
    if(validate("A=com.imangi.templerun",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchGame"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchGame"+"\t"+"FAIL\n")
        LaunchFailCnt+=1
def playvalidate():
    os.system("adb shell dumpsys activity > game1.txt")                                                 #For collecting activity logs
    with open("game1.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            if(("mLastPausedActivity: ActivityRecord" in line) and ("com.imangi.templerun/com.imangi.unityactivity.ImangiUnityNativeActivity" in line)):
                return(True)
        return(False)
def PlayGame():
    global PlayPassCnt
    global PlayFailCnt
    global fileobj_logsummary
    global i
    os.system("adb shell input tap 485 1448")                                                               #For tapping Play icon
    for i in range(1,9):
        print("...running...running...")
        sleep(1)
    print("....falling....")
    if(playvalidate()):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPlayGame"+"\t"+"PASS\n")
        PlayPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPlayGame"+"\t"+"FAIL\n")
        PlayFailCnt+=1
    os.system("adb shell am force-stop com.imangi.templerun")
    
def TestGameSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nGame_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestGameSanity_testsuit(): 
    KillGame()
    LaunchGame()
    PlayGame()

def Game_sanity_summary_log():
    global LaunchPassCnt
    global LaunchFailCnt
    global KillPassCnt
    global KillFailCnt
    global PlayPassCnt
    global PlayFailCnt
    global fileobj_logsummary
    print("PlayPassCnt:",LaunchPassCnt)
    print("PlayFailCnt",LaunchFailCnt)
    print("PlayPassCnt:",KillPassCnt)
    print("PlayFailCnt",KillFailCnt)
    print("PlayPassCnt:",PlayPassCnt)
    print("PlayFailCnt",PlayFailCnt)
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nGame_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str(KillFailCnt+KillPassCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt)+"\n")
    fileobj_logsummary.write(str(PlayPassCnt+PlayFailCnt)+"\t" + str(PlayPassCnt) +"\t"+ str(PlayFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    KillPassCnt=0
    KillFailCnt=0
    PlayPassCnt=0
    PlayFailCnt=0
    
def TestGameSanity_main():
    print("Entry of TestCalculatorSanity_main")
    TestGameSanity_Setup()
    TestGameSanity_testsuit()
    Game_sanity_summary_log()

