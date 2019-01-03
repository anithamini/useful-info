import os
import time
import re
import random
os.system("adb shell dumpsys batterystats >battery.txt")
fp=open("battery.txt","r+")
buf=fp.readline()
#k=0
while(1):
    buf=fp.readline()

    if(re.search('Charge total time:', buf,0)):
        #k+=1
    #if (k==3):
        break
print(buf)
