import os
import sys,time


def pull_img():
    os.system("adb pull /storage/emulated/0/coolpad/screenshots/Quation.png")
    print "img is pulled from sdcard to host......\n"

def push_img():
    #os.system("adb push 'C:\Users\Public\Pictures\Sample Pictures\Desert.jpg' /storage/emulated/0")
    #os.system("adb push C:\Users\amogilipalem\Desert.jpg /storage/emulated/0")
    os.system("adb push Desert.jpg /storage/emulated/0")
    print "img is pushed from host to sdcard......\n"

pull_img()
time.sleep(2)
push_img()
time.sleep(2)
