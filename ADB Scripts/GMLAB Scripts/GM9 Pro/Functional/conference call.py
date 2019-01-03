import os
import time
import sys
import re

def mo_call_test():
    os.system("adb shell getprop> gsm.txt ")
    time.sleep(3)
    fh=open("gsm.txt","r") 
    lines=fh.read()
    #print(lines)
    pass_cnt=0
    fh.close()   
    e1="[DEVICE_PROVISIONED]: [1]"
    print(e1)
    e2="[gsm.sim.state]: [READY,NOT_READY]"
    print(e2)
    e3="[gsm.sim.state]: [NOT_READY,READY]"
    e4="[gsm.sim.state]: [ABSENT,READY]"
    e5="[gsm.sim.state]: [READY,ABSENT]"
    e6="[gsm.sim.state]: [READY,READY]"
    print(e5)
    if(e1 in lines or e2 in lines  or e3 in lines  or e4 in lines  or e5 in lines or e6 in lines):
        print("sim prsent,proceed the test")
    else:
        print("sim not present, please insert the sim and start the test")
        return
    print("Connecting the call to MT_num...\n")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9704708710")
    #time.sleep(10)
    cnt=0
    while 1:
        os.system("adb shell dumpsys telephony.registry > mCallState1.txt")
        fh=open("mCallState1.txt", "r+")
        string2 ="mForegroundCallState=1"
        buf = fh.read()
        if (string2 in buf):
            print("ppd")
            cnt=1
            break;
        fh.close()
        if cnt==1:
            break
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9159495244")
    time.sleep(2)
    while 1:
        os.system("adb shell dumpsys telephony.registry > mCallState2.txt")
        fp=open("mCallState2.txt", "r")
        string ="mForegroundCallState=1"
        string3 ="mBackgroundCallState=2"
        buf = fp.read()
        if ((string in buf)):
            print("ppd")
            cnt=2
            pass_cnt+=1
            break;
        fp.close()
        if cnt==2:
            break
    os.system("adb shell input tap 200 1300")
    return pass_cnt
print("in main")
k=mo_call_test()
if(k):
    print("test pass_cnt",k)
else:
    print("test failed")
    
