
import time
import os
import re

################################################ EXECUTION STARTED######################

k=0
while(os.system("adb shell getprop sys.boot_completed")):  
    k=0
#################################################### DEVICE CONNECTED######################### AND GETTING DEVICE IMEI####################
os.system("adb shell getprop >imei.txt")
fs=open("imei.txt","r")
time.sleep(1)

while 1:
    str1=fs.readline()
    if (re.search("ro.ril.miui.imei",str1)):
        #print(str1)
        break
print(str1)
fs.close()


############################CALCULATING DEVICE PERCENTAGE BEFORE TESTING#########################
def before():
    
    os.system("adb shell dumpsys battery >battery.txt")
    
    
    fp=open("battery.txt","r")
    buf="ghdj"
    #print(buf)
    for i in range(15):
        buf=fp.readline()
       
        if (re.search("level",buf,re.I)):
            print(buf)
            break
    #print(buf)
    j=" "
    p=0
    for i in buf:
        if (i<='9' and i>='0'):
            j=int(i)
            p=p*10+j
    #print(p)        
    #print(type(p))
    return p


#print(time.localtime(time.time()))
###############################PRINTING THE PRESENT TIME###########################################
print(time.asctime())
########CALLING THE FUNCTION
num1=before()
num3=num1*41
print("the charged mAh is ",num3,"mAh")
time.sleep(5)

#######################REMOVING THE DEVICE##########
while(os.system("adb shell getprop sys.boot_completed")):
    k=0
##################DEVICE CONNECTED AND GETTING IMEI INFO###############
os.system("adb shell getprop >imei1.txt")
fs=open("imei1.txt","r")
time.sleep(1)

while 1:
    str2=fs.readline()
    if (re.search("ro.ril.miui.imei",str2)):
        break
print(str2)
fs.close()

#############################CHECKING THE DEVICES WHETHER TWO ARE SAME OR NOT,IF NOT EXECUTION GOES TO INFINITE LOOP##################
while(str1 not in str2):
    while(os.system("adb shell getprop sys.boot_completed")==0):
        k=0  
    while(os.system("adb shell getprop sys.boot_completed")):
        k=0
    os.system("adb shell getprop >imei1.txt")
    fs=open("imei1.txt","r")
    time.sleep(1)

    while 1:
        str2=fs.readline()
        if (re.search("ro.ril.miui.imei",str2)):
            break
print(str2)
    
fs.close()
time.sleep(2)
#####################CALLING THE FUNCTION AND TAKING THE BATTERY INFORMATION####################
num2=before()
discharge=num1-num2
charge=num2-num1
mAh=charge*41
num2=num2*41
print(time.asctime())
###################printing the results############################
print("the charged mAh is ",num2,"mAh")
mAh=discharge*41
print("the discharged mAh is ",mAh,"mAh")

