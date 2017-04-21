# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from src.project.PrinterControl.unittestSuites.HomeMoreAbout import HomeMoreAbout
from src.project.WebExample.unittestSuites.TestBrowser import TestBrowser
import unittest
#import xmlrunner
import os

# def run_suite_output_xml_report(suite, **args):
#     '''
#     :param suite: 已组装好的测试套
#     :param args: 可设置的参数及说明如下：
#          TEST_OUTPUT_DESCRIPTIONS: 输出描述
#          TEST_OUTPUT_DIR：测试报告输出路径，默认为根目录
#          TEST_OUTPUT_FILE_NAME：测试报告输入文件名，默认为hsplatform_ut_testreport.xml
#     :return:
#     '''
#     descriptions = args.get('TEST_OUTPUT_DESCRIPTIONS', True)
#     output_dir = args.get('TEST_OUTPUT_DESCRIPTIONS', 'c:\\')
#     single_file = args.get('TEST_OUTPUT_FILE_NAME', 'hsplatform_ut_testreport.xml')
#     kwargs = dict(verbosity=1, descriptions=descriptions, failfast=False)
#     if single_file is not None:
#         file_path = os.path.join(output_dir, single_file)
#         with open(file_path, 'wb') as xml:
#             return xmlrunner.XMLTestRunner(output=xml, **kwargs).run(suite)
#     else :
#         return xmlrunner.XMLTestRunner(output=output_dir, **kwargs).run(suite)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(HomeMoreAbout("test_flow"))
    suite.addTest(HomeMoreAbout("test_aioVersion"))
    suite.addTest(HomeMoreAbout("test_copyRight"))
    suite.addTest(HomeMoreAbout("test_legalInformaion"))
    suite.addTest(HomeMoreAbout("test_endUserLicenseAgreement"))
    suite.addTest(HomeMoreAbout("test_endUserLicenseAgreement_back"))
    suite.addTest(HomeMoreAbout("test_hpOnlinePrivacyStatement"))
    suite.addTest(HomeMoreAbout("test_hpOnlinePrivacyStatement_back"))
    suite.addTest(HomeMoreAbout("test_shareThisApp"))
    suite.addTest(HomeMoreAbout("test_shareThisApp_back"))
    suite.addTest(HomeMoreAbout("test_headerDisplay"))

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

