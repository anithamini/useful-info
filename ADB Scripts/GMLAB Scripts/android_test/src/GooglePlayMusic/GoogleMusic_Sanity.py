'''
Created on Jul 24, 2018

@author: hnagella
'''

import os
from time import sleep
from common import constants
i=0
LaunchPassCnt=0
LaunchFailCnt=0
KillPassCnt=0
KillFailCnt=0
PlayPassCnt=0
PlayFailCnt=0
PausePassCnt=0
PauseFailCnt=0

def Validate(s1,s2):
    os.system('adb shell dumpsys '+s2+' > googleplay.txt')                                             #For collecting activity logs
    with open("googleplay.txt","r") as fh:
        while 1:
            buf=fh.readline()
            if (buf==""):
                break
            if(s1 in buf):
                return(True)
            
def KillGoogleMusic():
    global KillPassCnt
    global KillFailCnt
    global fileobj_logfile
    os.system("adb shell am force-stop com.google.android.music")                                   #For killing Google Music Application
    sleep(2)
    if(Validate("I=com.android.launcher3/com.android.searchlauncher.SearchLauncher",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillGoogleMusic"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillGoogleMusic"+"\t"+"FAIL\n")
        KillFailCnt+=1
    
def LaunchGoogleMusic():
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logfile
    os.system("adb shell monkey -p com.google.android.music -c android.intent.category.LAUNCHER  1")       #For Launching GooglePlayMusic Application
    sleep(3)
    if(Validate("A=com.google.android.music.task",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchGoogleMusic"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchGoogleMusic"+"\t"+"FAIL\n")
        LaunchFailCnt+=1
                       
def PlayGoogleMusic():
    global PlayPassCnt
    global PlayFailCnt
    global fileobj_logfile
    os.system("adb shell input keyevent 85")                                                #To Play the song
    sleep(10)
    if(Validate("state(0), latency (600)",'media.player')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayGoogleMusic"+"\t"+"PASS\n")
        PlayPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayGoogleMusic"+"\t"+"FAIL\n")
        PlayFailCnt+=1

def PauseGoogleMusic():
    global PausePassCnt
    global PauseFailCnt
    global fileobj_logfile
    os.system("adb shell input keyevent 85")                                                                 #To pause the Music
    sleep(5)
    if(Validate("state(2), latency (600)",'media.player')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseGoogleMusic"+"\t"+"PASS\n")
        PausePassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseGoogleMusic"+"\t"+"FAIL\n")
        PauseFailCnt+=1
    sleep(2)
    os.system("adb shell am force-stop com.google.android.music")      
    
def TestGoogleMusicSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nGoogleMusic_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestGoogleMusicSanity_testsuit():
    KillGoogleMusic()
    LaunchGoogleMusic()
    PlayGoogleMusic()  
    PauseGoogleMusic()

def GoogleMusic_sanity_summary_log():
    global LaunchPassCnt
    global LaunchFailCnt
    global KillPassCnt
    global KillFailCnt
    global PlayPassCnt
    global PlayFailCnt
    global PausePassCnt
    global PauseFailCnt
    global fileobj_logsummary
    print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)
    print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
    print("Play Pass Count=",PlayPassCnt,",PlayFail Count=",PlayFailCnt)
    print("Pause Pass Count=",PausePassCnt,",Pause Fail Count=",PauseFailCnt)

    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nGoogleMusic_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(KillPassCnt+KillFailCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt)+"\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str(PlayPassCnt+PlayFailCnt)+"\t" + str(PlayPassCnt) +"\t"+ str(PlayFailCnt)+"\n")
    fileobj_logsummary.write(str(PausePassCnt+PauseFailCnt)+"\t" + str(PausePassCnt) +"\t"+ str(PauseFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    PlayPassCnt=0
    PlayFailCnt=0
    PausePassCnt=0
    PauseFailCnt=0
    KillPassCnt=0
    KillFailCnt=0
    
def TestGoogleSanity_main():
    print("Entry of TestGoogleMusicSanity_main")
    TestGoogleMusicSanity_Setup()
    TestGoogleMusicSanity_testsuit()
    GoogleMusic_sanity_summary_log()
