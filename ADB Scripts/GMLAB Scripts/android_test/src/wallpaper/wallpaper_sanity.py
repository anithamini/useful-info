'''
Created on Jul 24, 2018

@author: akesiboyina
'''
import os
import time
from common import constants
pass_cnt=0
fail_cnt=0
i=0
print("-----------WALLPAPER------------")

def kill_settings():
    os.system("adb shell am force-stop com.android.settings")

def wallpaper_setting():  
    global pass_cnt
    global fail_cnt
    global fileobj_logfile
    #os.system("adb shell am start -n com.android.settings/.DisplaySettings")     #to launch settings         
    os.system("adb shell input touchscreen swipe 480 1056 480 1056 1000")
    os.system("adb shell input keyevent 20")   
    os.system("adb shell input keyevent 20")   
    os.system("adb shell input keyevent 66") 
    os.system("adb shell input keyevent 22")                     #to move right side
    time.sleep(2)
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input tap 517 88")                #to tap on set wallpaper
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 4")
    if(validate()):
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "wallpaper_setting"+"\t"+"PASS\n")
        pass_cnt+=1
    else:
        fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
        fileobj_logfile.write("TC_1" +"\t"+ "wallpaper_setting"+"\t"+"FAIL\n")
        fail_cnt+=1

def validate():
    s1="packageName=com.android.wallpaperpicker processName=com.android.wallpaperpicker"
    os.system("adb shell dumpsys activity >wall.txt")              #to collect activity logs
    with open("wall.txt","r+") as fh:
        buf=fh.read() 
        if s1 in buf:
            return 1
        else:
            return 0

def TestWallpaperSanity_testsuit():    
    kill_settings()
    wallpaper_setting()
    kill_settings()
    
def TestWallpaperSanity_Setup():
     
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nWallpaper_sanity\n")
    fileobj_logfile.write("---------------------------------------------------\n")

def Wallpaper_sanity_summary_log():
    global pass_cnt
    global fail_cnt
    print("Pass Count:",pass_cnt,",Fail Count:",fail_cnt)
    '''Below code is used to get summary report'''
    print(constants.logsummary_absolutepath)
    global fileobj_logsummary
    fileobj_logsummary =open(constants.logsummary_absolutepath , 'a+')
    fileobj_logsummary.write("\nwallpaper_sanity\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write(str(pass_cnt+fail_cnt)+"\t" + str(pass_cnt) +"\t"+ str(fail_cnt)+"\n")
    fileobj_logsummary.write("\n---------------------------------------------------\n")
    fileobj_logsummary.close()
    #pass_cnt=0
    #fail_cnt=0
    
def TestWallpaperSanity_main():
   
    print("entry of TestWallpaperSanity_main")
    TestWallpaperSanity_Setup()
    TestWallpaperSanity_testsuit()
    Wallpaper_sanity_summary_log()
    
    
    
    """
    for i in range(0,3):
        time.sleep(2)
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")   
    for i in range(0,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    """
