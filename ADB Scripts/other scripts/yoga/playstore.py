import os
import sys
import time
import re
import unittest,time

def kill_playstore():
    os.system("adb shell am force-stop com.android.vending ")
    
def launch_playstore():
    os.system("adb shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
   
def search_app():
    os.system("adb shell input keyevent 84")
    #str1=input("enter the app name to download")
    #print(str1)
    os.system("adb shell input text 'facebook lite'")
    #os.system("adb shell input text "+str1)
    time.sleep(3)
    os.system("adb shell input keyevent 66")
    time.sleep(3)
    os.system("adb shell input tap 533 588")
    time.sleep(3)
    
def check_download():

    flag=1
    while(flag):
        os.system("adb shell pm list package -3>package.txt")
        fp=open("package.txt","r")
        buf1=fp.read()
        if (re.search("facebook",buf1,re.I)):
            #if(str1 in buf1):  
            #  print(buf1)
            print("your app is installed")
            flag=0
           
         
kill_playstore()
launch_playstore()  
search_app()
check_download()
print("opening application")
kill_playstore()
launch_playstore()
search_app()



 
