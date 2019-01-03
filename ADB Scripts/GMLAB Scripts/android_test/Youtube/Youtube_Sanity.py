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
i=0

def Validate(s1,s2):
    os.system("adb shell dumpsys "+s2+" > youtube.txt")                                             #For collecting activity logs
    with open("youtube.txt","r") as fh:
        while 1:
            buf=fh.readline()
            if (buf==""):
                break
            if(s1 in buf):
                return(True)

def KillYoutube():
    os.system("adb shell am force-stop com.google.android.youtube")                                   #For killing Youtube Application
    sleep(2)

def LaunchYoutube():
    KillYoutube()
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logfile
    os.system("adb shell monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1")       #For Launching Youtube Application
    sleep(5)
    if(Validate("packageName=com.google.android.youtube processName=com.google.android.youtube","activity")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchYoutube"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestLaunchYoutube"+"\t"+"PASS\n")
        LaunchFailCnt+=1
   
def PlayVideo():
    global PlayPassCnt
    global PlayFailCnt
    global i
    global fileobj_logfile
    os.system("adb shell input keyevent 84")                                                                #For searching
    os.system("adb shell input text dhee%s10")                                                              #To type text as "dhee 10"
    for i in range(0,2):
        os.system("adb shell input keyevent 66")                                                            #For enter
        sleep(5)
    if(Validate("state:started -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x200 tags= bundle=null","audio")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayYoutube"+"\t"+"PASS\n")
        PlayPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestPlayYoutube"+"\t"+"PASS\n")
        PlayFailCnt+=1
    sleep(3)
      
def PauseVideo():
    global PausePassCnt
    global PauseFailCnt
    global fileobj_logfile
    os.system("adb shell input keyevent 85")                                                                    #To pause the Video
    sleep(5)
    if(Validate("state:paused -- attr:AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x0 tags= bundle=null","audio")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseYoutube"+"\t"+"PASS\n")
        PausePassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_3" +"\t"+ "TestPauseYoutube"+"\t"+"PASS\n")
        PauseFailCnt+=1
    sleep(3)
    KillYoutube()

def TestYoutubeSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nYoutube_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestYoutubeSanity_testsuit():
    LaunchYoutube()
    PlayVideo()  
    PauseVideo()

def Youtube_sanity_summary_log():
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
    fileobj_logsummary.write("\nYoutube_sanity\n")
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
    print("Entry of TestYoutubeSanity_main")
    TestYoutubeSanity_Setup()
    TestYoutubeSanity_testsuit()
    Youtube_sanity_summary_log()







