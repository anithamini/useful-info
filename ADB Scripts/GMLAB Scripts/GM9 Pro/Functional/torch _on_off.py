import time
import unittest
import os
PassCnt=0
FailCnt=0
i=0
def Validate():
        os.system("adb logcat -m 15 > torch.txt")
        fp=open("torch.txt","r")
        buff=fp.read()
        if("torch status is now AVAILABLE_ON" in buff):
                return(True)
        else:
                return(False)

def torch_on():
        os.system("adb shell input swipe 0 0 0 300")
        os.system("adb logcat -c")
        os.system("adb shell input tap 990 176")
        
def torch_off():
        os.system("adb shell input tap 990 176")
        os.system("adb shell input swipe 0 400 300 0")

while (i<5):
    time.sleep(2)
    torch_on()
    if(Validate()):
            
            PassCnt+=1
    else:
            FailCnt+=1
    print(Validate())
    time.sleep(2)
    torch_off()
    i+=1
print("Pass Count=",PassCnt,",Fail Count=",FailCnt)
