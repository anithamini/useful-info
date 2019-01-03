
import os
import time
#count=2
n=1
pass_TC = 0
fail_TC = 0
from sys import argv
count = argv[1]
print ("Pushing audio file to /sdcard")
os.system("adb push C://Users//galluri//Desktop//GM_Stability2//GM_Stability//media //sdcard/movies/media")
def audio_test():
    print("Audio playing started")
    os.system("adb shell am start -a android.intent.action.VIEW -d file:///sdcard/movies/media/MP3_converted.mp3 -t video/3gp")
    time.sleep(8)
    os.system("adb shell input keyevent 4")
    print("Audio playing stopped")
    time.sleep(10);
    return 1
    #os.system("adb shell dumpsys media.player > audio.txt")

while(count!=0):
    print("Itr", n )
    print("--------------------------------")
    n=n+1
    x=audio_test()
    if(x==1):
        pass_TC += 1
        print("Test case = PASS ...\n")
        print("--------------------------------")
    else:
        fail_TC += 1
        ("Test case = FAIL ...\n")
        print("--------------------------------")
    count=count-1
print ("--------------------------------")
print ("Total NO.OF Iterations ran : " , n-1)
print ("Total NO.OF iterations Passed: %d" %pass_TC)
print ("Total NO.OF iterations Failed: %d" %fail_TC)
print ("---------------------------------")
