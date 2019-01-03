import os
import sys
import time

def kill_contact():
    os.system("adb shell input keyevent 3")
def add_contact():
    os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'amani' -e phone 8978209761")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 3")
def edit_contact():
    key=0
    keyevent="amani"
    os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'amani' -e phone 8978209761")
    for key in range (0,len(keyevent)):
        os.system("adb shell input keyevent 67")    
    os.system("adb shell input text Amani")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    for key in range (0,10):
        os.system("adb shell input keyevent KEYCODE_FORWARD_DEL")
    os.system("adb shell input text 9133618606")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    
    
def delete_contact():
    os.system("adb shell am start -a android.intent.action.VIEW content://contacts/people/")
    os.system("adb shell input tap 401 198")
    os.system("adb shell input text amani")
    os.system("adb shell input touchscreen swipe 358 281 358 281 1000")
    os.system("adb shell input tap 351 1218")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 3")
    
    



kill_contact()
add_contact()
edit_contact()
delete_contact()

