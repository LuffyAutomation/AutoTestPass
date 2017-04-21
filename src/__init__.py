__author__ = 'Wendy'
import os
import sys

#from utils import commonUtils as cmnu
'''from po.AndroidFWK import Android

from selenium import webdriver
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)
'''
'''desired_caps = {}
desired_caps['platformName']= 'Android'
desired_caps['browserName'] = ''
desired_caps['version'] = '4.4'
desired_caps['newCommandTimeout'] = '2000'
desired_caps['app'] = PATH('C:/Users/Wendy/Desktop/builds/android/ePrint-3.3-debug-RC5-VC86.apk')
desired_caps['app-package'] = 'com.hp.android.print'
desired_caps['app-activity'] = 'com.hp.android.print.welcome.WelcomeActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)'''
#c = cmnu.common()
#c.getRoot()
'''ads = Android()
value = ads.getAppType("test")
print("aaa" + value)
print (cmnu.common.getRoot(""))
data = configparser.ConfigParser()
#path_= os.chdir(os.getcwd()+os.sep+'../')
tmp = os.getcwd()+os.sep+'../'+os.sep+'resources'+os.sep+'data'+os.sep+'main.data'
print (tmp)
#data.read("../resources/data/main.data")
data.read(tmp)
s = data.sections()
print ('section:', s)
name = data.get("main" ,"data.uiMaps.AndroidApp.xml")
print(name)'''





