import os
import sys
import time
import re
import unittest,time
#from sys import argv
os.system("adb shell am start -a android.intent.action.SENDTO -d sms:+919640281782 --es sms_body 'hiiiiiiii' --ez exit_on_sent true")
os.system("adb shell input keyevent 22")
os.system("adb shell input keyevent 66")

 
