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

print (report_dir)
print (ret)
print (myPath)

from sys import argv
ITR = argv[1]

os.system('adb wait-for-device root')
os.system('adb wait-for-device remount')
os.system('adb wait-for-device')
print ("-----------------")
os.system("adb wait-for-device shell svc power stayon usb")
time.sleep(2)
#os.system("adb wait-for-device shell input keyevent 82")
os.system("adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME > home.txt")
os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings > wifi.txt")

class main_script():
	def test01_WiFi_on_off(self):

		def enable_Wifi():
			#os.system('adb wait-for-device shell svc wifi enable')
			os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
			os.system("adb shell input keyevent 19")
			os.system("adb shell input keyevent 23")
			time.sleep(10)
		def disable_Wifi():
			#os.system('adb wait-for-device shell svc wifi disable')
			os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
			os.system("adb shell input keyevent 19")
			os.system("adb shell input keyevent 23")
			time.sleep(5)
		def CheckWiFiState(arg):
				global pass_TC
				global fail_TC
				os.system( "adb shell dumpsys wifi > wlan.txt")
				file = open("wlan.txt","r+")
				red = file.readline();
				file.close()
				m = re.search(arg, red, re.I)
				if m:
					print (" Wifi is Enabled ")
					disable_Wifi()
					print (" Wifi is Disabled ")
					pass_TC +=1
					#return True
				else:
					print ("Unable to turn on Wifi")
					fail_TC +=1
					#return False
		for n in range(int(ITR)):
			print ("Itr",n+1)
			print ("------")
			enable_Wifi()
			CheckWiFiState('Wi-Fi is enabled')
		print ("--------------------------------")
		print ("Total NO.OF Iterations ran : " , n+1)
		print ("Total NO.OF iterations Passed: %d" %pass_TC)
		print ("Total NO.OF iterations Failed: %d" %fail_TC)
		print ("---------------------------------")

if __name__ == '__main__':
	#unittest.main()
	ob=main_script()
	ob.test01_WiFi_on_off()

	
