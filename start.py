# coding: utf-8
from fwk.base.InitFwk import InitFwk
from projects.PrinterControl.cases.HomeMoreAbout import HomeMoreAbout
from projects.PrinterControl.cases.HomeMoreAppSettings import HomeMoreAppSettings
from projects.WebExample.cases.WebExample import WebExample
from projects.WebMultipleThreads.cases.TestBrowser1 import TestBrowser1
from projects.WebMultipleThreads.cases.TestBrowser import TestBrowser
from projects.IosExample.cases.IosExample import IosExample
import multiprocessing
import unittest
import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

def mutipleProcesses1():
    suite = unittest.TestSuite()
    suite.addTest(TestBrowser("test_flow"))
    suite.addTest(TestBrowser1("test_flow"))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
def mutipleProcesses2():
    suite = unittest.TestSuite()
    suite.addTest(TestBrowser("test_flow"))
    suite.addTest(TestBrowser1("test_flow"))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    initFwk = InitFwk()
    if initFwk.name_project == "PrinterControl":
        listTestSuits = ["test_flow",
                         "test_aioVersion",
                         "test_copyRight",
                         "test_legalInformaion",
                         "test_endUserLicenseAgreement",
                         "test_endUserLicenseAgreement_back",
                         "test_hpOnlinePrivacyStatement",
                         "test_hpOnlinePrivacyStatement_back",
                         "test_shareThisApp",
                         "test_shareThisApp_back",
                         "test_headerDisplay"]
        for suit in listTestSuits:
            suite.addTest(HomeMoreAbout(suit))
        # suite.addTest(HomeMoreAppSettings("test_flow"))
        # suite.addTest(HomeMoreAppSettings("test_verifyCheckbox"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    elif initFwk.name_project == "WebExample":
        suite.addTest(WebExample("test_flow"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    elif initFwk.name_project == "WebMultipleThreads":
        listProcess = []
        t = multiprocessing.Process(target=mutipleProcesses1)
        listProcess.append(t)
        t = multiprocessing.Process(target=mutipleProcesses2)
        listProcess.append(t)
        processes = range(len(listProcess))
        for i in processes:
            listProcess[i].start()
            time.sleep(1)
        for i in processes:
            listProcess[i].join()
    elif initFwk.name_project == "IosExample":
        suite.addTest(IosExample("test_flow"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)

