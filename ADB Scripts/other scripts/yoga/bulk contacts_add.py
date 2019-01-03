#list.txt contain your name and number
import os
import time
with open("list.txt","r+") as fp:	
    while 1:
        buf=fp.readline()
        print(buf)
        if buf=="" :
            break
        reg=buf.split()
        os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name "+reg[0]+" " +" -e phone "+reg[1])
        os.system("adb shell input keyevent 3")
        os.system("adb shell am force-stop com.android.contacts")
    
        

        
    
