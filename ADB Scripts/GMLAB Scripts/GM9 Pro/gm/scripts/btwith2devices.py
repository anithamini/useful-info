import sys
import os
import time

def connectDevice(): 
    print ("Establishing the connection")
    global device
    deviceIds = []    
    global selectedDeviceId
    selectedDeviceId = None
    try:
        #detect multiple devices and ask user to select a device to run the scripts
        availableDevicesData = os.popen('adb devices').read().strip().split('\n')[1:]
        print(availableDevicesData)   
        iteratePosition = 1
        print ("Available devices list:")
        for data in availableDevicesData:
            deviceId = data.split('\t')[0]
            print ("%d. %s" % (iteratePosition, deviceId))
            deviceIds.append(deviceId)
            iteratePosition = iteratePosition + 1
            #print(deviceIds[0])
        if(len(deviceIds)<2):
            return 0           
        return(deviceIds)
    except:
        print ("Please connect device")

def f():
    os.system("adb -s " + deviceIds[i] + " shell input keyevent 20")
    os.system("adb -s " + deviceIds[i] + " shell input keyevent 66")
    time.sleep(3)

def pairing():
    os.system( "adb -s " + deviceIds[1] + " shell dumpsys bluetooth_manager > bt.txt")
    address: B8:DE:5E:00:A0:00
    
deviceIds = connectDevice()
print(deviceIds)
if(not(deviceIds)):
    print("Minimum 2 devcies need to be connected to run the MT test")
else:
    print("Bluetooth pairing starts...................")
    for i in range(0,2):
        os.system("adb -s " + deviceIds[i] + " shell am start -a android.settings.BLUETOOTH_SETTINGS")  
        if(i==0):
                f()
        else:


            for j in range(0,2):
                f()





        
