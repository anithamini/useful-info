import os
import time
import sys
iterations=sys.argv[1]
launch_pass_cnt=0
launch_fail_cnt=0
msg_pass_cnt=0
msg_fail_cnt=0
voice_fail_cnt=0
voice_pass_cnt=0
video_fail_cnt=0
video_pass_cnt=0

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
    print("-----------Launching whatsapp to foreground--------------")
    os.system( "adb shell am start -n com.whatsapp/.Main")

def search_contact():
    os.system("adb shell input tap 925 1837")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text Hdut")

def message_whatsapp():
    print("-----------sending message in whatsapp--------------") 
    search_contact()
    os.system("adb shell input tap 532 352")    
    os.system("adb shell input text helloooooooo")
    os.system("adb shell input tap 992 1212")  
    for i in range(0,2):
        os.system("adb shell input keyevent 4")

def audiocall_whatsapp():
    print("-----------making whatsapp audiocall--------------")
    for i in range(0,4):
        os.system("adb shell input keyevent 22")
    search_contact()
    os.system("adb shell input tap 814 329")
    time.sleep(4)
    os.system("adb shell input tap 516 1564")

def videocall_whatsapp():
    print("-----------making whatsapp videocall--------------")
    search_contact()
    os.system("adb shell input tap 926 322")
    
def end_call():
     print("-----------ending whatsapp videocall--------------")
     os.system("adb shell input tap 368 956")

def validate(s1):
    os.system("adb shell dumpsys activity >what.txt")
    with open("what.txt","r+") as fh:
        buf=fh.read() 
        if s1 in buf:
            return 1
        else:
            return 0
for i in range(int(iterations)):
    Kill_whatsapp()
    if(checkmobiledata()):
        Launch_whatsapp()
        if(validate("packageName=com.whatsapp processName=com.whatsapp")):
            launch_pass_cnt+=1
            message_whatsapp()
            if(validate("realActivity=com.whatsapp/.Conversation")):
                msg_pass_cnt+=1               
                audiocall_whatsapp()
                if(validate('label="Voice Call"')):
                    voice_pass_cnt+=1
                    videocall_whatsapp()
                    time.sleep(10)
                    if(validate('label="Video Call"')):
                        video_pass_cnt+=1
                        end_call()
                    else:
                        video_fail_cnt+=1
                else:
                    voice_fail_cnt+=1
            else:
               msg_fail_cnt+=1
        else:
            launch_fail_cnt+=1

    else:
        print("mobile data is off....unable to proceed")
    Kill_whatsapp()

print("Launch Pass Count=",launch_pass_cnt,",Launch Fail Count=",launch_fail_cnt)
print("Message Pass Count=",msg_pass_cnt,",Message Fail Count=",msg_fail_cnt)
print("Voice Pass Count=",voice_pass_cnt,",Voice Fail Count=",voice_fail_cnt)
print("Video Pass Count=",video_pass_cnt,",Video Fail Count=",video_fail_cnt)





