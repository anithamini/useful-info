'''
Created on 20-Jul-2018

@author: galluri
'''
import os

def logpath():
    logfilepath = os.path.join(os.getcwd(),"logs\bootuplog.txt")
    print(logfilepath)
    result = os.path.isfile(logfilepath)
    print(result)
    global fileobj
    fileobj = open(logfilepath , 'a+')
    print(fileobj)