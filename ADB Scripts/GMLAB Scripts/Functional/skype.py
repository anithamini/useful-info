import os
import sys
import time
import re
iterations=1#sys.argv[1]
pass_cnt=0
fail_cnt=0
LaunchPassCnt=0
LaunchFailCnt=0
def skype_launch():
    print("...........Launching the Skype Application.................")
    os.system("adb shell am start -n com.skype.raider/.Main")

def Validate(s1):
        os.system("adb shell dumpsys activity > skype.txt")
        with open("skype.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if(s1 in buf):
                                return(True)
                       
                return(False)     


def skype_kill():
    print("..............Killing the Skype Application................")
    os.system("adb shell am force-stop com.skype.raider")
    
def sim_test():
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
                return 1
        else:
                print("sim not present, please insert the sim and start the test")
                return 0

def switch_mobiledata():
    os.system("adb shell svc data enable")
    time.sleep(3)

def mobiledata_off():
    os.system("adb shell svc data disable")
    time.sleep(1)

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

def skype_chat():
    os.system("adb shell input tap 912 171")
    os.system("adb shell input text 'S Dut'")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    #===============intiating the chat============================
    os.system("adb shell input tap 244 1944")
    os.system("adb shell input text 'hello'")
    time.sleep(3)
    os.system("adb shell input tap 1021 1186")
    os.system("adb shell input keyevent 4")
    #===============intiating a video call=========================
    os.system("adb shell input tap 849 160")
    time.sleep(10)
    os.system("adb shell input tap 977 1903")

for i in range(int(iterations)):
    skype_kill()
    res=sim_test()
    if res:
        print("sim is present")
        pre=checkmobiledata()
        if pre:
            pass_cnt+=1
            print("mobile data on")
            time.sleep(7)
            skype_launch()
            if(Validate("packageName=com.skype.raider processName=com.skype.raider")):
                LaunchPassCnt+=1
            else:
                LaunchFailCnt+=1
            time.sleep(10)
            skype_chat()
            skype_kill()
        else:
            switch_mobiledata()
            pre=checkmobiledata()
            if pre:
                pass_cnt+=1
                print("mobile data on")
                time.sleep(7)
                skype_launch()
                time.sleep(10)
                skype_chat()
                skype_kill()
            else:
                fail_cnt+=1
print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
print("Data pass_cnt:",pass_cnt,",Data Fail Count:",fail_cnt)
            

        
