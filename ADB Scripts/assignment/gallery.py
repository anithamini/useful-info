                             #Gallery/File Manager

import os
import time

def kill_gallery():
    print("=======================================================================")
    print("Killing background process of Chrome")
    print("=======================================================================")
    os.system("adb shell am force-stop com.miui.gallery")

def launch_gallery():
    print("=======================================================================")
    print("Launching chrome")
    print("=====================================================================
    os.system("adb shell am start -n com.miui.gallery/com.miui.gallery.activity.HomePageActivity")
def gallery_folder():
    os.system("adb shell input tap 409 95")
    os.system("adb shell input tap 268 387")
    os.system("adb shell input keyevent 4")
kill_gallery()
launch_gallery()
for n in range(0,3):
    gallery_folder(n)
    time.sleep(5)
kill_gallery()

