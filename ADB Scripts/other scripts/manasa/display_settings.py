import os
import time
import sys

def launch_display_settings():
    print("............Opening the DISPLAY Settings............")
    os.system("adb shell am start -n com.android.settings/.DisplaySettings")

def change_brightness():
    #the brightness level range is in between 1-255 or 0-254
    print("Changing the Brighness level from MINIMUM to MAXIMUM")
    os.system("adb shell settings put system screen_brightness 255")
    time.sleep(3)
    print("Changing the Brightness level from MAXIMUM to MINIMUM")
    os.system("adb shell settings put system screen_brightness 1")

def auto_brightness():
    print("toggle auto brighness")
    os.system("adb shell input tap 555 425")
    print("auto brightness mode is ON")
    #print("Brightness level is:")
    #os.system("adb shell settings get system screen_brightness")       
    time.sleep(3)
    os.system("adb shell input tap 555 425")
    print("auto brightness mode is OFF")
    #print("Brightness level is:")
    #os.system("adb shell settings get system screen_brightness")
    #time.sleep(3)

def change_wallpaper():
    for i in range(1,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 66")
    print("........Selecting the Wallpaper for lockscreen.......")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 4")
    os.system("adb shell input keyevent 4")

def change_sleep():
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
    
def change_screen_rotation():
    print("screen  auto rotation is enabled")
    os.system("adb shell settings put system accelerometer_rotation 1")
    print("screen  auto rotation is disabled")
    os.system("adb shell settings put system accelerometer_rotation 0")

def font_style(): 
    for i in range(1,4):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 4")

def font_size():
    for i in range(1,3):
        os.system("adb shell input keyevent 20")
        os.system("adb shell input keyevent 66")
    
def kill_display():
    os.system("adb shell am force-stop com.android.settings")

launch_display_settings()
change_brightness()
print("the brightness is adjusted\n")
auto_brightness()
change_wallpaper()
print("lockscreen image is set")
change_sleep()
print("sleep is set for some sec delay")
change_screen_rotation()
font_style()
print("the default font style is set")
font_size()
print("the font size iz set")
print("...........Closing the Settings........")
kill_display()



    
    
