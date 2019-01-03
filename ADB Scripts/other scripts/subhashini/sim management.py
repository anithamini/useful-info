
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
iterations=3
def launch_settings():
    os.system("adb shell am start -a android.settings.SETTINGS")
    time.sleep(5)
    os.system("adb shell input swipe 393 483 372 151")
    time.sleep(5)
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")

def kill_dial():
    os.system("adb shell am force-stop com.android.contacts")

def kill_msg():
    os.system("adb shell am force-stop com.android.mms")

def act_sim1():
    print("..sim1 deactiviating..")
    time.sleep(2)
    os.system("adb shell input tap 307 693")
    for i in range(1,3):
        os.system("adb shell input keyevent 22")
    for i in range(1,3):
        os.system("adb shell input keyevent 66")
    time.sleep(8)
    os.system("adb shell input keyevent 66")
    print(".....sim1 is activating......")
    time.sleep(2)
    os.system("adb shell input tap 307 693")
    time.sleep(5)
    os.system("adb shell input keyevent 66")
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
        else:
            print("...sim1 is not activated....")
            global sim1acf
            sim1acf+=1
            print("sim1 deactive count :",sim1acf)

def act_sim2():
    print("..sim2 deactiviating..")
    time.sleep(2)
    os.system("adb shell input tap 663 697")
    for i in range(1,3):
        os.system("adb shell input keyevent 22")
    for i in range(1,3):
        os.system("adb shell input keyevent 66")
    time.sleep(8)
    os.system("adb shell input keyevent 66")
    print(".....sim2 is activating......")
    os.system("adb shell input tap 663 697")
    for i in range(1,3):
        os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(3)

def ver_sim2():
    os.system("adb shell getprop > sim2.txt")
    with open("sim2.txt","r") as fp2:
        buf2=fp2.read()
        if ("[gsm.sim.state]: [NOT_READY,READY]" in buf2 or "[gsm.sim.state]: [READY,READY]" in buf2):
            print("......sim2 is activated........")
            global sim2acp
            sim2acp+=1
            print("sim2 active count :",sim2acp)
        else:
            print("......sim2 is not activated........")
            global sim2acf
            sim2acf+=1
            print("sim2 deactive count :",sim2acf)

def data_sim1():
    print("...enabling the data connection of sim1")
    for i in range(1,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 66")
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
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 66")
    for i in range(1,3):
        os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 66")
    
def voice_sim1():
    print("....enabling the voice of sim1....")
    for i in range(1,3):
        os.system("adb shell input keyevent 19")
        time.sleep(1)
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 66")

def data_sim2():
    print("...enabling the data connection of sim2")
    for i in range(1,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
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
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def voice_sim2():
    print("....enabling the voice of sim2....")
    for i in range(1,3):
        os.system("adb shell input keyevent 19")
        time.sleep(1)
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")

def launch_voice():
    os.system("adb shell am start -n com.android.contacts/com.android.contacts.activities.WtDialerActivity")
    time.sleep(5)
    os.system("adb shell input tap 329 674")
    num=input("enter mobile no. to dial")
    os.system("adb shell input text " +str(num))
    sim=input("select 1 for sim1 and 2 for sim2")
    if(int(sim)==1):
        os.system("adb shell input tap 324 1229")
    elif(int(sim)==2):
        os.system("adb shell input tap 444 1226")
    else:
        print("........invalid selection......")

def launch_msg():
    print("launching messaging")
    os.system("adb shell am start com.android.mms")
    time.sleep(2)
    os.system("adb shell input tap 522 103")
    num=input("enter mobile no. to dial")
    os.system("adb shell input text " +str(num))
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input text hiii")
    os.system("adb shell input tap 665 731")
    print("..........msg sent......")

def ver_voice():
    time.sleep(1)
    os.system("adb shell dumpsys telephony.registry > mCallState.txt")
    with open("mCallState.txt", "r+") as fv:
        lines = fv.read()
        if ("mCallState=2" in lines):
                print("Call successfully connected and in progress...\n")
                print("Ending the call \n")
                time.sleep(5)
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

    
for j in range(int(iterations)):  
    kill_settings()
    kill_dial()
    launch_settings()
    act_sim1()
    ver_sim1()
    time.sleep(5)
    data_sim1()
    msg_sim1()
    launch_msg()
    kill_msg()
    time.sleep(8)
    voice_sim1()
    launch_voice()
    ver_voice()
    kill_dial()
    time.sleep(8)
    act_sim2()
    ver_sim2()
    time.sleep(5)
    data_sim2()
    msg_sim2()
    launch_msg()
    kill_msg()
    voice_sim2()
    launch_voice()
    ver_voice()
    kill_dial()
    kill_settings()
time.sleep(10)
