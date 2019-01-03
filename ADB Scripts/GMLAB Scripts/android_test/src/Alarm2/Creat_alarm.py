'''
Created on 17-Jul-2018

@author: akesiboyina
'''
import os
def func():
    n1=22
    for i in range(0,5):
        os.system("adb shell input keyevent "+str(n1))
        if(i==2):
            n1+=45
def alarm(hr,minu):
    os.system("adb shell input tap 125 177")
    os.system("adb shell input tap 521 1902")
    os.system("adb shell input tap 219 1548")
    os.system("adb shell input keyevent 61")
    func()
    os.system("adb shell input text " +str(hr))
    os.system("adb shell input keyevent 61")
    func()
    os.system("adb shell input text "+ str(minu))
    n2=61
    for i in range(0,4):
        if(i==3):
            n2+=5
        os.system("adb shell input keyevent "+str(n2))
        


