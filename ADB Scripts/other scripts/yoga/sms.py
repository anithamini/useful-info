import os
import sys
import time
#//////////////send message ////////////////
os.system("adb shell am start -a android.intent.action.SENDTO -d sms:+919159495244 --es sms_body 'hi dis is yoga' --ez exit_on_sent true")
os.system("adb shell input keyevent 22")
os.system("adb shell input keyevent 66")
os.system("adb shell input keyevent 3")