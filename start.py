# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from project.PrinterControl.unittestSuites.HomeMoreAbout import HomeMoreAbout
from src.base.core.GlobalArgs import GlobalArgs
from project.PrinterControl.ProjectPortal import ProjectPortal
import unittest

if __name__ == '__main__':
    GlobalArgs.setProjectName(ProjectPortal.getProjectName())
    GlobalArgs.setProjectPath(ProjectPortal.getProjectPath())

    suite = unittest.TestSuite()
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

    # suite.addTest(unittest.makeSuite(HomeMoreAbout, 'test'))
    # suite.addTest(TestBrowser("test_flow"))



    test_result = unittest.TextTestRunner(verbosity=2).run(suite)


    # suite = unittest.TestSuite()
    # suite.addTest(HomeMoreAbout("test_flow"))
    # test_result = unittest.TextTestRunner(verbosity=2).run(suite)

    # suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    # pass
    # test_result = run_suite_output_xml_report(suite)
    # print('All case number')
    # print(test_result.testsRun)
    # print('Failed case number')
    # print(len(test_result.failures))
    # print('Failed case and reason')
    # print(test_result.failures)
    # for case, reason in test_result.errors:
    #     print('case.id')
    #     print(case.id())
    #     print('reason')
    #     print(reason)

