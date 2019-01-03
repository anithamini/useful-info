#****************************************************************************************************************************************************
# * Copyright (C) 1998-2016 Connected Devices, Innominds Software Inc.
# *
# * This file is part of Connected Devices Project
# *
# * Connected Devices Project and associated code can not be copied
# * and/or distributed without the express permission of
# * Innominds Software Inc. and/or it subsidiaries
# *
# * Description: This script executes the MO call test case.
# * For any modification contact @Ramamohan (rbandapalli@innominds.com)
#*****************************************************************************************************************************************************

import os
import time
import sys
count=int(sys.argv[1])
n=1
pass_TC = 0
fail_TC = 0
print ("Pushing audio and video to /sdcard")
os.system("adb push C://Users//galluri//Desktop//GM_Stability2//GM_Stability//media_video //sdcard/movies/media/")
def mo_call_test():
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
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9100071290")#6300246158
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
                time.sleep(1)
                os.system("adb shell input keyevent 3")#("adb shell input keyevent KEYCODE_ENDCALL")
                print("Call is in background!!!...\n")
                print("Video is playing")
                os.system("adb shell am start -a android.intent.action.VIEW -d file:///sdcard//movies//media//1080p_30fps_128kbps.mp4 -t video/3gp")
                time.sleep(7)
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                print("call ENDED!!!")
                time.sleep(5)
                test=1
                #break
                return 1
        else:
            print("Unable to connect the call, so test case is failed")
            return 0



while(count!=0):
    print("Itr", n )
    print("--------------------------------")
    n=n+1
    x=mo_call_test()
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

