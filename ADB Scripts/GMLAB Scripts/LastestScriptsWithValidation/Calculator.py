import os
pass_cnt=0
fail_cnt=0
import sys

iterations=sys.argv[1]

print("-----------------Calculator Application--------------------")

def LaunchCalculator():
        os.system("adb shell monkey -p com.google.android.calculator -c android.intent.category.LAUNCHER 1")

def validate():
    os.system( "adb shell dumpsys activity > calc.txt")
    with open("calc.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1="packageName=com.google.android.calculator processName=com.google.android.calculator"
            if(s1 in line):
                return(True)
        return(False)

def operation():
    for i in range(0,2):
        os.system("adb shell input keyevent 8")
    os.system("adb shell input keyevent 67")
    os.system("adb shell input keyevent 81")
    os.system("adb shell input keyevent 10")
    os.system("adb shell input keyevent 66")

def Trigonometric():
        os.system("adb shell input touchscreen swipe 1057 1343 170 1432")
        os.system("adb shell input tap 450 1154")
        os.system("adb shell input touchscreen swipe 170 1432 1057 1343")
        n=10
        for i in range(0,3):
                os.system("adb shell input keyevent "+str(n))
                if (i==0):
                        n-=3
                else:
                        n+=59
def RadMode():
    print("Changing to Radian Mode")
    os.system("adb shell input tap 140 210")
    operation()
    Trigonometric()
               
def DegMode():
    print("Changing to Degree Mode")
    os.system("adb shell input tap 140 210")
    operation()
    Trigonometric()         
def KillCalculator():
    os.system("adb shell am force-stop com.google.android.calculator")

for i in range(int(iterations)):
	KillCalculator()
	LaunchCalculator()
	if(validate()):
	        pass_cnt+=1
	else:
	        fail_cnt+=1
	DegMode()               
	RadMode()
print("Fail count=",fail_cnt,",Pass count=",pass_cnt)
