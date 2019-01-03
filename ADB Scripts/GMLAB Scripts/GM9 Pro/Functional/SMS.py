import os
import time

pass_cnt=0
fail_cnt=0

print("Working with Messages application")

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
    
def sms():
    page_open()
    os.system("adb shell input tap 910 1880")
    os.system("adb shell input text 08466081316")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input text HaiTesting.....")
    sending()

def sms_multiplepeople():
    page_open()
    os.system("adb shell input tap 910 1880")
    list=["8466081316","9640281782","9100205816"]
    for number in list:
        os.system("adb shell input text "+number)
        os.system("adb shell input keyevent 66")
        os.system("adb shell input tap 734 368")
    os.system("adb shell input tap 1008 1939")
    os.system("adb shell input text SMS%sto%sMultiple%scontacts....")
    sending()

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
    
def Delete_sms():
    page_open()
    os.system("adb shell input touchscreen swipe 450 700 450 700 1000")    
    time.sleep(5)
    os.system("adb shell input tap 835 147")
    time.sleep(2)
    f()
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
    print("sending SMS to a contact")
    sms()
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
print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)
