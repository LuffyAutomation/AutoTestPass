# coding: utf-8
from fwk.base.InitFwk import InitFwk
from fwk.utils.utilMultiple.UtilMultipleThreads import UtilMultipleThreads
from projects.PrinterControl.cases.HomeMoreAbout import HomeMoreAbout
from projects.PrinterControl.cases.HomeMoreAppSettings import HomeMoreAppSettings
from projects.PrinterControl.cases.TilePersonalize import TilePersonalize
from projects.HPSmart.cases.HomeMoreAbout import HomeMoreAbout
from projects.HPSmart.cases.HomeMoreAppSettings import HomeMoreAppSettings
from projects.HPSmart.cases.HomeMoreHelpCenter import HomeMoreHelpCenter
from projects.HPSmart.cases.Files import Files
from projects.WebExample.cases.WebExample import WebExample
from projects.WebMultipleThreads.cases.TestBrowser1 import TestBrowser1
from projects.WebMultipleThreads.cases.TestBrowser import TestBrowser
from projects.IosExample.cases.IosExample import IosExample
from projects.HPSmartiOS.cases.HomeFistLaunchiOS import HomeFistLaunchiOS
import multiprocessing
import unittest
import time

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# print platform.python_version()

def mutipleThread1():
    suite = unittest.TestSuite()
    # suite.addTest(TestBrowser("test_flow"))
    suite.addTest(TestBrowser1("test_flow"))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

def mutipleThread2():
    suite = unittest.TestSuite()
    # suite.addTest(TestBrowser("test_flow"))
    suite.addTest(TestBrowser1("test_flow"))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':

   # "耗材购买".decode("utf-8")

    suite = unittest.TestSuite()
    initFwk = InitFwk()
    if initFwk.name_project == "PrinterControl":
        from projects.PrinterControl.cases.HomeMoreAbout import HomeMoreAbout
        # listTestSuits = ["test_flow"
        #                  # ,
        #                  # "test_aioVersion",
        #                  # "test_copyRight",
        #                  # "test_legalInformaion",
        #                  # "test_endUserLicenseAgreement",
        #                  # "test_endUserLicenseAgreement_back",
        #                  # "test_hpOnlinePrivacyStatement",
        #                  # "test_hpOnlinePrivacyStatement_back",
        #                  # "test_shareThisApp",
        #                  # "test_shareThisApp_back",
        #                  # "test_headerDisplay"
        #                  ]
        # for suit in listTestSuits:
        #     suite.addTest(TilePersonalize(suit))
        from projects.PrinterControl.cases.HomeMoreAppSettings import HomeMoreAppSettings
        suite.addTest(HomeMoreAppSettings("test_flow"))
        suite.addTest(HomeMoreAppSettings("test_verifyCheckbox"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    elif initFwk.name_project == "HPSmart":
        # listTestSuits = ["test_flow",
        #                  # "test_aioVersion",
        #                  # "test_copyRight",
        #                  # "test_legalInformaion",
        #                  # "test_endUserLicenseAgreement",
        #                  # "test_endUserLicenseAgreement_back",
        #                  # "test_hpOnlinePrivacyStatement",
        #                  # "test_hpOnlinePrivacyStatement_back",
        #                  # "test_shareThisApp",
        #                  # "test_shareThisApp_back",
        #                  # "test_headerDisplay"
        #
        #                  # "test_HelpCenter",
        #                  # "test_HowToPrint",
        #                  # "test_OnlineSupport",
        #                  # "test_contactHPonFacebookMessager_step3",
        #                  # "test_contactHPonFacebookMessager_step5",
        #                  # "test_connectionIssues_step1",
        #                  # "test_connectionIssues_step2",
        #                  # "test_connectionIssues_step3",
        #                  # "test_connectionIssues_step4",
        #                  # "test_PrintQualityTools_step1"
        #
        #                  "test_File_Basicfunctionactionbaroption_step1",
        #                  "test_File_Basicfunctionactionbaroption_step2_3_4_5_6",
        #                  "test_File_Basicfunctionactionbaroption_step7",
        #                  "test_File_Basicfunctionactionbaroption_step8",
        #                  "test_File_Basicfunctionactionbaroption_step9",
        #                  "test_File_Basicfunctionactionbaroption_step11",
        #                  "test_FilesMoreOption_step1",
        #                  "test_FilesMoreOption_step2",
        #                  "test_FilesMoreOption_step3",
        #                  "test_01_docs_pdf_pull_down",
        #                  "test_02_select_a_file",
        #                  "test_03_select_multiple_jpegs",
        #                  "test_04_select_mixed_file_types",
        #                  "test_05_only_jpegs",
        #                  "test_06_select_multiple_jpegs",
        #                  "test_07_only_pdf",
        #                  "test_08_select_multiple_pdfs"
        #                  ]
        # for suit in listTestSuits:
        #     suite.addTest(Files(suit))
        # suite.addTest(HomeMoreAppSettings("test_flow"))
        suite.addTest(HomeMoreHelpCenter("test_flow"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    elif initFwk.name_project == "HPSmartiOS":
        suite.addTest(HomeFistLaunchiOS("test_verifyhpAgreement"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    elif initFwk.name_project == "WebExample":
        suite.addTest(WebExample("test_flow1"))
        suite.addTest(WebExample("test_flow"))
        suite.addTest(WebExample("test_flow2"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    elif initFwk.name_project == "WebMultipleThreads":
        # MultipleThreads
        UtilMultipleThreads.run_multiple_threads(mutipleThread1)
    elif initFwk.name_project == "IosExample":
        suite.addTest(IosExample("test_flow"))
        suite.addTest(IosExample("test_your_other_flow"))
        test_result = unittest.TextTestRunner(verbosity=2).run(suite)

