import os
from time import sleep

pass_cnt=0
fail_cnt=0

def validate():
    os.system( "adb shell dumpsys activity > game.txt")
    with open("game.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1="packageName=com.imangi.templerun processName=com.imangi.templerun"
            if(s1 in line):
                return(True)
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

KillGame()
LaunchGame()
if(validate()):
        pass_cnt+=1
else:
        fail_cnt+=1
KillGame()
print("pass_cnt:",pass_cnt)
print("fail_cnt",fail_cnt)
