import os
import sys
import time


iterations=sys.argv[1]
launch_pass_cnt=0
launch_fail_cnt=0
campic_pass_cnt=0
campic_fail_cnt=0
video_pass_cnt=0
video_fail_cnt=0

def kill_camera():
    os.system("adb shell input keyevent 3")
def launch_camera():
    os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
    time.sleep(2)
def capture_camera():
    os.system("adb shell input keyevent KEYCODE_CAMERA")
def save():
    time.sleep(5)
    os.system("adb shell input tap 786 1854")
def video_camera():
    print("---------")
    os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")
    time.sleep(5)
    os.system("adb shell input keyevent ")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(5)
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    time.sleep(2)
    os.system("adb shell input keyevent 4")

def validate(s):
    os.system("adb shell dumpsys activity >cam.txt")
    with open("cam.txt","r+") as fh:
        buf=fh.read() 
        if s in buf:
            return 1
        else:
            return 0
        
kill_camera()
for i in range(int(iterations)):
    launch_camera()
    if(validate("packageName=org.codeaurora.snapcam processName=org.codeaurora.snapcam")):
        launch_pass_cnt+=1
        capture_camera()
        if(validate("act=com.android.camera.NEW_PICTURE")):
            campic_pass_cnt+=1
            save()
        else:
           campic_fail_cnt+=1
        time.sleep(5)
        video_camera()
        if(validate("act=android.media.action.VIDEO_CAPTURE")):
            video_pass_cnt+=1
        else:
            video_fail_cnt+=1
    else:
       launch_fail_cnt+=1
    kill_camera()
print("launch_pass_cnt:",launch_pass_cnt,"launch_fail_cnt:",launch_fail_cnt)
print("campic_pass_cnt:",campic_pass_cnt,"campic_fail_cnt:",campic_fail_cnt)
print("video_pass_cnt:",video_pass_cnt,"video_fail_cnt:",video_fail_cnt)





