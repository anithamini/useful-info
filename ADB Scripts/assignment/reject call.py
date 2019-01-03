                  #reject a call with a message


import os
import time
#end a call
#os.system("adb shell input keyevent 6")
#reject a call with a msg
os.system("adb shell input swipe 120 2076 234 1307")
j=input("enter the number to choose msg    ")
os.system("adb shell input text "+j)  
i=int(j)
for k in range(1,i):
    print(k)
    os.system("adb shell input keyevent 20")
if(i==1):   
    print("can't talk now.What's up?")
elif(i==2):
    print("I'll call you right back")
elif(i==3):
    print("I'll call you later")
elif(i==4):
    print("Can't talk now.Call me later?")
elif(i==5):
    print("Write your own...")
    os.system("adb shell input keyevent 66")  
    str=input("enter ur own message...")
    os.system("adb shell input text "+str)
    os.system("adb shell input keyevent 22")    
else:
    print("cancel")
    os.system("adb shell input tap 358 1189")
    os.system("adb shell input keyevent 6")  
os.system("adb shell input keyevent 66")
544 184
