import os
import sys
import time
import re
import unittest,time
print("=======================================================================")
print("Launching Calendar")
print("=======================================================================")

#os.system("adb shell")
#os.system("dumpsys window windows |grep -E 'mCurrentFocus'")
os.system("adb shell am start -n com.android.calendar/com.android.calendar.homepage.AllInOneActivity")

