
import os
import time
simvcp=0
sim1dcp=0
sim2dcp=0
sim1acp=0
sim2acp=0
simvcf=0
sim1dcf=0
sim2dcf=0
sim1acf=0
sim2acf=0
import sys
iterations=sys.argv[1]

print("------------SIM Settings---------------")

def launch_settings():
    os.system("adb shell am start -a android.settings.SETTINGS")
    time.sleep(1)
    os.system("adb shell input tap 549 177")
    os.system("adb shell input text 'sim cards'")
    for i in range(2):
        os.system("adb shell input keyevent 66")
    
def launch_voice():
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9100205816")
    time.sleep(5)

def launch_msg():
    print("launching messaging")
    os.system("adb shell am start -n com.google.android.apps.messaging/.ui.ConversationListActivity")
    time.sleep(2)
    os.system("adb shell input tap 945 1877")
    os.system("adb shell input text 9100205816")
    os.system("adb shell input keyevent 66")
    time.sleep(4)
    os.system("adb shell input text hiii")
    os.system("adb shell input tap 1000 1153")
    print("..........msg sent......")

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")

def kill_dial():
    os.system("adb shell am force-stop com.google.android.dialer")

def kill_msg():
    os.system("adb shell am force-stop com.google.android.apps.messaging")

def act_sim1():
    print("..sim1 deactiviating..")
    time.sleep(2)
    os.system("adb shell input keyevent 19")
    os.system("adb shell input tap 1004 462")
    time.sleep(2)
    for i in range(1,3):
        os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(7)
    for i in range(1,2):
        os.system("adb shell input keyevent 66")
        time.sleep(1)
    print(".....sim1 is activating......")
    os.system("adb shell input tap 933 452")
    time.sleep(5)
    for i in range(1,3):
        os.system("adb shell input keyevent 66")

def ver_sim1():
    os.system("adb shell getprop > sim1.txt")
    with open("sim1.txt","r") as fp1:
        buf1=fp1.read()
        if ("[gsm.sim.state]: [READY,NOT_READY]" in buf1 or "[gsm.sim.state]: [READY,READY]" in buf1):
            print("......sim1 is activated........")
            global sim1acp
            sim1acp+=1
            print("sim1 active count :",sim1acp)
            return(True)
        else:
            print("...sim1 is not activated....")
            global sim1acf
            sim1acf+=1
            print("sim1 deactive count :",sim1acf)
            return(False)

def data_sim1():
    print("...enabling the data connection of sim1")
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 544 991")
    time.sleep(2)
    os.system("adb shell dumpsys network_management > data1.txt")
    with open("data1.txt","r") as fd1:
        d1=fd1.read()
        if("mNetworkActive=true" in d1):
            print(".....data connection for sim1 is enabled......")
            global sim1dcp
            sim1dcp+=1
            print("sim1 data pass count :",sim1dcp)
        else:
            print(".....data connection for sim1 is disabled......")
            global sim1dcf
            sim1dcf+=1

def msg_sim1():
    print("........enabling the message of sim1.....")
    for i in range(1,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 497 1087")
    
def voice_sim1():
    print("....enabling the voice of sim1....")
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
        time.sleep(1)
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 469 1078")

def act_sim2():
    print("..sim2 deactiviating..")
    os.system("adb shell input tap 981 671")
    time.sleep(2)
    for i in range(1,3):
        os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(7)
    for i in range(1,2):
        os.system("adb shell input keyevent 66")
        time.sleep(1)
    print(".....sim2 is activating......")
    os.system("adb shell input tap 936 666")
    time.sleep(5)
    for i in range(1,3):
        os.system("adb shell input keyevent 66")

def ver_sim2():
    os.system("adb shell getprop > sim2.txt")
    with open("sim2.txt","r") as fp2:
        buf2=fp2.read()
        if ("[gsm.sim.state]: [NOT_READY,READY]" in buf2 or "[gsm.sim.state]: [READY,READY]" in buf2):
            print("......sim2 is activated........")
            global sim2acp
            sim2acp+=1
            print("sim2 active count :",sim2acp)
            return(True)
        else:
            print("......sim2 is not activated........")
            global sim2acf
            sim2acf+=1
            print("sim2 deactive count :",sim2acf)
            return(False)


def data_sim2():
    print("...enabling the data connection of sim2")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 535 1176")
    time.sleep(5)
    os.system("adb shell dumpsys network_management > data2.txt")
    with open("data2.txt","r") as fd2:
        d2=fd2.read()
        if("mNetworkActive=true" in d2):
            print(".....data connection for sim2 is enabled......")
            global sim2dcp
            sim2dcp+=1
            print("sim2 data pass count :",sim2dcp)

        else:
            print(".....data connection for sim2 is disabled......")
            global sim2dcf
            sim2dcf+=1
            print("sim2 data fail count :",sim2dcf)
            
def msg_sim2():
    print("........enabling the message of sim2.....")
    for i in range(1,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 531 1255")
    
def voice_sim2():
    print("....enabling the voice of sim2....")
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 587 1264")


def ver_voice():
    time.sleep(1)
    os.system("adb shell dumpsys telephony.registry > mCallState.txt")
    with open("mCallState.txt", "r+") as fv:
        lines = fv.read()
        if ("mCallState=2" in lines):
                print("Call successfully connected and in progress...\n")
                print("Ending the call \n")
                time.sleep(10)
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                print("Call successfully disconnected ...\n")
                global simvcp
                simvcp+=1
                print("call connected count ",simvcp)
        else:
            print("call is not connected")
            global simvcf
            simvcf+=1
            print("call fail count",simvcf)


kill_settings()
for i in range(int(iterations)):
	if(ver_sim1() and ver_sim2()):    
	    for j in range(int(iterations)):  
	        kill_settings()
	        kill_dial()
	        launch_settings()
	        act_sim1()
	        time.sleep(5)

	        data_sim1()

	        voice_sim1()
	        launch_voice()
	        ver_voice()
	        kill_dial()

	        launch_settings()
	        msg_sim1()
	        launch_msg()
	        kill_msg()
	        time.sleep(3)
	        
	        launch_settings()
	        act_sim2()
	        time.sleep(5)

	        data_sim2()
	        time.sleep(5)
	            
	        voice_sim2()
	        launch_voice()
	        ver_voice()
	        kill_dial()
	            
	        launch_settings()
	        msg_sim2()
	        launch_msg()
	        kill_msg()
	       
	else:
	    print("single sim is present.....operations cant be performed")
	kill_settings()
time.sleep(5)
