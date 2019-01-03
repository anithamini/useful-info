import time
import sys
import unittest
import os
iterations=2
#iterations=sys.argv[1]
PassCnt=0
FailCnt=0
i=0
def Validate():
        os.system("adb logcat -d > torch.txt")
        cnt=0
        with open("torch.txt","r") as fh:
                while 1:
                        buf=fh.readline()
                        if (buf==""):
                                break
                        if("torch status is now AVAILABLE_ON" in buf):
                                cnt+=1
                       
                print(cnt)        
                return cnt     

def torch_on():
        os.system("adb shell input swipe 0 0 0 300")
        os.system("adb shell input tap 990 176")
        
def torch_off():
        os.system("adb shell input tap 990 176")
        os.system("adb shell input swipe 0 400 300 0")

for i in range(int(iterations)):
    time.sleep(2)
    torch_on()
    if(Validate()==i+1):
            PassCnt+=1
    else:
            FailCnt+=1
    time.sleep(2)
    torch_off()
print("Pass Count=",PassCnt,",Fail Count=",FailCnt)
