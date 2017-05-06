# coding: utf-8
from fwk.base.InitFwk import InitFwk
from projects.PrinterControl.cases.HomeMoreAbout import HomeMoreAbout
from projects.WebExample.cases.TestBrowser import TestBrowser

import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    initFwk = InitFwk()
    if initFwk.name_project == "PrinterControl":
        suite.addTest(HomeMoreAbout("test_flow"))
        # suite.addTest(HomeMoreAbout("test_aioVersion"))
        # suite.addTest(HomeMoreAbout("test_copyRight"))
        # suite.addTest(HomeMoreAbout("test_legalInformaion"))
        # suite.addTest(HomeMoreAbout("test_endUserLicenseAgreement"))
        # suite.addTest(HomeMoreAbout("test_endUserLicenseAgreement_back"))
        # suite.addTest(HomeMoreAbout("test_hpOnlinePrivacyStatement"))
        # suite.addTest(HomeMoreAbout("test_hpOnlinePrivacyStatement_back"))
        # suite.addTest(HomeMoreAbout("test_shareThisApp"))
        # suite.addTest(HomeMoreAbout("test_shareThisApp_back"))
        # suite.addTest(HomeMoreAbout("test_headerDisplay"))
    elif initFwk.name_project == "WebExample":
        suite.addTest(TestBrowser("test_flow"))    # WebExample
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

