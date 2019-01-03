                                   #Video call


import os
import time
def Kill_whatsapp():
    print("-----------killing background process of whatsapp--------")
    os.system( "adb shell am force-stop com.whatsapp")
def Launch_whatsapp():
    print("-----------Launching whatsapp to foreground--------------")
    os.system( "adb shell am start -n com.whatsapp/.Main")
def videocall_whatsapp():
    print("-----------making whatsapp videocall--------------")
    os.system("adb shell input keyevent 22")
    time.sleep(2)
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input tap 619 1195")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text bhavani")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
def end_call():
     print("-----------ending whatsapp videocall--------------")
     os.system("adb shell input tap 368 956")
     
def whatsapp():
    Kill_whatsapp()
    Launch_whatsapp()
    videocall_whatsapp()
    time.sleep(5)
    end_call()
    Kill_whatsapp()
#----------------------------imo------------------------------#
def Kill_imo():
    print("-----------killing background process of imo--------")
    os.system( "adb shell am force-stop com.imo.android.imoim")
def Launch_imo():
    print("-----------Launching imo to foreground--------------")
    os.system( "adb shell am start -n com.imo.android.imoim/com.imo.android.imoim.activities.Home")
def videocall_imo():
    print("-----------making imo videocall--------------")
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text manasa")
    os.system("adb shell input tap 636 339") 
def endcall_imo():
    print("-----------ending imo videocall--------------")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 66")
def imo():
    Kill_imo()
    Launch_imo()
    videocall_imo()
    time.sleep(5)
    endcall_imo()
    Kill_imo()
for i in range(1,3):
    whatsapp()
time.sleep(5)
for i in range(1,3):
    imo()

