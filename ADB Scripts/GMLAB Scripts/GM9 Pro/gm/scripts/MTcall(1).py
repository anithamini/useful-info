import os
import sys
import time
import re
import unittest,time

def connectDevice(): 
    print ("Establishing the connection")
    global device
    deviceIds = 0    
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
            #print(deviceIds)
        if(len(deviceIds)<2):
            return 0           
        return(deviceIds)
    except:
        print ("Please connect device")
deviceIds = connectDevice()
print(deviceIds)
if(not(deviceIds)):
    print("Minimum 2 devcies need to be connected to run the MT test")
else:    
    adb_command = "adb -s " + deviceIds[0] + " shell am start -a android.intent.action.CALL -d tel:9030676276" 
    #adb_command = "adb -s " + deviceIds[0] + " shell pm list packages" 
    print(adb_command)
    os.system(adb_command)
    time.sleep(10)
    adb_command = "adb -s " + deviceIds[1] + " shell dumpsys telephony.registry > MTcall_receivedlog.txt "
    os.system( adb_command)
    