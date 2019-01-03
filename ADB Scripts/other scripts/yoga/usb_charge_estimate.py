import os
import time
import re
import random
import math
flag=1

os.system("adb shell dumpsys battery >battery.txt")
fp=open("battery.txt","r")

for i in range(15):
    buf=fp.readline()
    if (re.search("level",buf,re.I)):
        print(buf)
then = time.time() #Time before the operations start
str1="level: 94"
while(flag):
    
    os.system("adb shell dumpsys battery >battery.txt")
    fp=open("battery.txt","r")
    for i in range(15):
        buf1=fp.readline()
        #if (re.search("level:92",buf1,0)):
        if(str1 in buf1):  
            print(buf1)
            flag=0
            break
        
now = time.time() #Time before the operations start
mins=math.floor((now-then)/60)
sec=math.floor((now-then)%60)
print("It took: ", mins,"min : ",sec,"sec")
#print("It took: ", now-then, " seconds for booting")