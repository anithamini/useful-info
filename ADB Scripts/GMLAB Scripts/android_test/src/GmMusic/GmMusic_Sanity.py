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
    os.system("adb shell dumpsys "+s2+" > gmmusic.txt")                                             #For collecting activity logs
    with open("gmmusic.txt","r") as fh:
        while 1:
            buf=fh.readline()
            if (buf==""):
                break
            if(s1 in buf):
                return(True)

def KillGmMusic():
    os.system("adb shell am force-stop com.generalmobile.app.musicplayer")                          #For killing GM Music Application
    sleep(2)

def LaunchGmMusic():
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logfile
    KillGmMusic()
    os.system("adb shell monkey -p com.generalmobile.app.musicplayer -c android.intent.category.LAUNCHER  1")       #For Launching GmMusic Application
    sleep(3)
    if(Validate("packageName=com.generalmobile.app.musicplayer processName=com.generalmobile.app.musicplayer","activity")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchGmMusic"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchGmMusic"+"\t"+"PASS\n")
        LaunchFailCnt+=1
                       
def PlayGmMusic():
    global PlayPassCnt
    global PlayFailCnt
    global fileobj_logfile
    os.system("adb shell input tap 536 1290")                                                                   #To Play the Music 
    sleep(5)
    if(Validate("state:started -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayGmMusic"+"\t"+"PASS\n")
        PlayPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayGmMusic"+"\t"+"PASS\n")
        PlayFailCnt+=1

def PauseGmMusic():
    global PausePassCnt
    global PauseFailCnt
    global fileobj_logfile
    os.system("adb shell input keyevent 85")                                                                    #To pause the Music
    sleep(2)
    if(Validate("state:paused -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseGmMusic"+"\t"+"PASS\n")
        PausePassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseGmMusic"+"\t"+"PASS\n")
        PauseFailCnt+=1
    sleep(2)
    KillGmMusic()
    
def TestGmMusicSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nGmMusic_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestGmMusicSanity_testsuit():
    LaunchGmMusic()
    PlayGmMusic()  
    PauseGmMusic()

def GmMusic_sanity_summary_log():
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
    fileobj_logsummary.write("\nGmMusic_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt))
    fileobj_logsummary.write(str(PlayPassCnt+PlayFailCnt)+"\t" + str(PlayPassCnt) +"\t"+ str(PlayFailCnt))
    fileobj_logsummary.write(str(PausePassCnt+PauseFailCnt)+"\t" + str(PausePassCnt) +"\t"+ str(PauseFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    #LaunchPassCnt=0
    #LaunchFailCnt=0
    #PlayPassCnt=0
    #PlayFailCnt=0
    #PausePassCnt=0
    #PauseFailCnt=0
    
def TestGmMusicSanity_main():
    print("Entry of TestGmMusicSanity_main")
    TestGmMusicSanity_Setup()
    TestGmMusicSanity_testsuit()
    GmMusic_sanity_summary_log()



    

