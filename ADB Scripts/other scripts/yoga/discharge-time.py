import time
import os
import re
import math
hrs=0
str2="MAC: ac:c1:ee:62:92:93"
def check():
    os.system("adb shell dumpsys wifi >mac.txt")
    fs=open("mac.txt","r")
    time.sleep(1)
    str1=fs.read()
    #str2="MAC: b8:de:5e:01:d9:2e"
    while 1:
        if (str2 in str1):
            print(str2)
            return str1
        else:
            return 0

def batstatus():
    buff=check()
    if buff:
        print("found")
        os.system("adb shell dumpsys battery >battery.txt")
        fp=open("battery.txt","r")
        for i in range(15):
            buf=fp.readline()
            if (re.search("level",buf,re.I)):
                print(buf)
                break
    else:
        print("please connect the same device")
        while(1!=os.system("adb shell getprop sys.boot_completed")):
            k=0
        while(1==os.system("adb shell getprop sys.boot_completed")):   
            if(check()):
                break
    return buff       
         
buff1=batstatus()
print("your battery status has been recorded...")
print("u can remove your device")
while(1!=os.system("adb shell getprop sys.boot_completed")):
    time.sleep(1)
then = time.time() #Time before the operations start
while(1==os.system("adb shell getprop sys.boot_completed")):
    k=0
#batstatus()
buff1=batstatus()
while(1):
    if(str2 in str(buff1)):
        now = time.time() #Time before the operations start
        mins=math.floor((now-then)/60)
        if (mins >= 60):
            hrs=math.floor(mins/60)
            mins=mins%60
        sec=math.floor((now-then)%60)
        print("It took: ",hrs,"hrs :", mins,"min : ",sec,"sec")
        break
    else:
        buff1=batstatus()

