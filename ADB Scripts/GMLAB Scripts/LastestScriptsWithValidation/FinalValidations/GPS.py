import os
import re
from time import sleep
import sys
iterations=sys.argv[1]
pass_cnt=0
fail_cnt=0

print("---------------GPS ON/OFF---------------")

def GPS_ON():
        print("Enabling GPS.........")
        os.system("adb shell settings put secure location_providers_allowed +gps")

def GPS_OFF():
        print("Disabling GPS.........")
        os.system("adb shell settings put secure location_providers_allowed -gps")

def validation():
    os.system("adb shell dumpsys location>text.txt")
    str1="mStarted=true"
    with open("text.txt","r") as fd:
        buf=fd.read()
    if(re.search(str1,buf,re.I)):
        return(True)
    else:
        return(False)

for i in range(int(iterations)):
#To check whether GPS is ON or OFF just to print the statement
	if(validation()):
	        print("GPS is enabled")
	        pass_cnt+=1
	else:
	        print("GPS is disabled")
	        GPS_ON()
	        sleep(2)
	        if(validation()):
	                print("GPS is enabled")
	                pass_cnt+=1
	        else:
	                print("GPS is disabled")
	                fail_cnt+=1


print("pass_cnt=",pass_cnt)
print("fail_cnt=",fail_cnt)
                
        
        
