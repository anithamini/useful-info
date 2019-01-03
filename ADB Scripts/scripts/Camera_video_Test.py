###########################
## Camera Preview        ##
###########################
#Front Camera
#adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 1
#Back Camera
#adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0

import os
import sys
import time
import re
import unittest,time

pass_TC = 0
fail_TC = 0
from sys import argv
ITR = argv[1]

os.system('adb wait-for-device root')
os.system('adb wait-for-device remount')
os.system('adb wait-for-device')
print ("-----------------")
os.system("adb wait-for-device shell svc power stayon usb")
time.sleep(2)
os.system("adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME > home.txt")

class main_script():
	def test01_video_Preview(self):
		def camera_Front():
			#os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 1 > camera.txt")
			print("Launching the camera and capturing the video \n")
			#os.system("adb wait-for-device shell input keyevent 3")
			os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")
			time.sleep(10)
			os.system("adb wait-for-device shell input keyevent KEYCODE_CAMERA")
			isCamera_opened("No active camera clients yet")
			print("check 2")
			time.sleep(10)
			os.system("adb wait-for-device shell input keyevent KEYCODE_CAMERA")
			os.system("adb wait-for-device shell input keyevent KEYCODE_BACK")
			#os.system("adb wait-for-device shell input keyevent KEYCODE_BACK")
			os.system("adb wait-for-device shell input keyevent 3")
			time.sleep(5)
			 
	

		def isCamera_opened(arg1):
			global pass_TC
			global fail_TC
			print("check 3")
			os.system("adb shell dumpsys media.camera > cam.txt")
			print("check 4")
			with open('cam.txt') as f:
				lines = f.readlines()
			f.close()
			count = 0
			
			for line in lines:
				if arg1 in line:
					count += 1
			
			if count != 1:
				print ("Camera Preview")
				#take_snap()
				pass_TC +=1
			else:
				print ("Unable to launch camera")
				fail_TC +=1
		for n in range(int(ITR)):
			print ("Itr",n+1)
			print ("------")
			camera_Front()
			
		I = (n+1)+(n+1)
		print ("--------------------------------")
		print ("Total NO.OF Iterations ran : " , I)
		print ("Total NO.OF iterations Passed: %d" %pass_TC)
		print ("Total NO.OF iterations Failed: %d" %fail_TC)
		print ("---------------------------------")

			
if __name__ == '__main__':
	#unittest.main()

	ob=main_script()
	ob.test01_video_Preview()