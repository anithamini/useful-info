import os
import time

def LaunchValidate(s1):
        os.system("adb shell dumpsys activity > SmsLaunch.txt")
        with open("SmsLaunch.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if(s1 in buf):
                                return(True)
                       

def sim_test():
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
                return 1
        else:
                print("sim not present, please insert the sim and start the test")
                return 0
                
def sending():
    os.system("adb shell input tap 958 1096")
    time.sleep(3)
    for i in range(0,2):
        os.system("adb shell input keyevent 4")

def page_open():
    os.system("adb shell monkey -p com.google.android.apps.messaging 1")

def page_kill():
    os.system("adb shell am force-stop com.google.android.apps.messaging")
    
def f():
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    
def Forward_sms():
    page_open()
    os.system("adb shell input tap 447 396")
    os.system("adb shell input touchscreen swipe 930 1670 930 1670 1000")
    os.system("adb shell input tap 513 155")
    for i in range(0,2):
        os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 950 1870")
    for i in range(0,2):
        os.system("adb shell input keyevent 4")
    
    
def delete_multipleConversations():
    time.sleep(2)
    page_open()
    num1=250
    num2=380
    
    for i in range(0,3):
        os.system("adb shell input touchscreen swipe "+str(num1)+" "+str(num2)+" "+str(num1)+" "+str(num2)+" "+str(1000))
        num1+=100
        num2+=300
    time.sleep(5)
    os.system("adb shell input tap 865 215")
    f()
page_kill()
    if(sim_test()):
        page_open()
        time.sleep(2)
        if(LaunchValidate("packageName=com.google.android.apps.messaging processName=com.google.android.apps.messaging")):
            LaunchPassCnt+=1
        else:
            LaunchFailCnt+=1
        #print("sending SMS to a contact")
        sms()
        if(SmsValidate()==n+1):
            SmsPassCnt+=1
        else:
            SmsFailCnt+=1
        print("sending SMS to multiple contacts")
        sms_multiplepeople()
        n=i*4
        if(SmsValidate()==n):
            MultiSmsPassCnt+=1
        else:
            MultiSmsFailCnt+=1
print("Launch Pass Count=",LaunchPassCnt,",Launch Fail Count=",LaunchFailCnt)
print("SMS Pass Count=",SmsPassCnt,",SMS Fail Count=",SmsFailCnt)
print("MultiSMS Pass Count=",MultiSmsPassCnt,",MultiSMS Fail Count=",MultiSmsFailCnt)


"""
	    print("sending SMS to multiple contacts")
	    sms_multiplepeople()
	    print("forwarding SMS to a contact")
	    Forward_sms()
	    print("Deleting one conversation")
	    Delete_sms()
	    print("Deleting Multiple convesations")
	    delete_multipleConversations()
	    os.system("adb shell input keyevent 4")	
	    pass_cnt+=1
	else:
	    print("sim is not present.....unable to perform operations")
	    fail_cnt+=1




ProcessPendingMessagesAction: cleared next retry time for channel sms_send
ProcessSentMessageAction: Done sending SMS message
ProcessPendingMessagesAction: process from ProcessSentMessageAction due to sms_send success with queues:
"""    
