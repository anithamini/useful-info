import os
import sys,re
import time,unittest

def on_airpalne():
    os.system("adb shell settings put global airplane_mode_on 1")
    os.system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE")

def off_airplane():
    os.system("adb shell settings put global airplane_mode_on 0")
    os.system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE")

def mo_call_test():
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
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
            #print(line)
            string1="mCallState=2"
            if(string1 in line):
                print("Call already connected and in progress...\n")
                print("Ending the call \n")
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                break
    print("Connecting the call to MT_num...\n")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:8466081316")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    time.sleep(10)
    os.system("adb shell dumpsys telephony.registry > mCallState1.txt")
    time.sleep(5)
    with open("mCallState1.txt", "r+") as fh:
        lines = fh.readlines()
        for line in lines:
            # print(line)
            #print("checking for call status")
            string2 = "mCallState=2"
            if (string2 in line):
                print("Call successfully connected and in progress...\n")
                print("Ending the call \n")
                time.sleep(5)
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                print("Call successfully disconnected ...\n")
                test=1
                #break
                return 1
        else:
            print("Unable to connect the call, so test case is failed")
            return 0    

def mdata_enable():
    os.system("adb shell svc data enable")
    os.system( "adb shell dumpsys telephony.registry > mdata_log.txt")
    mdata_log=open("mdata_log.txt","r+")
    buffer=mdata_log.read()
    mdata_log.close()
    enabled=re.search(" mDataConnectionState=2",buffer,re.I)
    print enabled
    if(enabled):
        print("Data is enabled...\n")
        return (True)
    else:
        return (False)
        

        

def mdata_test():
    state=mdata_enable()
    print state
    if not state:
        os.system("adb shell getprop >gsm1.txt ")        
        gsm1_log=open("gsm1.txt","r+")
        buffer=gsm1_log.read()
        print buffer
        gsm1_log.close()
        str1="[persist.radio.airmode_sim0]: [true]"
        if str1 in buffer:
            print("airplane mode is on so mobile data is offed...\n")
        else:
            print("normally disabled the data...\n")
            
            

#to check call and mobile data working or not when airplane mode is on
on_airpalne()
time.sleep(5)
mo_call_test()
mdata_test()
time.sleep(5)
#to check call and mobile data working or not when airplane mode is off
off_airplane()
mo_call_test()
time.sleep(5)
mdata_test()

