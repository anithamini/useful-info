

##check airplane mode on/off if enable code will check the sim status and make a call to ref and send a sms to ref.#




import os
import sys
import time
import re
import unittest,time 
print("***********************************************************************")
print("Airplane mode enable disable test started")
print("***********************************************************************")
n=2
count=n
pass_TC = 0
fail_TC = 0
print("Iterations:",n)
def Checkbtstate():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    air_log = open("wifi_log.txt","r+")
    buffer = air_log.readline();
    air_log.close()
    Enabled = re.search('mAirplaneModeOn false', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

    
def Toggle_bt():
    os.system( "adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    os.system( "adb shell input tap 346 438")
    os.system( "adb shell input keyevent 66")
    time.sleep(5)
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
                break
        else:
            print("sim not present, please insert the sim and start the test")
    os.system("adb wait-for-device shell input keyevent 82")
    os.system("adb wait-for-device shell input keyevent 3")
    os.system( "adb shell dumpsys telephony.registry > mCallState.txt")
    time.sleep(5)
    with open("mCallState.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="mCallState=2"
            if(string1 in line):
                print("Call already connected and in progress...\n")
                print("Ending the call \n")
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                break
    print("Connecting the call to MT_num...\n")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9159495244")
    time.sleep(10)
    os.system("adb shell dumpsys telephony.registry > mCallState1.txt")
    time.sleep(5)
    with open("mCallState1.txt", "r+") as fh:
        lines = fh.readlines()
        for line in lines:
            string2 = "mCallState=2"
            if (string2 in line):
                print("Call successfully connected and in progress...\n")
                print("Ending the call \n")
                time.sleep(10)
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                print("Call successfully disconnected ...\n")
                test=1
                time.sleep(10)
                print("***********************************************************************")
                print("sending message")
                print("***********************************************************************")
                os.system("adb shell am start -a android.intent.action.SENDTO -d sms:+919159495244 --es sms_body 'hi dis is yoga' --ez exit_on_sent true")
                os.system("adb shell input keyevent 22")
                os.system("adb shell input keyevent 66")
                os.system("adb shell input keyevent 3")
                return 1
        else:
            print("Unable to connect the call, so test case is failed")
            return 0
state = Checkbtstate()
print(state)# if apn is off print false if apn is on then print true
if (state==0):
    print("airplane mode is enable so we can't make a call \n")
    print ("still checking dut can make a call \n")
print("airplane mode is disable we can make call \n")    
while(count!=0):
        print("--------------------------------")



        #n=n+1
        x=Toggle_bt()
        if(x==1):
            pass_TC += 1
            print("Test case = PASS ...\n") 
            print("--------------------------------")
        else:
            fail_TC += 1
            ("Test case = FAIL ...\n")
            print("--------------------------------")
        count=count-1
print ("--------------------------------")
print ("Total NO.OF Iterations ran : " , n-1)
print ("Total NO.OF iterations Passed: %d" %pass_TC)
print ("Total NO.OF iterations Failed: %d" %fail_TC)
