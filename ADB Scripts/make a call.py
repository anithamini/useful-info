#import os
#import sys
#import time
#os.system("adb shell input tap 90 1187")
#os.system( "adb shell input keyevent 5")
#
#os.system( "adb shell input text 6300347124")
#os.system("adb shell input tap 363 1108")
#os.system( "adb shell input keyevent 5")
#)
#////////////make call///////////
#os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Yoga@innominds' -e phone 9159495244")
#os.system("adb shell am start -a android.intent.action.CALL -d tel:9159495244")
#time.sleep(15) 
#os.system( "adb shell input keyevent 6")# /// end call after 15 sec
#//////////////send message ////////////////
#os.system("adb shell am start -a android.intent.action.SENDTO -d sms:+919159495244 --es sms_body 'hi dis is yoga' --ez exit_on_sent true")
#os.system("adb shell input keyevent 22")
#os.system("adb shell input keyevent 66")
#os.system("adb shell input keyevent 3")
#/////////////
"""os.system("adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
os.system("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")
os.system("adb shell service call bluetooth_manager 6")
os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings")"""
#////////
#os.system("adb shell svc wifi enable")
#os.system("adb shell svc wifi disable")

#/////////pull contact to desktop
#os.system("adb pull /data/data/com.android.providers.contacts/databases/contacts2.db /Desktop")
