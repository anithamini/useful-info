import os
import time
import csv
fields=['testcase','passcnt','failcnt']
iterations=3
pass_cnt=0
fail_cnt=0
def kill_mail():
        os.system("adb shell am force-stop com.google.android.gm")
def launch_mail():
        os.system("adb shell am start -n com.google.android.gm/com.google.android.gm.ConversationListActivityGmail")
        time.sleep(1)
        os.system("adb shell input tap 973 1880")
        time.sleep(1)
def compose_mail():
    os.system("adb shell input text innomindsgm@gmail.com")
    os.system("adb shell input keyevent 66") 
    os.system("adb shell input keyevent 66")
    os.system("adb shell input text hii")
    os.system("adb shell input keyevent 19") 
    os.system("adb shell input keyevent 19")
    os.system("adb shell input text test")
def attach_mail():
         os.system("adb shell input tap 787 156")
        for i in range(1,3):
                os.system("adb shell input keyevent 20")     #for attachements in the mail
                os.system("adb shell input keyevent 66")
                time.sleep(1)
        os.system("adb shell input tap 908 155")
"""
def test():
    os.system("adb shell logcat >gmail.txt")
    with open("gmail.txt","r+") as fh:
            lines= fh.readlines()
            for line in lines:
                    string="activation: Account innomindsgm@gmail.com"
                    if (string in line):
                            return 1
                            break
            else:
                    return 0
"""
kill_mail()         
for i in range(iterations):
        launch_mail()
"""
        result=test()
        if result:
                pass_cnt+=1
        else:
                fail_cnt+=1
"""
        compose_mail()
        attach_mail()
        time.sleep(5)      #delay is given based on the signal strength  based on that delay,mail will be sent
        kill_mail()
"""
data_rows=['email_send',str(pass_cnt),str(fail_cnt)]
csvfp=open("exc.csv",'a')   
csvwriter=csv.writer(csvfp)

#writing the fields
csvwriter.writerow(fields)

#writing the rows
csvwriter.writerow(data_rows)
"""
