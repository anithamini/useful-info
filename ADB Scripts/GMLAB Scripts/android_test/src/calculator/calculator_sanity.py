'''
Created on Jul 24, 2018

@author: hnagella
'''
import os
from time import sleep
from common import constants
LaunchPassCnt=0
LaunchFailCnt=0
KillPassCnt=0
KillFailCnt=0
DegPassCnt=0
DegFailCnt=0 
RadPassCnt=0
RadFailCnt=0 
i=0

def Validate(s1,s2):
    os.system('adb shell dumpsys '+s2+' > calc.txt')         #To Collect the activity logs
    with open("calc.txt","r") as fh:
        buff=fh.read()
        if(s1 in buff):
            return(True)
        else:
            return(False)

def KillCalculator():
    os.system("adb shell am force-stop com.google.android.calculator")      #To kill the calculator application
    sleep(2)
    global KillPassCnt
    global KillFailCnt
    global fileobj_logfile
    if(Validate("I=com.android.launcher3/com.android.searchlauncher.SearchLauncher",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillCalculator"+"\t"+"PASS\n")
        KillPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "TestKillCalculator"+"\t"+"FAIL\n")
        KillFailCnt+=1

def LaunchCalculator():
    global LaunchPassCnt
    global LaunchFailCnt
    global fileobj_logfile
    os.system("adb shell monkey -p com.google.android.calculator -c android.intent.category.LAUNCHER 1")        #To Launch the Calculator application
    sleep(2)
    if(Validate("A=com.google.android.calculator",'activity recents | find "Recent #0"')):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchCalculator"+"\t"+"PASS\n")
        LaunchPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestLaunchCalculator"+"\t"+"FAIL\n")
        LaunchFailCnt+=1
        
def Mathematic():
    for i in range(0,2):
        os.system("adb shell input keyevent 8")     #For tapping number 1
    os.system("adb shell input keyevent 67")        #To delete the number 
    os.system("adb shell input keyevent 81")        #For '+' operator
    os.system("adb shell input keyevent 10")        #For tapping number 3
    os.system("adb shell input keyevent 66")        #For tapping '=' or enter

def Trigonometric():
    os.system("adb shell input touchscreen swipe 1057 1343 170 1432")       #For dragging the screen to trigonometric operations table
    os.system("adb shell input tap 450 1154")                               #For selecting the sin function
    os.system("adb shell input touchscreen swipe 170 1432 1057 1343")       #For dragging the screen to mathematical operations table
    n=10
    for i in range(0,3):
        os.system("adb shell input keyevent "+str(n))                       #For tapping number 3 for iteration 0
        if (i==0):                                                          #For tapping number 0 for iteration 1
            n-=3                                                            #For '-' operator for iteration 2
        else:
            n+=59
            
def RadMode():
    global RadPassCnt
    global RadFailCnt
    global fileobj_logsummary
    os.system("adb shell input tap 140 210")                                #Changing to Radian mode
    Mathematic()
    Trigonometric()
    if(Validate("BFGS change:active","activity")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestRadMode"+"\t"+"PASS\n")
        RadPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestRadMode"+"\t"+"FAIL\n")
        RadFailCnt+=1
    
def DegMode():
    global DegPassCnt
    global DegFailCnt
    global fileobj_logsummary
    os.system("adb shell input tap 140 210")                                #Changing to Degree mode
    Mathematic()
    Trigonometric()  
    if(Validate("BFGS change:active","activity")):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestDegMode"+"\t"+"PASS\n")
        DegPassCnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_2" +"\t"+ "TestDegMode"+"\t"+"FAIL\n")
        DegFailCnt+=1 
              
def TestCalculatorSanity_Setup():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nCalculator_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    
def TestCalculatorSanity_testsuit(): 
    KillCalculator()
    LaunchCalculator()
    DegMode()
    RadMode()

def Calculator_sanity_summary_log():
    global LaunchPassCnt
    global LaunchFailCnt
    global KillPassCnt
    global KillFailCnt
    global DegPassCnt
    global DegFailCnt
    global RadPassCnt
    global RadFailCnt
    global fileobj_logsummary
    print("Launch Pass Count=",LaunchPassCnt,",LaunchFail Count=",LaunchFailCnt)
    print("Kill Pass Count=",KillPassCnt,",Kill Fail Count=",KillFailCnt)
    print("Degree mode Pass Count=",DegPassCnt,",LaunchFail Count=",DegFailCnt)
    print("Radian mode Pass Count=",RadPassCnt,",Kill Fail Count=",RadFailCnt)
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nCalculator_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(LaunchPassCnt+LaunchFailCnt)+"\t" + str(LaunchPassCnt) +"\t"+ str(LaunchFailCnt)+"\n")
    fileobj_logsummary.write(str(KillPassCnt+KillFailCnt)+"\t" + str(KillPassCnt) +"\t"+ str(KillFailCnt)+"\n")
    fileobj_logsummary.write(str(DegPassCnt+DegFailCnt)+"\t" + str(DegPassCnt) +"\t"+ str(DegFailCnt)+"\n")
    fileobj_logsummary.write(str(RadPassCnt+RadFailCnt)+"\t" + str(RadPassCnt) +"\t"+ str(RadFailCnt))
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    LaunchPassCnt=0
    LaunchFailCnt=0
    KillPassCnt=0
    KillFailCnt=0
    DegPassCnt=0
    DegFailCnt=0 
    RadPassCnt=0
    RadFailCnt=0 
    
def TestCalculatorSanity_main():
    print("Entry of TestCalculatorSanity_main")
    TestCalculatorSanity_Setup()
    TestCalculatorSanity_testsuit()
    Calculator_sanity_summary_log()
    


