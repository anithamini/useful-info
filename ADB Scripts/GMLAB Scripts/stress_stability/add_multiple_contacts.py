import os
import time
import sys
fs=open("mcts.txt","r+")
pass_cnt=0
fail_cnt=0
itr=int(sys.argv[1])
while itr:
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
    if(reg==""):
        pass_cnt+=1
    else:
        fail_cnt+=1
    itr-=1       

print("pass_cnt ",pass_cnt)
print("fail_cnt ",fail_cnt)
