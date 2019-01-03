import os
import time
def kill_simsettings():
    os.system("adb shell am force-stop com.android.settings")
    os.system("adb shell input keyevent 3")
def launch_simsettings():
    os.system("adb shell am start -n com.android.settings/.Settings")
    time.sleep(2)
    os.system("adb shell input tap 320 800")

def sim1_enable():
    os.system("adb shell input tap 300 740")
    time.sleep(2)
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def sim2_enable():
    os.system("adb shell input tap 665 720")
    time.sleep(4)
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")


def sim1_disable():
    print("enabling sim1....")
    os.system("adb shell input tap 300 740")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(4)
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def sim2_disable():
    os.system("adb shell input tap 665 720")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(4)
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def check_sim1state():
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="[gsm.sim.state]: [READY,READY]"
            string2 = "[gsm.sim.state]: [READY,NOT_READY]"
            string3 = "[gsm.sim.state]: [READY,ABSENT]"
            if (string1 in line or string2 in line or string3  in line):
                print("Sim1 is enabled")
                return(True)
        else:
            print("sim1 is disabled ")
            return(False)

def check_sim2state():
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="[gsm.sim.state]: [READY,READY]"
            string2 = "[gsm.sim.state]: [NOT_READY,READY]"
            string3 = "[gsm.sim.state]: [ABSENT,READY]"
            if (string1 in line or string2 in line or string3  in line):
                print("Sim2 is enabled")
                return(True)
        else:
            print("sim2 is disabled ")
            return(False)

kill_simsettings()
launch_simsettings()
state=check_sim1state()
if(state != 1):
    sim1_enable()
    check_sim1state()
state=check_sim2state()
if(state==1):
    sim2_disable()
    check_sim2state()
time.sleep(3)
kill_simsettings()
