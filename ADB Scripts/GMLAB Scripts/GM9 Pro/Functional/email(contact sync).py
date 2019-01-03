import os
import csv
import time
fields=['testcase','passcnt','failcnt']
iterations=3
pass_cnt=0
fail_cnt=0
def launch_settings():
        os.system("adb shell am start -a android.settings.SETTINGS")
        time.sleep(1)
def contact_sync():
        os.system("adb shell input tap 696 222")
        os.system("adb shell input text users")
        os.system("adb shell input keyevent 66")
        os.system("adb shell input keyevent 20")
        #os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
        """
        #os.system("adb shell input swipe 415 1273 359 151")
        time.sleep(1)
        os.system("adb shell input tap 345 857")
        """
        time.sleep(1)
        for i in range(1,2):
             os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
        for k in range(1,2):
                os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
       
        for k in range(1,3):
                os.system("adb shell input keyevent 20")
        os.system("adb logcat -c")
        time.sleep(1)
        os.system("adb shell input keyevent 66")       
        os.system("adb shell input keyevent 66")
        print("gmail account is synced with contacts")
        time.sleep(5)
def kill_settings():
        os.system("adb shell am force-stop com.android.settings")
def test():
    print("before")    
    os.system("adb logcat -m 300 >sync.txt")
    print("after")
    fh=open("sync.txt",'r')
    buf=fh.read()
    fh.close()
    if("ContactsSyncAdapter: @onPerformSync Sync finished successfully" in buf):
            return 1
    else:
            return 0
kill_settings()     
for i in range(iterations):
        #os.system("adb logcat -c")
        launch_settings()
        contact_sync()
        result=test()
        if result:
                pass_cnt+=1
        else:
                fail_cnt+=1
"""            
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

print("pass_cnt,fail_cnt",pass_cnt,fail_cnt)
