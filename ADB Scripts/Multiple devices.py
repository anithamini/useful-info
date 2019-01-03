import os
import time

os.system("adb -s 0123456789ABCDEF shell am start -a android.intent.action.SENDTO -d sms:+919100205816 --es sms_body 'hiiiiiiii' --ez exit_on_sent true")
os.system("adb -s 0123456789ABCDEF shell input tap 651 1270")
time.sleep(5)

os.system("adb -s B1669106231 shell am start -a android.intent.action.SENDTO -d sms:+919100205163 --es sms_body 'hiiiiiiii' --ez exit_on_sent true")
os.system("adb -s B1669106231 shell input tap 651 1270")
