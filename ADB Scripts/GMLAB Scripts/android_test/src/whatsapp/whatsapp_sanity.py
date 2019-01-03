'''
Created on Jul 24, 2018

@author: akesiboyina
'''
import os
import time
from common import constants
launch_pass_cnt=0
launch_fail_cnt=0
msg_pass_cnt=0
msg_fail_cnt=0
voice_fail_cnt=0
voice_pass_cnt=0
video_fail_cnt=0
video_pass_cnt=0
i=0

print("-------------Whatsapp Application--------")

def checkmobiledata():
    os.system("adb shell getprop>mobiledata.txt")
    fp=open("mobiledata.txt","r+")
    buff=fp.read()
    str1="[gsm.defaultpdpcontext.active]: [true]"
    if str1 in buff:
        print(str1)
        return 1
    else:
        return 0
    
def Kill_whatsapp():
    print("-----------killing background process of whatsapp--------")
    os.system( "adb shell am force-stop com.whatsapp")          
def Launch_whatsapp():
    global launch_pass_cnt
    global launch_fail_cnt
    global fileobj_logfile
    print("-----------Launching whatsapp to foreground--------------")
    os.system( "adb shell am start -n com.whatsapp/.Main")
    if(validate("packageName=com.whatsapp processName=com.whatsapp")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "launch_whatsapp"+"\t"+"PASS\n")
        launch_pass_cnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "launch_whatsapp"+"\t"+"FAIL\n")
        launch_fail_cnt+=1    

def search_contact():
    os.system("adb shell input tap 925 1837")    #tapping to make new chat
    os.system("adb shell input keyevent 84")     #for search
    os.system("adb shell input text Hdut")       #for entering contact as Hdut

def message_whatsapp():
    global msg_pass_cnt
    global msg_fail_cnt
    global fileobj_logfile
    print("-----------sending message in whatsapp--------------") 
    search_contact()
    os.system("adb shell input tap 532 352")             #for tapping on Hdut contact
    os.system("adb shell input text helloooooooo")       #for entering text
    os.system("adb shell input tap 992 1212")            #for tapping on send button
    for i in range(0,2):
        os.system("adb shell input keyevent 4")          #to move back
    if(validate("realActivity=com.whatsapp/.Conversation")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "message_whatsapp"+"\t"+"PASS\n")
        msg_pass_cnt+=1   
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "message_whatsapp"+"\t"+"FAIL\n")
        msg_fail_cnt+=1
    time.sleep(5)   
               
def audiocall_whatsapp():
    global voice_fail_cnt
    global voice_pass_cnt
    global fileobj_logfile
    print("-----------making whatsapp audiocall--------------")
    for i in range(0,4):
        os.system("adb shell input keyevent 22")   #to move rightside
    search_contact()
    os.system("adb shell input tap 814 329")       # to tap on audiocall option
    time.sleep(4)
         #to end audiocall
    if(validate('label="Voice Call"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "audiocall_whatsapp"+"\t"+"PASS\n")
        voice_pass_cnt+=1 
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "audiocall_whatsapp"+"\t"+"FAIL\n")
        voice_fail_cnt+=1   
    os.system("adb shell input tap 516 1564") 
    time.sleep(5)
    
def videocall_whatsapp():
    global video_fail_cnt
    global video_pass_cnt
    global fileobj_logfile
    print("-----------making whatsapp videocall--------------")
    search_contact()
    os.system("adb shell input tap 926 322")        #to tap on videocall option
    time.sleep(10)
    if(validate('label="Video Call"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "videocall_whatsapp"+"\t"+"PASS\n")
        video_pass_cnt+=1
        
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "videocall_whatsapp"+"\t"+"FAIL\n")
        video_fail_cnt+=1
    end_call()
    os.system( "adb shell am force-stop com.whatsapp") 
          
def end_call():
    print("-----------ending whatsapp videocall--------------")
    os.system("adb shell input tap 368 956")                          #to end videocall

def validate(s1):
    os.system("adb shell dumpsys activity >what.txt")
    with open("what.txt","r+") as fh:
        buf=fh.read() 
        if s1 in buf:
            return 1
        else:
            return 0
    
    
def TestWhatsappSanity_Setup():
     
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nWhatsapp_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    if(checkmobiledata()):
        print("mobile data is on....proceed the test")
    else:   
        os.system("adb shell svc data enable")        #enabling mobiledata
        time.sleep(2)
        
def TestWhatsappSanity_testsuit(): 
    Kill_whatsapp()
    Launch_whatsapp()
    message_whatsapp()
    audiocall_whatsapp()
    videocall_whatsapp()

def Whatsapp_sanity_summary_log():
    global launch_pass_cnt
    global launch_fail_cnt
    global msg_pass_cnt
    global msg_fail_cnt
    global voice_fail_cnt
    global voice_pass_cnt
    global video_fail_cnt
    global video_pass_cnt
    global fileobj_logfile
    
    print("Launch Pass Count=",launch_pass_cnt,",Launch Fail Count=",launch_fail_cnt)
    print("Message Pass Count=",msg_pass_cnt,",Message Fail Count=",msg_fail_cnt)
    print("Voice Pass Count=",voice_pass_cnt,",Voice Fail Count=",voice_fail_cnt)
    print("Video Pass Count=",video_pass_cnt,",Video Fail Count=",video_fail_cnt)

    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    global fileobj_logsummary
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nwhatsapp_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(launch_pass_cnt+launch_fail_cnt)+"\t" + str(launch_pass_cnt) +"\t"+ str(launch_fail_cnt)+"\n")
    fileobj_logsummary.write(str(msg_pass_cnt+msg_fail_cnt)+"\t" + str(msg_pass_cnt) +"\t"+ str(msg_fail_cnt)+"\n")
    fileobj_logsummary.write(str(voice_pass_cnt+voice_fail_cnt)+"\t" + str(voice_pass_cnt) +"\t"+ str(voice_fail_cnt)+"\n")
    fileobj_logsummary.write(str(video_pass_cnt+video_fail_cnt)+"\t" + str(video_pass_cnt) +"\t"+ str(video_fail_cnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    launch_pass_cnt=0
    launch_fail_cnt=0
    msg_pass_cnt=0
    msg_fail_cnt=0
    voice_fail_cnt=0
    voice_pass_cnt=0
    video_fail_cnt=0
    video_pass_cnt=0

    
def TestWhatsappSanity_main():
   
    print("entry of TestWhatsappSanity_main")
    TestWhatsappSanity_Setup()
    TestWhatsappSanity_testsuit()
    Whatsapp_sanity_summary_log()







