import os
import re
import time
pass_cnt=0
fail_cnt=0
def kill_mail():
        os.system("adb shell am force-stop com.google.android.gm")
def launch_mail():
        os.system("adb shell am start -n com.google.android.gm/com.google.android.gm.ConversationListActivityGmail")
        time.sleep(2)
        os.system("adb shell input tap 630 1198")
        time.sleep(2)
def send_mail():
        print("entering mail-id")
        mail=raw_input("enter mail id:")
        time.sleep(2)
        os.system("adb shell input text " +mail)
        os.system("adb shell input keyevent 66")
        os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 19")
def sub_mail():
        time.sleep(2)
        print("subject of the mail")                         #for subject of the mail
        os.system("adb shell input text testcase")
        os.system("adb shell input keyevent 20")
def body_mail():
        time.sleep(2)
        print("body of the mail")                            #for body of the mail
        os.system("adb shell input text hiiii")         
def attach_mail():
        os.system("adb shell input tap 482 106")
        for i in range(1,3):
                os.system("adb shell input keyevent 20")     #for attachements in the mail
                os.system("adb shell input keyevent 66")
                time.sleep(5)
        os.system("adb shell input tap 605 115")

def test():
        with open("C:\Users\schevvakula\log.txt","r+") as fh:
                lines= fh.readlines()
                for line in lines:
                        #print(line)
                        string="created account chevvakula1996@gmail.com"
                        if (string in line):
                                return 1
                                break
                else:
                        return 0
kill_mail()         
for i in range(1,3):
        launch_mail()
        result=test()
        if result:
                pass_cnt+=1
                print("account succesfully created",pass_cnt)
        else:
                fail_cnt+=1
                print("account is not created",fail_cnt)
        send_mail()
        sub_mail()
        body_mail()
        attach_mail()
        time.sleep(5)      #delay is given based on the signal strength  based on that delay,mail will be sent
        kill_mail()

