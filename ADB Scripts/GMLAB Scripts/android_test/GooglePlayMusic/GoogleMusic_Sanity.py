'''
Created on Jul 24, 2018

@author: hnagella
'''

import os
from time import sleep
from common import constants
LaunchPassCnt=0
LaunchFailCnt=0
PlayPassCnt=0
PlayFailCnt=0
PausePassCnt=0
PauseFailCnt=0

def Validate(s1,s2):
    os.system("adb shell dumpsys "+s2+" > googleplay.txt")                                             #For collecting activity logs
    with open("googleplay.txt","r") as fh:
        while 1:
            buf=fh.readline()
            if (buf==""):
                break
            if(s1 in buf):
                return(True)
            
def KillGoogleMusic():
    os.system("adb shell am force-stop com.google.android.music")                                   #For killing Google Music Application
    sleep(2)
    
def LaunchGoogleMusic():
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logfile
    KillGoogleMusic()
    os.system("adb shell monkey -p com.google.android.music -c android.intent.category.LAUNCHER  1")       #For Launching GooglePlayMusic Application
    sleep(3)
    if(Validate("packageName=com.google.android.packageinstaller processName=com.google.android.packageinstaller","activity")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchGoogleMusic"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchGoogleMusic"+"\t"+"PASS\n")
        LaunchFailCnt+=1
                       
def PlayGoogleMusic():
    global PlayPassCnt
    global PlayFailCnt
    global fileobj_logfile
    os.system("adb shell input keyevent 20")                                                                #For keypad down
    os.system("adb shell input keyevent 66")                                                                #For tapping the song
    sleep(5)
    if(Validate("state:started -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayGoogleMusic"+"\t"+"PASS\n")
        PlayPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayGoogleMusic"+"\t"+"PASS\n")
        PlayFailCnt+=1

def PauseGoogleMusic():
    global PausePassCnt
    global PauseFailCnt
    global fileobj_logfile
    os.system("adb shell input keyevent 85")                                                                    #To pause the Music
    sleep(5)
    if(Validate("state:paused -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseGoogleMusic"+"\t"+"PASS\n")
        PausePassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseGoogleMusic"+"\t"+"PASS\n")
        PauseFailCnt+=1
    sleep(2)
    KillGoogleMusic()
    
def TestGoogleMusicSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nGoogleMusic_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestGoogleMusicSanity_testsuit():
    LaunchGoogleMusic()
    PlayGoogleMusic()  
    PauseGoogleMusic()

def GoogleMusic_sanity_summary_log():
    global LaunchPassCnt
    global LaunchFailCnt
    global PlayPassCnt
    global PlayFailCnt
    global PausePassCnt
    global PauseFailCnt
    global fileobj_logsummary
    print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
    print("Play Pass Count=",PlayPassCnt,",PlayFail Count=",PlayFailCnt)
    print("Pause Pass Count=",PausePassCnt,",Pause Fail Count=",PauseFailCnt)

    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nGoogleMusic_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt))
    fileobj_logsummary.write(str(PlayPassCnt+PlayFailCnt)+"\t" + str(PlayPassCnt) +"\t"+ str(PlayFailCnt))
    fileobj_logsummary.write(str(PausePassCnt+PauseFailCnt)+"\t" + str(PausePassCnt) +"\t"+ str(PauseFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    PlayPassCnt=0
    PlayFailCnt=0
    PausePassCnt=0
    PauseFailCnt=0
    
def TestGoogleSanity_main():
    print("Entry of TestGoogleMusicSanity_main")
    TestGoogleMusicSanity_Setup()
    TestGoogleMusicSanity_testsuit()
    GoogleMusic_sanity_summary_log()
