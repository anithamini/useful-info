'''
Created on 20-Jul-2018

@author: galluri
'''
import os
import time
import random
import re
from datetime import datetime
from time import strftime,localtime
from common import constants

def bootuptime_Sanity():
    print(constants.logfile_absolutepath)
    global fileobj_logfile
    fileobj_logfile =open(constants.logfile_absolutepath , 'a+')
    fileobj_logfile.write("\nBootup time \n")
    fileobj_logfile.write("---------------------------------------------------\n")
    currentTime = strftime("%H.%M.%S", localtime())
    time = datetime.now()
    then = time.time() #Time before the operations start
#     print("Initiated the device reboot at:",currentTime)
    flag=0
    os.system("adb reboot")
    fileobj_logfile.write("please wait your device is off..." ) 
    while(flag!=os.system("adb shell getprop sys.boot_completed")):
        fileobj_logfile.write('.')    
    fileobj_logfile.write("device is on")
    now = time.time() #Time before the operations start
    result = now-then
    fileobj_logfile.write("It took: ", result, " seconds for booting")

def bootuptime_main():
    print("---------------------------Boot up Time sanity-------------------------------")
    bootuptime_Sanity()


#RCSService BC-Receiver: Boot Complete Event Received 
 
