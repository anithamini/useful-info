import os
import time

fs=open("mcts.txt","r")
while 1:
    reg=fs.readline()
    if (reg ==""):
        break
    buf=reg.split()
    os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name "+buf[0]+" " +" -e phone "+buf[2])
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    os.system("adb shell am force-stop com.android.contacts")
        

