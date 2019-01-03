
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
    os.system("adb wait-for-device shell am start -a android.settings.BLUETOOTH_SETTINGS")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 23")
    time.sleep(4)
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
