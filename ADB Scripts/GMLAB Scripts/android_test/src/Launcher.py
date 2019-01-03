import os
from wifi import wifi_sanity
from Monkey import monkey_test
from Alarm2 import alarm_sanity
from airplane import airplane_sanity
import configuration,sys
from datetime import datetime, date
from common import constants
from time import strftime, localtime
from chrome import chrome_sanity
from wallpaper import wallpaper_sanity
from whatsapp import whatsapp_sanity
import wallpaper
from GmMusic import GmMusic_Sanity
from GooglePlayMusic import GoogleMusic_Sanity
from Youtube import Youtube_Sanity
from calculator import calculator_sanity
from Calendar import Calendar_Sanity
from Game import game_sanity
from sms import sms_sanity
import whatsapp
from mobiledata import mobiledata

''' TESTTYPE and COMPONENT lists contain the available test types and components respectively. IF we want to add new component testcases, we should add
the new component name to COMPONENT list'''
TESTTYPE = ["sanity","monkey_test","regression"]
COMPONENT  = ["wifi","monkey","alarm","airplane","bt","chrome","wallpaper","whatsapp"]

'''This function is user to test weather the selected test type is valid or not,return true if invalid and false if valid 
 if the selected type is not valid, it will execute sanity default''' 
def isTesttypeInvalid(testtype):
    if testtype in TESTTYPE:
        return(False)
    else:
        return(True)
'''This function is used to test weather the selected component is valid or not,return true if invalid and false if valid '''  
def iscomponentInvalid(component):
    if component in COMPONENT:
        return(False)
    else:
        return(True)
def setup(): 
    createlog()
    createSummarylog()   
    
def createlog():
    currentTime = strftime("%Y-%m-%d_%H-%M-%S", localtime())
    log_location = "logs\\"+currentTime+".txt"
    print(log_location)
    logfile_absolutepath = os.path.join(os.getcwd(),log_location)
    print(logfile_absolutepath)
    result = os.path.isfile(logfile_absolutepath)
    if not (result):
        fileobj_logfile = open(logfile_absolutepath , 'a+')
        print(fileobj_logfile)
    fileobj_logfile.write("---------------------------------------------------\n")
    fileobj_logfile.write("Id" +"\t"+ "TC_Description"+"\t"+"Result\n")
    fileobj_logfile.write("---------------------------------------------------\n")
    constants.logfile_absolutepath = logfile_absolutepath
    fileobj_logfile.close()

'''This function is used to check if the summaryReport exists, else  create summaryReport '''
def createSummarylog():
    currentTime = strftime("%Y-%m-%d_%H-%M-%S", localtime())
    logsummary_location = "logs\Summary_Report_"+currentTime+".txt"
    logsummary_absolutepath = os.path.join(os.getcwd(),logsummary_location)
    result = os.path.isfile(logsummary_absolutepath)
    if not (result):
        fileobj_logsummary = open(logsummary_absolutepath , 'a+')
        print(fileobj_logsummary)
    fileobj_logsummary.write("---------------------------------------------------\n")
    fileobj_logsummary.write("No.TCS" +"\t"+ "PassCount"+"\t"+"FailCount\n")
    fileobj_logsummary.write("---------------------------------------------------\n")
    print(fileobj_logsummary)
    constants.logsummary_absolutepath = logsummary_absolutepath
    fileobj_logsummary.close()
 
'''This function is used to test weather the any device is conencted or not,  if connected it will return the 1st device id
sandeep : Need to implement to return multiple device ids : pending '''
def isDeviceConnected():
    availableDevicesData = os.popen('adb devices').read().strip().split('\n')[1:]
    if len(availableDevicesData)>0 :
        print("Device connected " , availableDevicesData)
        deviceId = availableDevicesData[0].split('\t')
        return(deviceId[0])
        print(deviceId[0])
    else:
        return(0)
    
''' Main function of launcher'''    
def main(componentlist,testtype,number):
    for i in range(int(number)):
        ''' checking test type selected'''
        if(testtype == TESTTYPE[0]):
            for component in componentlist:
                ''' checking component selected'''
                if(component == COMPONENT[1]):
                    wifi_sanity.TestWifiSanity_main()
                    ''' if no component is selected, all is selected.
                sandeep:  need to modify is required to show error if no component is selected '''
                elif(component == COMPONENT[2]):
                    alarm_sanity.TestAlarmSanity_main()
                elif(component == COMPONENT[3]):
                    airplane_sanity.Airplanetest_Main()
                elif(component == COMPONENT[4]):
                    wifi_sanity.TestWifiSanity_main()
#                     alarm_sanity.TestAlarmSanity_main()
                    airplane_sanity.Airplanetest_Main()
                else:
                    mobiledata.TestMobileDataSanity_main()
                    
                    
                    ''' Main entry to launcher'''
        if(testtype == TESTTYPE[1]):
            ''' checking component selected'''
            for component in componentlist:
                ''' checking component selected'''
                if(component == COMPONENT[1]):
                    monkey_test.Monkey_test_main()
                    ''' if no component is selected, all is selected.'''
                else:
                    return(0)      
if __name__ == '__main__':
    testtype = configuration.testtype.lower()
    componentlist = configuration.component.lower().split(',')
    number = configuration.number
    removelist = []
    print("selected test type is :", testtype)
    print("selected component to test is: ",componentlist)
    print("No of iterations to test is: ",number)
    ''' checking if testtype and component are valid'''
    if(isTesttypeInvalid(testtype)):
        print("invalid testtype hence running sanity")
        testtype = "sanity"
    for component in componentlist:
        if(iscomponentInvalid(component)):
            print(component,"is invalid")
            removelist.append(component)
        else:
            print(component,"is valid")
    print(removelist)  
    for removeitem in removelist:
        componentlist.remove(removeitem)  
    if(len(componentlist) == 0):
        componentlist.append("all")
    print("final list ", componentlist)
    '''Checking if device is connected '''
    Device = isDeviceConnected()
    if not (Device):
        print("Device not connected, hence execution stopped")
        sys.exit()
    print(Device)
    setup()
    main(componentlist,testtype,number)
    