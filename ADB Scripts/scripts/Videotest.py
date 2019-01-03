import time
import os
import time
#count=2
n=1
pass_TC = 0
fail_TC = 0
from sys import argv
count = int (argv[1])
print ("Pushing audio and video to /sdcard")
os.system("adb push C://Users//galluri//Desktop//GM_Stability2//GM_Stability//media //sdcard/movies/media/")
def video_test():
    os.system("adb shell input keyevent 4")
    print("Video is playing")
    os.system("adb shell am start -a android.intent.action.VIEW -d file:///sdcard//movies//media//1080p_30fps_128kbps.mp4 -t video/3gp")
    time.sleep(10)
    os.system("adb shell input keyevent 26")
    time.sleep(2)
    os.system("adb shell input keyevent 26")
    time.sleep(2)
    os.system("adb shell input keyevent 82")
    time.sleep(5)
    os.system("adb shell am start -a android.intent.action.VIEW -d file:///sdcard//movies//media//MP3_converted.mp3 -t video/3gp")
    time.sleep(20)
    os.system("adb shell input keyevent 4")
    print("video stopped")
    time.sleep(10);
    #os.system("adb shell dumpsys media.player > audio.txt")
    return 1

while(count!=0):
    print("Itr", n )
    print("--------------------------------")
    n=n+1
    x=video_test()
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

