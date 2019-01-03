import os
import time
PassCnt=0
FailCnt=0
def kill_contact():
    os.system("adb shell input keyevent 3")
def Validate(s1):
    os.system("adb logcat -d > contact.txt")
    cnt=0
    with open("contact.txt","r") as fh:
        while 1:
            buf=fh.readline()
            if (buf==""):
                break
            if(s1 in buf):
                cnt+=1
                       
        print(cnt)        
        return cnt 
def add_contact():
    os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input text ABCDEFG")
    for i in range(1,4):
    	os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input text 9123456789")
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

for i in range(int(iterations)):   
    kill_contact()
    add_contact()
    if(Validate("")==i+1):
            PassCnt+=1
    else:
            FailCnt+=1
    edit_contact()
    if(Validate("")==i+1):
            PassCnt+=1
    else:
            FailCnt+=1
    delete_contact()
    if(Validate("")==i+1):
            PassCnt+=1
    else:
            FailCnt+=1
    kill_contact()
    
print("Pass Count=",PassCnt,",Fail Count=",FailCnt)

