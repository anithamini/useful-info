'''
Created on 16-Jul-2018

@author: galluri
'''
#/************************************************************************
# * Copyright (C) 1998-2016 Connected Devices, Innominds Software Pvt Ltd.
# *
# * This file is part of Connected Devices Project
# *
# * Connected Devices Project and associated code can not be copied
# * and/or distributed without a written permission of
# * Innominds Software Pvt Ltd., and/or it subsidiaries
# *
# * Description: This module script called when smoketest invokes the
#                btcheck.
#* For any modification contact @Ramamohan (rbandapalli@innominds.com)
#************************************************************************/
import os
import time
import re
import datetime
import sys
import configuration

#
#device_id="de4de013"

device_id = configuration.deviceID.lower()

class Monkey_test:

    def device_status(self):
        self.count=20
        while (self.count!=0):
            print("checking device state ")
            if (re.match("device", os.popen("adb get-state").read()) == None):
                time.sleep(1)
                os.system("adb kill-server")
                self.count=self.count-1
            else:
                print("device found")
                return 1
        else:
            print("Here manual intervention is required .")
            print("Device not connected to host machine or device went into bad state")
            return 0

    def monkey_test(self):
        print("Staring Monkey command")
        time.sleep(10)
        Start_time = datetime.datetime.now()
        os.system(
            "adb shell monkey -s 950 --throttle 500 -v --ignore-timeouts --ignore-crashes --ignore-security-exceptions  --kill-process-after-error --pct-trackball 12  --pct-touch 35 --pct-motion 10 --pct-nav 3 --pct-syskeys 5 --pct-appswitch 10 --pct-anyevent 1 --pct-flip 15 --pct-majornav 9 10  > monkey_console.txt ")
        End_time = datetime.datetime.now()
        Time_difference = End_time - Start_time
        print(Time_difference)
        Time_difference_minsec = divmod(Time_difference.days * 86400 + Time_difference.seconds, 60)
        #print(Time_difference_minsec)
        print("=====================================================================")
        print("Monkey test ran for {}mins and {}seconds".format(Time_difference_minsec[0], Time_difference_minsec[1]))
        cwd= os.getcwd()
        print (cwd)
        os.system(cwd + "\qcomlog-dump.bat")
        print ("log created")

    def device_logging(self):
        print("Started capturing the logs")
        #cmd1 = "perl logs.pl" + ' ' + device_id
        #os.system(cmd1)
        
        

def Monkey_test_main():
    print("entry of MonkeyTest_main")
    ob=Monkey_test()
    result=ob.device_status()
    if(result==1):
        ob.device_logging()
        time.sleep(10)
        ob.monkey_test()
    else:
        print("Script exited")
    
