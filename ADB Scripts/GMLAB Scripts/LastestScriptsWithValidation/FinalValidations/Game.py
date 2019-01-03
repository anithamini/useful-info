import os
from time import sleep
import sys
iterations=2#sys.argv[1]
LaunchPassCnt=0
LaunchFailCnt=0
KillPassCnt=0
KillFailCnt=0

print("----------------GAME(Temple Run) Application--------------")

def Validate():
    os.system( 'adb shell dumpsys activity > game.txt')
    with open("game.txt","r") as fh:
            buff=fh.read()
            if("packageName=com.imangi.templerun processName=com.imangi.templerun" in buff):
                return(True)
            else:
                return(False)
            
def KillValidate():
    os.system( 'adb shell dumpsys activity recents | find "Recent #0" > gamekill.txt')
    with open("gamekill.txt","r") as fh:
            buff=fh.read()
            if("" not in buff):
                return(True)
            else:
                return(False)  
            
def LaunchGame():
    os.system("adb shell monkey -p com.imangi.templerun -c android.intent.category.LAUNCHER 1")
    sleep(20)
    os.system("adb shell input tap 485 1448")
    for i in range(1,9):
        print("...running...running...")
        sleep(1)
    print("....falling....")
    
def KillGame():
    os.system("adb shell am force-stop com.imangi.templerun")

for i in range(int(iterations)):
    KillGame()
    sleep(5)
    if(KillValidate()):
        KillPassCnt+=1
    else:
        KillFailCnt+=1
    sleep(2)
    LaunchGame()
    if(Validate()):
        LaunchPassCnt+=1
    else:
        LaunchFailCnt+=1
KillGame()

print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)
