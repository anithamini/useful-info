import os
import time
pass_cnt=0
fail_cnt=0

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
    Launch_whatsapp()
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
     
Kill_whatsapp()
if(checkmobiledata()):
    message_whatsapp()
    audiocall_whatsapp()
    videocall_whatsapp()
    time.sleep(10)
    end_call()
    pass_cnt+=1
else:
    fail_cnt+=1
    print("mobile data is off")
   
Kill_whatsapp()
print("pass_cnt is:",pass_cnt)
print("fail_cnt is:",fail_cnt)
    
