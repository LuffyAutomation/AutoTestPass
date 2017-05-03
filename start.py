# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from fwk.base.GlobalArgs import GlobalArgs

from projects.PrinterControl.cases.HomeMoreAbout import HomeMoreAbout
from projects.PrinterControl.ProjectPortal import ProjectPortal

from projects.WebExample.cases.TestBrowser import TestBrowser
from projects.WebExample.ProjectPortal import ProjectPortal

import unittest

if __name__ == '__main__':
    GlobalArgs.setProjectName(ProjectPortal.getProjectName())
    GlobalArgs.setProjectPath(ProjectPortal.getProjectPath())

    suite = unittest.TestSuite()
    # PrintControl
    # suite.addTest(HomeMoreAbout("test_flow"))
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


    suite.addTest(TestBrowser("test_flow"))    # WebExample
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

