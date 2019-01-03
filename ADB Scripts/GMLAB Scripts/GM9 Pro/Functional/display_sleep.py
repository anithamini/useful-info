import os
import time
import sys

def launch_display_settings():
    print("............Opening the DISPLAY Settings............")
    os.system("adb shell am start -n com.android.settings/.DisplaySettings")

def change_sleep():
    for i in range(1,6):
        os.system("adb shell input keyevent 20")
    for i in range(2):
        os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 433 969")
    
def kill_display():
    os.system("adb shell am force-stop com.android.settings")


print("...........Closing the Settings........")
kill_display()

print("...........Opening the Settings........")
launch_display_settings()

change_sleep()
print("sleep is set for some sec delay")

print("...........Closing the Settings........")
kill_display()



    
    
