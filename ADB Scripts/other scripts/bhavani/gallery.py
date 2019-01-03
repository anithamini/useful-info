import os
import time

def Kill_gallery():
    os.system( "adb shell am force-stop com.android.gallery3d")

def launch_gallery():
    os.system("adb shell monkey -p com.android.gallery3d 1")

def camera_images():
    os.system("adb shell input tap 190 400")
    print("in camera....")
    time.sleep(2)
    os.system("adb shell input tap 380 510")
    time.sleep(2)
    delete_image()
    back()
def screenshot_images():
    os.system("adb shell input swipe 250 1000 250 450")
    os.system("adb shell input tap 200 500")
    time.sleep(2)
    os.system("adb shell input tap 380 510")
    time.sleep(1)
    back()
def back():
    os.system("adb shell input keyevent 4")

def delete_image():
    os.system("adb shell input tap 680 100")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
    print("....image deleted.....")

Kill_gallery()
launch_gallery()
time.sleep(2)
camera_images()
time.sleep(2)
back()
screenshot_images()
time.sleep(2)
Kill_gallery()
