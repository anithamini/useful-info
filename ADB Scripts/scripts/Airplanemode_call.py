
import os
import time
#count=2
n=1
pass_TC = 0
fail_TC = 0
from sys import argv
count = int(argv[1])
def aeroplane_mode():
    print("Aeroplane mode:")
    os.system("adb shell settings put global airplane_mode_on 1")
    time.sleep(2)
    os.system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE")
    print("Started!!!")
    time.sleep(5)
    #os.system("adb wait-for-device shell input keyevent 3")
    #os.system("adb shell am start -a android.intent.action.CALL -d tel:9160185866")
    #print("Device trying to call in aeroplane mode")
    #time.sleep(10)
    #print("Call not able to proceed in aeroplane mode")
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="[gsm.sim.state]: [READY,READY]"
            if(string1 in line):
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
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9100071290")
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
    os.system("adb shell input keyevent KEYCODE_ENDCALL")
    os.system("adb shell settings put global airplane_mode_on 0")
    time.sleep(2)
    os.system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE")
    print("Aeroplane mode OFF!")
    time.sleep(2);
    return 1
    #os.system("adb shell dumpsys media.player > audio.txt")

while(count!=0):
    print("Itr", n )
    print("--------------------------------")
    n=n+1
    x=aeroplane_mode()
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
print ("---------------------------------")
