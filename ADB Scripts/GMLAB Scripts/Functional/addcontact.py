import os
import time

def kill_contact():
    os.system("adb shell input keyevent 3")
def add_contact():
    os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input text test")
    for i in range(1,4):
    	os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input text 9100205816")
    os.system("adb shell input tap 855 188")	
    os.system("adb shell input keyevent 3")
def edit_contact():
    os.system("adb shell am start -a android.intent.action.VIEW content://contacts/people/")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text test")
    for i in range(1,7):
    	os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 930 1862")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")  
    os.system("adb shell input text test")
    for i in range(1,5):
    	os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 855 188")
    time.sleep(4)
    
def delete_contact():
    os.system("adb shell am start -a android.intent.action.VIEW content://contacts/people/")
    time.sleep(5)
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text test")
    for i in range(1,7):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 1000 136")
    for i in range(1,3):
    	os.system("adb shell input keyevent 20")
    for i in range(1,3):
    	os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    
    
kill_contact()
add_contact()
edit_contact()
delete_contact()
kill_contact()

