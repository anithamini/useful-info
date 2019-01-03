                                    #GOOGLE PLAY MUSIC APPLICATION LAUNCH,PLAY,PAUSE and RESUME
    
import os
import sys
import time
def launch_Google_play_music():
    print("Launching Google play music application......")
    os.system("adb shell am start -n com.google.android.music/com.android.music.activitymanagement.TopLevelActivity")
    time.sleep(3)
def operations():
    print("Searching music....")
    #os.system("adb shell input keyevent 84")
    os.system("adb shell input tap 666 109")
    os.system("adb shell input text Shape")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 22")
    print("Music is playing.....")
    os.system("adb shell input keyevent 66")
    os.system("adb shell input tap 324 1219")
    #os.system("adb shell input keyevent 126") //For lastly played song
    time.sleep(10)
    """
   # In MI these commands are not working...
    print("Music Forward....")
    os.system("adb shell input keyevent 125")
    time.sleep(10)
   # In MI these commands are not working....
    print("Recording media music.....")
    os.system("adb shell input keyevnt 130")
    time.sleep(15)
    """
    print("Pausing the music....")
    os.system("adb shell input keyevent 127")
    time.sleep(10)
    print("Resuming music.....")
    os.system("adb shell input keyevent 85")#can use 85 for both play and pause
    time.sleep(10)
def kill_Google_play_music():
    print("Killing background Google play music application.......")
    os.system("adb shell am force-stop com.google.android.music")
#Main program
kill_Google_play_music()
launch_Google_play_music()
operations()


