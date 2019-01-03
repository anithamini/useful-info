import os
import sys
import time
os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Yoga@innominds' -e phone 9159495244")
#os.system("adb shell am start -a android.intent.action.CALL -d tel:9159495244")
time.sleep(15) 
os.system( "adb shell input keyevent 6")# /// end call after 15 sec