import os
import sys
import sys
import time
import re
def facebookstate():
    os.system("adb logcat>logfile_face.txt")
    fp=open("logfile_face.txt","r+")
    buff=fp.read()
    enabled=re.search("com.android.commands.am.Am start -a android.intent.action.VIEW -d facebook://facebook.com/inbox ",buff,re.I)
    if enabled:
        return(True)
    else:
        return(False)

def facebooklaunch():
    os.system("adb shell am start -a android.intent.action.VIEW -d facebook://facebook.com/inbox")

def facebook_id():
    time.sleep(2)
    os.system("adb shell input tap 540 1040")
    time.sleep(2)
    os.system("adb shell input text mounikavemunoori@gmail.com")
    os.system("adb shell input keyevent 20")
    time.sleep(2)

def facebook_password():
    os.system("adb shell input tap 500 806")
    #below command we need to type fb password instead of *
    os.system("adb shell input text *****")
    os.system("adb shell input keyevent 66")
    #time.sleep(20)


def facesearchvideo():
    os.system("adb shell input tap 530 170")
    os.system("adb shell input text cutebabiesvideos")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 600 1570")


state=facebookstate()
if state:
    print("facebook on")
else:
    print("facebook off")


facebooklaunch()
state=facebookstate()
print state
time.sleep(2)

facebook_id()
time.sleep(1)

facebook_password()
time.sleep(60)

facesearchvideo()
# below one for scrolling the screen up to 20 iterations
"""i=0
while i<20:
    os.system("adb shell input touchscreen swipe 420 1684 586 576")
    time.sleep(1)
    i=i+1"""


