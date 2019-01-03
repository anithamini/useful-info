import os,time
#count=2
n=1
pass_TC = 0
fail_TC = 0
from sys import argv
count = argv[1]
def sms_test():
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
                    "adb shell am start -a android.intent.action.SENDTO -d sms:9160185866 --es sms_body 'SMS BODY GOES HERE' --ez exit_on_sent true")
                time.sleep(5)
                os.system("adb shell input tap 680 1290")
                time.sleep(5)
                return 1

        else:
            print("sim not present, please insert the sim and start the test")
            return 0


while(count!=0):
    print("Itr", n )
    print("--------------------------------")
    n=n+1
    x=sms_test()
    if(x==1):
        pass_TC += 1
        print("Test case = PASS ...\n")
        print("--------------------------------")
        os.system("adb wait-for-device shell input keyevent 4")
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

