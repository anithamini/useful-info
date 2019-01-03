from os import system
from time import sleep
Iterations=3
P_Cnt=0
F_Cnt=0
def Checkstate():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    with open("wifi_log.txt","r") as fd:
        buffer = fd.readline()
    res = re.search('mAirplaneModeOn false', buffer, re.I)
    if res:
        return(True)
    else:
        return(False)
def toggle_airplane_mode():
    system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    sleep(1)
    print("Airplane mode is enabling....")
    system("adb shell input tap 656 1072")
    sleep(5)
    if(Checkstate()):
        P_Cnt+=1
    else:
        F_Cnt+=1
    print("Airplane mode is disabling....")
    system("adb shell input tap 656 1072")
    sleep(5)
    if(Checkstate()):
        P_Cnt+=1
    else:
        F_Cnt+=1
    system("adb shell input keyevent 3")
for i in range(0,3):
    toggle_airplane_mode()
print("Pass count:",P_Cnt,"Fail count:",F_Cnt)
