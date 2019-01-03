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
import sys
import time
import re
import unittest,time
#import configparser
#import shutil
#import HTMLTestRunner
#reload(HTMLTestRunner)
print("=======================================================================")
print("Stability test started")
print("=======================================================================")
pass_TC = 0
fail_TC = 0
#Settings.ActionLogs=False

#myPath= os.path.dirname(getBundlePath())
myPath= os.path.dirname(__file__)
#print myPath
#print "Current dir : %s" %myPath
ret = os.path.isdir("%s\TestReport" %myPath)   # Creating test report dir	
if ret == True:
	pass
if ret == False:
	os.mkdir("%s\TestReport" %myPath)
report_dir = "%s\TestReport" %myPath

os.system('adb wait-for-device root')
os.system('adb wait-for-device remount')
os.system('adb wait-for-device')
print ("-----------------")
os.system("adb wait-for-device shell svc power stayon usb")
time.sleep(2)
#os.system("adb wait-for-device shell input keyevent 82")
os.system("adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME > home.txt")
from sys import argv
ITR = argv[1]

class main_script():
	def test01_loadpage(self):
		def pageload():
			#os.system("adb wait-for-device shell service call bluetooth_manager 8 > bt.txt")
			os.system("adb shell am start -a android.intent.action.VIEW -d https://www.amazon.com/")
			time.sleep(5)
		
		def close(arg1):
			global pass_TC
			global fail_TC
			os.system("adb shell am force-stop com.android.chrome")
			count = 0
			for line in lines:
				if arg1 in line:
					count += 1
			if count == 1:
				print (" BT enabled")
				disable_BT()
				print (" BT Disabled")
				pass_TC +=1
			else:
				print (" Unable to turn on Blue tooth")
				fail_TC +=1
		for n in range(int(ITR)):
			print ("Itr",n+1)
			print ("---------------------------")
			enable_BT()
			get_status('enabled: true')
		print ("--------------------------------")
		print ("Total NO.OF Iterations ran : " , n+1)
		print ("Total NO.OF iterations Passed: %d" %pass_TC)
		print ("Total NO.OF iterations Failed: %d" %fail_TC)
		print ("---------------------------------")

			
if __name__ == '__main__':
	#unittest.main()
	ob=main_script()
	ob.test01_loadpage()

	