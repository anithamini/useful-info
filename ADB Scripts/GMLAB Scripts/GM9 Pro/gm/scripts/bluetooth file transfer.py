import os
import sys
import time
import re



os.system("adb shell input touchscreen swipe 500 600 100 600 ")
time.sleep(0.5)
os.system("adb shell input tap 163 1100")
time.sleep(1)
os.system("adb shell input touchscreen swipe 800 400 100 400 500")
time.sleep(1)
os.system("adb shell input tap 200 600")
time.sleep(0.5)
os.system("adb shell input touchscreen swipe 300 400 300 400 1000")
time.sleep(0.5)
os.system("adb shell input tap 320 1794")
time.sleep(0.5)

os.system("adb shell input tap 400 1520")
time.sleep(1)
os.system("adb shell input tap 759 1780")
time.sleep(1)
os.system("adb shell input tap 450 600")
time.sleep(2)
os.system( "adb shell dumpsys bluetooth_manager > bt.txt")
time.sleep(2)
bt=open("bt.txt","r+")
buffer=bt.read()

while(re.search("Is acquired                    : false",buffer,re.I)) :
    print("file not sending")
    os.system("adb shell dumpsys bluetooth_manager > bt.txt")
    time.sleep(1)
    bt=open("bt.txt","r+")
    time.sleep(1)
    buffer=bt.read()
    time.sleep(2)
    
   


while(re.search("Is acquired                    : true",buffer,re.I)) :
    print("file sending")
    os.system( "adb shell dumpsys bluetooth_manager > bt.txt")
    time.sleep(1)
    bt=open("bt.txt","r+")
    buffer=bt.read()
    time.sleep(2)

print("file sent successfully")
for i in range(4):
    os.system("adb shell input keyevent 4")

time.sleep(0.5)
os.system("adb shell input touchscreen swipe 500 5 500 1500 1000") 
os.system("adb shell input touchscreen swipe 500 1050 500 1500 1000") 
os.system("adb shell input tap 400 700")
os.system("adb shell input keyevent 3")
