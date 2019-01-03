
import os
import time
import sys
Iterations=sys.argv[1]
Pass_cnt=0
Fail_cnt=0

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

def CheckAPMState():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    fd=open("wifi_log.txt","r+")
    buf = fd.read()
    s1='mAirplaneModeOn true'
    if(s1 in buf):
        return(True)
    else:
        return(False)
    
def LAUNCH_APM():
    os.system( "adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")

def Toggle_APM():
    LAUNCH_APM()
    os.system("adb shell input tap 466 1521")
    time.sleep(5)
    

for i in range(int(Iterations)):
    if(CheckAPMState()==False):
        Toggle_APM()
        print("Just now APM enabled...")
    print("APM already enabled...disabling APM")
    if(sim_test()):
        print("Connecting the call to MT_num...\n")
        os.system("adb shell am start -a android.intent.action.CALL -d tel:9100071290")
        time.sleep(3)
        if(Validate()):
            Fail_cnt+=1
        else:
            Pass_cnt+=1
        Toggle_APM()
if(CheckAPMState()):
    Toggle_APM()
print("Pass cnt=",Pass_cnt)
print("Fail cnt=",Fail_cnt)

        



