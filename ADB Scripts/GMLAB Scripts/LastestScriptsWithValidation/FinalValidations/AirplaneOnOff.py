
import os
import time
import sys
Iterations=1#sys.argv[1]
Pass_cnt=0
Fail_cnt=0
LaunchPassCnt=0
LaunchFailCnt=0

print("----------------AIRPLANE MODE(ON/OFF)---------")

def CheckAPMState():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    fd=open("wifi_log.txt","r+")
    buf = fd.read()
    s1='mAirplaneModeOn true'
    if(s1 in buf):
        return(True)
    else:
        return(False)

def LaunchAPMPageValidate():
    os.system( "adb shell dumpsys activity > APM.txt")
    with open("APM.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1="realActivity=com.android.settings/.Settings$NetworkDashboardActivity"
            if(s1 in line):
                return(True)
        return(False)
    
def LAUNCH_APM():
    os.system( "adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    time.sleep(2)
def Toggle_APM():
    os.system("adb shell input tap 466 1521")
    time.sleep(5)
    
LAUNCH_APM()
if(LaunchAPMPageValidate()):
    LaunchPassCnt+=1
    for i in range(int(Iterations)):
    if(CheckAPMState()):
        print("APM already enabled...disabling APM")
        Toggle_APM()
    print("APM disabled and enabling APM")
    Toggle_APM()
    time.sleep(5)    
    if(CheckAPMState()):
        print("APM enabled")
        Pass_cnt+=1
    else:
        print("APM disabled")
        Fail_cnt+=1            
else:
    LaunchFailCnt+=1
    print("unable to open Network settings page,so operations not performed")
time.sleep(5)
if(CheckAPMState()):
    Toggle_APM()


print("Pass cnt=",Pass_cnt)
print("Fail cnt=",Fail_cnt)
print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
        

