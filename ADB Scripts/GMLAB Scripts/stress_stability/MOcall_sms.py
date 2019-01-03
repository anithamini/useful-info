import os
import time
from sys import argv
Iterations=argv[1]
passcnt = 0
failcnt = 0
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
                return(True)
        else:
                return(False)
def Validate():
    os.system( "adb shell dumpsys telephony.registry > mCallState.txt")
    time.sleep(5)
    with open("mCallState.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="mCallState=2"
            if(string1 in line):
                print("Call already connected and in progress...\n")
                return(True)
        return(False)   
def page_open():
    os.system("adb shell monkey -p com.google.android.apps.messaging 1")
def page_kill():
    os.system("adb shell am force-stop com.google.android.apps.messaging")
def sending():
    os.system("adb shell input tap 958 1096")
    for i in range(0,2):
        os.system("adb shell input keyevent 4")
def sms():
    page_kill()
    time.sleep(2)
    page_open()
    time.sleep(2)
    os.system("adb shell input tap 910 1880")
    os.system("adb shell input text 9100205456")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input text HaiTesting.....")
    sending()
    
for i in range(int(Iterations)):
    if(sim_test()):
        if(Validate()):
            print("Ending the call \n")
            os.system("adb shell input keyevent KEYCODE_ENDCALL")
        else:
            print("No call is in progress...")
        print("Connecting the call to MT_num...\n")
        os.system("adb shell am start -a android.intent.action.CALL -d tel:9100071290")
        sms()
        #os.system("adb shell input tap 536 1290")
        if(Validate()):
            print("Call successfully connected and in progress...")
            passcnt+=1
            time.sleep(2)
            print("Ending the call \n")
            os.system("adb shell input keyevent KEYCODE_ENDCALL")
            print("Call successfully disconnected ...")
        else:
            failcnt+=1   
    else:
        print("SIM not present...unable to make a call...")
        failcnt+=1
        
print("Pass count,Fail count: ",passcnt,failcnt)
    
    


    
