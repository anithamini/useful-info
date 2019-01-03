import os
import time
import unittest
i=0
print("trying to drag the screen")
def drag_screen():
    os.system("adb shell input touchscreen swipe 560 55 560 820")
    print("screen is dragged successflly")
def airplane_on():
    os.system("adb shell input tap 990 180")
    print("airplane mode is on for iteration",i)
def airplane_off():
    os.system("adb shell input tap 990 180")
    print("airplane mode is off for iteration",i)

while(i<5):
    drag_screen()
    time.sleep(2)
    airplane_on()
    time.sleep(2)
    airplane_off()
    os.system("adb shell input keyevent 3")
    i+=1
