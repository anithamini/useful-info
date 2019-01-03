import os
import csv
import time
fields=['testcase','passcnt','failcnt']
Iterations=3
pass_cnt=0
fail_cnt=0
def launch_settings():
        os.system("adb shell am start -a android.settings.SETTINGS")
        time.sleep(1)
def contact_sync():
        os.system("adb shell input swipe 415 1273 359 151")
        time.sleep(1)
        os.system("adb shell input tap 345 857")
        time.sleep(1)
        for i in range(1,4):
             os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
        for k in range(1,2):
                os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
        for k in range(1,3):
                os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")       
        os.system("adb shell input keyevent 66")
        print("gmail account is synced with contacts")
def kill_settings():
        os.system("adb shell am force-stop com.android.settings")
"""
def test():
    print("before")    
    os.system("adb shell logcat >sync.txt")
    print("after")
    with open("sync.txt","r+") as fh:
            lines= fh.readlines()
            for line in lines:
                    string="ContactsSyncAdapter: @onPerformSync Sync finished successfully"
                    if (string in line):
                            return 1
                            break
            else:
                    return 0
"""

kill_settings()     
for i in range(iterations):
        launch_settings()
        contact_sync()
"""
        result=test()
        if result:
                pass_cnt+=1
        else:
                fail_cnt+=1
data_rows=['email_contact_sync',str(pass_cnt),str(fail_cnt)]
csvfp=open("exc.csv",'a') 
csvw=csv.writer(csvfp)
#writing the fields
csvw.writerow(fields)
#writing the rows
csvw.writerow(data_rows)
csvfp.close()
"""    
	kill_settings()
