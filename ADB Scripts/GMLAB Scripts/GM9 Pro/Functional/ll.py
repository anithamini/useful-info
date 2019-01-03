import os
os.system("adb logcat -c")
os.system("adb logcat -m 100 >log.txt")
