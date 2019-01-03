import os
import sys
import time
import unittest
import re
i=0
print("trying to drag the screen")
def drag_screen():
    os.system("adb shell input touchscreen swipe 655 25  625 1000")
    print("screen is dragged successfully for iteration ",i)
def torch_on():
    os.system("adb shell input tap 691 470")
    print("torch is ON for iteration ",i)
def torch_off():
    os.system("adb shell input tap 691 470")
    print("torch is OFF for iteration ",i)
while (i<10):
    drag_screen()
    time.sleep(2)
    torch_on()
    time.sleep(2)
    torch_off()
    i+=1
    
