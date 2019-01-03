import os
import time
import random
then = time.time() #Time before the operations start
flag=0
os.system("adb reboot")
print("please wait your device is off...",end=' ')
while(flag!=os.system("adb shell getprop sys.boot_completed")):
	#print('.',end=' ')	
print("device is on")
now = time.time() #Time before the operations start
print("It took: ", now-then, " seconds for booting")
