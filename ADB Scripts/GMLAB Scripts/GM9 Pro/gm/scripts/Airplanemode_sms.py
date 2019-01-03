
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
    os.system("adb wait-for-device shell input keyevent 4")
    os.system("adb shell getprop >gsm3.txt ")
    with open("gsm3.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="[gsm.sim.state]: [READY,READY]"
            string2 = "[gsm.sim.state]: [READY,NOT_READY]"
            string3 = "[gsm.sim.state]: [NOT_READY,READY]"
            string4 = "[gsm.sim.state]: [ABSENT,READY]"
            string5 = "[gsm.sim.state]: [READY,ABSENT]"
            if(string1 in line or string2 in line or string3 in line or string4 in line or string5 in line):
                print("Sim present, so procedding the test")
                os.system("adb wait-for-device shell input keyevent 4")
                print("in home screen")
                time.sleep(5)
                os.system(
                    "adb shell am start -a android.intent.action.SENDTO -d sms:9100071290 --es sms_body 'SMS BODY GOES HERE' --ez exit_on_sent true")
                time.sleep(5)
                os.system("adb shell input tap 680 1290")
                time.sleep(5)
                return 1

        else:
            print("sim not present, please insert the sim and start the test")
    os.system("adb shell input keyevent KEYCODE_ENDCALL")
    os.system("adb shell settings put global airplane_mode_on 0")
    time.sleep(2)
    os.system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE")
    print("Aeroplane mode OFF!")
    os.system("adb shell am start -a android.intent.action.VIEW -d https://www.amazon.com/")
    time.sleep(5)     
    os.system("adb shell am force-stop com.android.chrome")
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
