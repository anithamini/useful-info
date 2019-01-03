import os
import re
import time
from sys import argv
Iterations=argv[1]
passcnt = 0
failcnt = 0
wifi_pass_cnt = 0
wifi_fail_cnt = 0

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
 
def launch_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
def toggle_wifi():
    os.system("adb shell input tap 940 368")
def Checkwifistate():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    bt_log = open("wifi_log.txt","r+")
    buffer = bt_log.readline()
    bt_log.close()
    Enabled = re.search('Wi-Fi is enabled', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

def kill_wifi():
    os.system("adb shell am force-stop com.android.settings")

  
for i in range(int(Iterations)):
    if(sim_test()):
        if(Validate()):
            print("Ending the call \n")
            os.system("adb shell input keyevent KEYCODE_ENDCALL")
        else:
            print("No call is in progress...")
        print("Connecting the call to MT_num...\n")
        os.system("adb shell am start -a android.intent.action.CALL -d tel:9100071290")
        time.sleep(2)
        launch_wifi()
        time.sleep(3)
        state = Checkwifistate()
        if state:
            print("wifi enabled")
            toggle_wifi()
            time.sleep(2)
            toggle_wifi()
        else:
            print("wifi disabled")
            toggle_wifi()
        state = Checkwifistate()
        if state:
            print("wifi enabled")
            wifi_pass_cnt+=1            
        else:
            print("wifi disabled")
            wifi_fail_cnt+=1
                        
        time.sleep(5)
        toggle_wifi()
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
        
print("call_Pass count,call_Fail count: ",passcnt,failcnt)
print("wifi_pass_cnt:",wifi_pass_cnt)
print("wifi_fail_cnt:",wifi_fail_cnt)

    
    


    
