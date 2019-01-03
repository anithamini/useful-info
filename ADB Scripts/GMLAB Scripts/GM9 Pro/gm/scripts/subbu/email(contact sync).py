import os
import sys
import time
iterations=2
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
        time.sleep(1)
        os.system("adb shell input keyevent 66")       
        os.system("adb shell input keyevent 66")
        print("gmail account is synced with contacts")
        time.sleep(5)
def kill_settings():
        os.system("adb shell am force-stop com.android.settings")
def test():
    print("before")    
    os.system("adb logcat -d >sync.txt")
    print("after")
    s1="ContactsSyncAdapter: @onPerformSync Sync finished successfully" 
    cnt=0
    with open("sync.txt","r") as fh:
        while 1:
                buf=fh.readline()
                if (buf==""):
                        break
                if(s1 in buf):
                        cnt+=1
                       
        print(cnt)        
        return cnt     

            
kill_settings()     
for i in range(int(iterations)):
        launch_settings()
        contact_sync()
        result=test()
        if result==i+1:
                pass_cnt+=1
        else:
                fail_cnt+=1
kill_settings()

print("pass_cnt,fail_cnt",pass_cnt,fail_cnt)


"""
with open("sync.txt","r",encoding="utf8") as fh:
            while(buf!=''):
                    buf=fh.readline()
                    if(s1 in buf):
                            cnt+=1
                
            return cnt
"""            
