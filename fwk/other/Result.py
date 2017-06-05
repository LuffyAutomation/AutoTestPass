import logging
import logging.config
import os
from xml.dom import minidom

from fwk.base.GlobalArgs import GlobalArgs
from fwk.utils.exceller.Exceller import Exceller


class Result:
    NA = "NA"
    name_project = ""
    path_folder_results = ""
    path_folder_currentTest = ""
    path_folder_screenshotFail = ""
    path_folder_screenshots = ""
    path_file_xsl_xmlReport = ""
    path_file_xml_xmlReport = ""
    DictCaseInfo_android = None
    DictCaseInfo_web = None
    DictCaseInfo_ios = None
    DictCaseInfo_current = None
    _env_block_msg = None
    # currentDescripttion = ""
    # currentExpectedResult = ""
    # caseRunTime = ""
    # TestRunTime = ""

    def __init__(self, UI, Init, testName=None):
        self._Init = Init
        self._UI = UI
        self._UtilTime = self._UI.UtilTime
        self._UtilFolder = self._UI.UtilFolder
        self._UtilConsole = self._UI.UtilConsole
        self._UtilFile = self._UI.UtilFile
        self._r_pass = "Pass"
        self._r_fail = "Fail"
        self._value_nonPass_result = self._r_fail
        self._value_pass_result = self._r_pass
        self._r_tbd = "TBD"
        self._r_flow = "Flow"
        self._r_block = "Block"
        self._blockStatus = ""
        self._step = "step"
        self._description = "description"
        self._expectedResult = "expectedResult"
        self._ErrorMessage = "ErrorMessage"
        self._manualCheck = "manualCheck"
        self._result = "result"
        self._testName = "testName"
        self._testSetName = "testSetName"

        self._platform = "os"
        self._platformVersion = "version"
        self._language = "language"
        self._region = "region"

        self._deviceName = "deviceName"
        self._deviceModel = "deviceModel"
        self._sdk = "sdk"

        self._startTime = "startTime"
        self._runTime = "time"
        self._runTimeTotal = "timeTotal"
        self._project = "project"
        self._passesNum = "passes"
        self._failsNum = "failures"
        self._errorsNum = "errors"
        self._blocksNum = "blocks"
        self._tbdsNum = "tbds"
        self._passesPercent = "passesPercent"
        self._failsPercent = "failsPercent"
        self._errorsPercent = "errorsPercent"
        self._blocksPercent = "blocksPercent"
        self._tbdsPercent = "tbdsPercent"
        self._testsNum = "tests"
        self._testcaseName = "name"
        self._testcaseClassName = "classname"
        self._testsuitName = "testsuitName"
        self.__setupENV()
        self._dict_report = {self._step: 0, self._description: self.NA, self._expectedResult: self.NA,
                             self._ErrorMessage: self.NA, self._manualCheck: self.NA,
                             self._result: self.NA, self._testName: self.NA, self._platform: self.NA,
                             self._platformVersion: self.NA, self._language: self.NA, self._region: self.NA,
                             self._deviceName: self.NA, self._deviceModel: self.NA, self._startTime: self.NA,
                             self._runTime: 0, self._project: self.NA, self._runTimeTotal: self.NA, self._passesNum: 0,
                             self._failsNum: 0,
                             self._errorsNum: 0, self._blocksNum: 0, self._tbdsNum: 0, self._testsNum: 0,
                             self._testcaseName: self.NA, self._testcaseClassName: self.NA, self._testsuitName: self.NA,
                             self._passesPercent: self.NA, self._failsPercent: self.NA, self._errorsPercent: self.NA,
                             self._blocksPercent: self.NA, self._tbdsPercent: self.NA}

        self._list_baseInfo = [self._project, self._testName, self._platform, self._platformVersion, self._language,
                               self._region, self._deviceName, self._deviceModel]
        self._list_resultInfo = [self._runTime, self._testsNum,
                                 self._passesNum, self._failsNum, self._blocksNum, self._tbdsNum, self._errorsNum,
                                 self._passesPercent, self._failsPercent, self._errorsPercent, self._blocksPercent,
                                 self._tbdsPercent]

        self._list_testsuitAttribute = self._list_baseInfo + self._list_resultInfo

        self._list_testcaseNode = [self._step, self._description, self._expectedResult, self._manualCheck, self._result]
        self._list_testcaseAttribute = [self._testcaseName, self._testcaseClassName, self._runTime]
        self.setTestName(testName)

    def setEnvBlockMsg(self, env_block_msg):
        self._env_block_msg = env_block_msg

    def _setAsLink(self, str):
        return "#$#" + str + "#$#" + self._setLine("")

    def _setLine(self, str):
        return str + "~!~"

    def __setManualCheck(self, comment, link):
        return comment + "@@@" + link

    # def __decode(self, str, encoding='utf-8'):
    #     try:
    #         str = str.decode(encoding)
    #     except:
    #         str = str

    def addResultToXML(self, xml_Url, strXSl="xmlReport.xsl"):
        xmlDoc = None
        try:
            if not os.path.exists(xml_Url):
                xmlDoc = minidom.Document()
                root = xmlDoc.appendChild(xmlDoc.createElement("testsuite"))
                # xmlDoc.insertBefore(header, root)
                if strXSl != "":
                    instruction = xmlDoc.createProcessingInstruction("xml-stylesheet",
                                                                     "type=\"text/xsl\" href = \"%s\"" % strXSl)
                    xmlDoc.insertBefore(instruction, root)
            else:
                xmlDoc = minidom.parse(xml_Url)
            root = xmlDoc.getElementsByTagName('testsuite')[0]
            testcaseNode = xmlDoc.createElement("testcase")
            for xn in self._list_testsuitAttribute:
                root.setAttribute(xn, str(self._dict_report[xn]))
            root.setAttribute("time", str(self._dict_report[self._runTimeTotal]))
            root.setAttribute("name", str(self._dict_report[self._testsuitName]))
            root.setAttribute(self._language,
                              str(self._dict_report[self._language]) + "_" + str(self._dict_report[self._region]))
            xmlDoc.lastChild.appendChild(testcaseNode)
            for xn in self._list_testcaseAttribute:
                testcaseNode.setAttribute(xn, str(self._dict_report[xn]))
            for xn in self._list_testcaseNode:
                testcaseChildNode = xmlDoc.createElement(xn)
                testcaseChildNode.appendChild(xmlDoc.createTextNode(str(self._dict_report[xn])))
                root.lastChild.appendChild(testcaseChildNode)
            testcaseChildNode = xmlDoc.createElement("failure")

            testcaseChildNode.appendChild(xmlDoc.createCDATASection(str(self._dict_report[self._ErrorMessage])))

            testcaseChildNode.setAttribute("message", str(self._dict_report[self._ErrorMessage]))
            testcaseChildNode.setAttribute("type", "Exception")
            root.lastChild.appendChild(testcaseChildNode)

            # f = open(xml_Url, 'w', encoding='UTF-8')
            f = open(xml_Url, 'w')  # Python2 encoding is not a option.
            try:
                # f.write(xmlDoc.toxml(encoding = 'UTF-8'))
                # f.write(xmlDoc.toprettyxml(encoding='UTF-8').decode())
                # xmlDoc.writexml(f, encoding = 'UTF-8')
                f.write(xmlDoc.toprettyxml(encoding='UTF-8').decode().replace("\t\t\n", "").replace("\t\n", "").replace(
                    "\n\n", "\n").replace("\n\t\t\t\t", "\n\t\t"))
            except Exception:
                pass
            finally:
                f.close()
        except Exception as e:
            pass

    def __getNextStep(self):
        self._dict_report[self._step] += 1
        return self._dict_report[self._step]

    def getCurrentStep(self):
        return self._dict_report[self._step]

    def __addLoggingForEachTestCase(self):
        self._UtilFile.writeFile(os.path.join(self.path_folder_currentTest, self.__getResultName() + ".log"), "",
                                 file_mode="a")
        self.fileHandler = logging.FileHandler(
            filename=os.path.join("results", os.path.basename(self.path_folder_currentTest),
                                  self.__getResultName() + ".log"), mode='a', encoding="utf-8")
        self.fileHandler.setLevel(logging.DEBUG)
        self.fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s - %(message)s'))
        logging.getLogger("simpleExample").addHandler(self.fileHandler)

    def _setBaseInfo(self):
        self._dict_report[self._platform] = self._UI.RunTimeConf.platform
        self._dict_report[self._platformVersion] = self._UI.RunTimeConf.platformVersion
        self._dict_report[self._sdk] = self._UI.RunTimeConf.sdk
        self._dict_report[self._deviceName] = self._UI.RunTimeConf.deviceName
        self._dict_report[self._deviceModel] = self._UI.RunTimeConf.deviceModel
        self._dict_report[self._language] = self._UI.RunTimeConf.language
        self._dict_report[self._region] = self._UI.RunTimeConf.region

    def printBaseInfo(self):
        for info in self._list_baseInfo:
            self._UI.logger.info("%s: [%s]" % (info, self._dict_report[info]))

    def setResultToBlockIfFail(self):  # for skip
        self._value_nonPass_result = self._r_block

    def setStepContinueFromFailIfBlock(self):
        self._value_nonPass_result = self._r_fail

    def setResultToTBD(self):  # for skip
        pass

    def setStepBlock(self, env_block_msg):
        if env_block_msg is not None:
            self._value_nonPass_result == self._r_block
            raise Exception("This step is failed since the test env error. Please check the log file for details.")
        if self._value_nonPass_result == self._r_block:
            raise Exception("This step is failed since the last step was not successful.")

    def __loadCaseInfo(self, dictCaseInfo, filePath, name_sheet=None, path_file_excel=None):
        if path_file_excel is None:
            path_file_excel = filePath
        if dictCaseInfo is None:
            dictCaseInfo = Exceller(path_file_excel, name_sheet).getDictAllCasesInfo()
        self.DictCaseInfo_current = dictCaseInfo

    def loadAndroidCaseInfoFromExcel(self, name_sheet=None, path_file_excel=None):
        self.__loadCaseInfo(self.DictCaseInfo_android, self._Init.path_file_xlsx_caseInfo_android, name_sheet, path_file_excel)

    def loadIosCaseInfoFromExcel(self, name_sheet=None, path_file_excel=None):
        self.__loadCaseInfo(self.DictCaseInfo_ios, self._Init.path_file_xlsx_caseInfo_ios, name_sheet, path_file_excel)

    def loadWebCaseInfoFromExcel(self, name_sheet=None, path_file_excel=None):
        self.__loadCaseInfo(self.DictCaseInfo_web, self._Init.path_file_xlsx_caseInfo_web, name_sheet, path_file_excel)

    def setDescriptionAndExpectedResultFromExcel(self, id):
        if self.DictCaseInfo_current is not None:
            caseInfo = self.DictCaseInfo_current[id]
            self.setDescription(*caseInfo.description)
            self.setExpectedResult(*caseInfo.expectedResult)
        self.setStepBlock(self._env_block_msg)

    def beforeEachFunction(self, TestCase):
        self._UI.logger.debug("******************************************************************************")
        self._UI.logger.debug("********Start Testcase********************************************************")
        self._dict_report[self._testcaseName] = TestCase._testMethodName
        self._dict_report[self._testcaseClassName] = TestCase.id().replace("." + TestCase._testMethodName, "")
        self._dict_report[self._testsuitName] = TestCase.id().replace("." + TestCase._testMethodName, "")
        self._dict_report[self._project] = self.name_project
        if self._dict_report[self._testName] is None or self._dict_report[self._testName] == self.NA:
            self.setTestName(self._dict_report[self._testcaseClassName])
        self._stepNum = self.__getNextStep()
        self._dict_report[self._startTime] = self._UtilTime.getDateTime()
        self.setDescriptionAndExpectedResultFromExcel(self._dict_report[self._testcaseName])
        # for line feed > test_flow (src.projects.PrinterControl.unittestCases.HomeMoreAbout.HomeMoreAbout) ... 2017-04-07 14:54:14,275 INFO - Waiting for the element [checkbox_accept] to be shown on page['page_agreements'].
        # self._UtilConsole.printCmdLn("")

    def afterEachFunction(self, TestCase):
        self.__getTime()
        if hasattr(TestCase, '_outcome'):  # Python 3.4+
            result = TestCase.defaultTestResult()  # these 2 methods have no side effects
            TestCase._feedErrorsToResult(result, TestCase._outcome.errors)
        else:  # Python 3.2 - 3.3 or 2.7
            result = getattr(TestCase, '_outcomeForDoCleanups', TestCase._resultForDoCleanups)
        error = self.__list2reason(TestCase, result.errors)
        failure = self.__list2reason(TestCase, result.failures)
        ok = not error and not failure

        msg = self.NA
        if not ok:
            typ, text = ('ERROR', error) if error else ('FAIL', failure)
            msg = [x for x in text.split('\n')[1:] if not x.startswith(' ')][0]
            # print("\n%s: %s\n     %s" % (typ, TestCase.id(), msg))
            self._dict_report[self._failsNum] += 1
            self._dict_report[self._result] = self._r_fail
            self.setResultToBlockIfFail()
            self._dict_report[self._ErrorMessage] = self.__getActualReuslt(msg)
        else:
            self._dict_report[self._passesNum] += 1
            self._dict_report[self._result] = self._r_pass
        self._dict_report[self._testsNum] += 1
        self.setScreenshot()
        self._dict_report[self._passesPercent] = self.__getPercent(self._dict_report[self._passesNum],
                                                                   self._dict_report[self._testsNum])
        self._dict_report[self._failsPercent] = self.__getPercent(self._dict_report[self._failsNum],
                                                                  self._dict_report[self._testsNum])
        self._dict_report[self._errorsPercent] = self.__getPercent(self._dict_report[self._errorsNum],
                                                                   self._dict_report[self._testsNum])
        self._dict_report[self._blocksPercent] = self.__getPercent(self._dict_report[self._blocksNum],
                                                                   self._dict_report[self._testsNum])
        self._dict_report[self._tbdsPercent] = self.__getPercent(self._dict_report[self._tbdsNum],
                                                                 self._dict_report[self._testsNum])
        # GlobalArgs.setPathXmlResult(os.path.join(self.path_folder_currentTest, self.__getResultName()) + ".xml")
        self.path_file_xml_xmlReport = os.path.join(self.path_folder_currentTest, self.__getResultName()) + ".xml"

        self.addResultToXML(os.path.join(self.path_folder_currentTest, self.__getResultName()) + ".xml")
        self._UI.logger.debug("------------------------------------------------------------------------------")
        self._UI.logger.debug("[[[Step]]]: %s" % self._dict_report[self._step])
        self._UI.logger.debug("[[[Description]]]: %s" % self._dict_report[self._description])
        self._UI.logger.debug("[[[ExpectedResult]]]: %s" % self._dict_report[self._expectedResult])
        self._UI.logger.debug("[[[ErrorMessage]]]: %s" % self._dict_report[self._ErrorMessage])
        self._UI.logger.debug("[[[ManualCheck]]]: %s" % self._dict_report[self._manualCheck])
        self._UI.logger.debug("[[[Result]]]: %s" % self._dict_report[self._result])
        self._UI.logger.debug("[[[Time(s)]]]: %s" % self._dict_report[self._runTime])
        self.__restoreSomeProperties()
        self._UI.logger.debug("********End Testcase**********************************************************")
        self._UI.logger.debug("******************************************************************************")

    def beforeClass(self):
            self.globalTestSuiteNum = GlobalArgs.getGlobalTestSuiteNum()
            self.__addLoggingForEachTestCase()
            self._setBaseInfo()
            self.printBaseInfo()
            self.path_folder_testSuiteNumScreenshots = os.path.join(self.path_folder_currentTest,
                                                                    self.__getResultName())
            self._UtilFolder.createFolder(self.path_folder_testSuiteNumScreenshots)

    def afterClass(self, TestCase):
        # self._UI.quit()
        if self._UI.RunTimeConf.isDevicePassTest:
            # print self.path_file_xml_xmlReport
            # print self.path_file_xsl_xmlReport
            # print os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self.__getResultName() + ".xml.png")
            # print os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self._UI.NAME_FILE_XSL + ".png")
            # print os.path.join(self.path_folder_currentTest, self._UI.NAME_FILE_XSL)
            self._UI.UtilFile.copyFile(os.path.join(self.path_folder_currentTest, self._UI.NAME_FILE_XSL),
                                           os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"),
                                                        self._UI.NAME_FILE_XSL + ".png"))
            self._UI.UtilFile.copyFile(self.path_file_xsl_xmlReport,
                                           os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"),
                                                        self._UI.NAME_FILE_XSL + ".png"))
            self._UI.UtilFile.copyFile(self.path_file_xml_xmlReport,
                                           os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"),
                                                        self.__getResultName() + ".xml.png"))
            self._UI.UtilFile.copyFile(self.path_file_xsl_xmlReport,
                                           os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"),
                                                        self._UI.NAME_FILE_XSL + ".png"))

    def __getResultName(self):
        return "%s_%s" % (str(self.globalTestSuiteNum), self._dict_report[self._testName])

    def setScreenshot(self, name="stepEnd", comment="Step ended"):
        try:
            path_screenShot = self._UI.getScreenShot(name, self)
            if self._UI.RunTimeConf.isDevicePassTest:
                tmp = os.path.join(path_screenShot.replace(self.path_folder_testSuiteNumScreenshots, "")[1:])
            else:
                tmp = os.path.join(path_screenShot.replace(self.path_folder_currentTest, "")[1:])
            tmp = self.__setManualCheck(comment, tmp)
            if self._dict_report[self._manualCheck] == self.NA:
                self._dict_report[self._manualCheck] = ""
            self._dict_report[self._manualCheck] += self._setAsLink(tmp)
            return self._setAsLink(tmp)
        except:
            pass

    def setComment(self, comment=""):
        if self._dict_report[self._manualCheck] == self.NA:
            self._dict_report[self._manualCheck] = ""
        self._dict_report[self._manualCheck] += self._setLine(comment)
        return self._dict_report[self._manualCheck]

    def __getActualReuslt(self, str):
        return str.replace("Exception: ", "").replace("AssertionError: ", "").replace("AttributeError: ", "")

    def __getPercent(self, num1, num2):
        return "%.1f%%" % (float(num1 * 100) / num2)

    def __getTime(self):
        self._dict_report[self._runTime] = self._UtilTime.dateDiff(self._dict_report[self._startTime],
                                                                   self._UtilTime.getDateTime())
        if self._dict_report[self._runTimeTotal] == self.NA:
            self._dict_report[self._runTimeTotal] = self._dict_report[self._runTime]
        else:
            self._dict_report[self._runTimeTotal] += self._dict_report[self._runTime]

    def __restoreSomeProperties(self):
        self._dict_report[self._ErrorMessage] = self.NA
        self._dict_report[self._manualCheck] = self.NA
        self._dict_report[self._description] = self.NA
        self._dict_report[self._expectedResult] = self.NA

    def __list2reason(self, TestCase, exc_list):
        if exc_list and exc_list[-1][0] is TestCase:
            return exc_list[-1][1]

    def setTestName(self, name):
        self._dict_report[self._testName] = name

    def setExpectedResult(self, *expectedResult):
        tmp = ""
        for idx in range(len(expectedResult)):
            if idx + 1 != len(expectedResult):
                tmp += self._setLine(expectedResult[idx])
            else:
                tmp += expectedResult[idx]
        self._dict_report[self._expectedResult] = tmp
        self.setStepBlock(self._env_block_msg)

    def setDescription(self, *description):
        tmp = ""
        for idx in range(len(description)):
            if idx + 1 != len(description):
                tmp += self._setLine(description[idx])
            else:
                tmp += description[idx]
        self._dict_report[self._description] = tmp

    def getMobileInfo(self, UI):
        self.UI = UI
        lines = self.UI.getMobilePropReadlines(self.deviceName)
        self.__setMobileDetails(lines)

    def getWebInfo(self, UI):
        self.UI = UI

    # def __setMobileDetails(self, lines):
    #     # self.UI.logger.info(self.platform.lower().strip() == "android")
    #     if self.platform.lower().strip() == "android":
    #         for line in lines:
    #             if line.decode('utf-8').strip().split("=")[0] == "ro.product.locale.language":
    #                 self.language = line.decode('utf-8').strip().split("=")[1]
    #             elif line.decode('utf-8').strip().split("=")[0] == "ro.product.locale.region":
    #                 self.region = line.decode('utf-8').strip().split("=")[1]
    #             elif line.decode('utf-8').strip().split("=")[0] == "ro.product.model":
    #                 self.deviceModel = line.decode('utf-8').strip().split("=")[1]
    #             elif line.decode('utf-8').strip().split("=")[0] == "ro.build.version.release":
    #                 self.platformVersion = line.decode('utf-8').strip().split("=")[1]
    #             elif line.decode('utf-8').strip().split("=")[0] == "ro.build.version.sdk":
    #                 self.sdk = line.decode('utf-8').strip().split("=")[1]
    #     if self.language == "" or self.region == "":  # 6.0
    #         t = self.UI.getBuildInMobileLanguage(self.deviceName)
    #         self.language = t.split("-")[0]
    #         self.region = t.split("-")[1]
    #     self._path_file_localXml = os.path.join(self.UI._path_folder_uiMaps,
    #                                             self.UI.getLanguageRegion() + ".xml")
    #     if self.language != "en":  # en_US.xml needn't be loaded.
    #         self._xmlTreeLocalXml = self.UI.UtilXml.getTree(self._path_file_localXml)
    #         self._rootLocalXml = self.UI.UtilXml.getRootElement(self._xmlTreeLocalXml)

    def __setupENV(self):
        self.name_project = self._Init.name_project
        self.path_folder_results = self._Init.path_folder_results

        #self.Result.path_folder_currentTest = os.path.join(self.Result.path_folder_results, self.UtilTime.getCurrentTime())
        self.path_folder_currentTest = self._Init.path_folder_currentTest

        self.path_folder_screenshots = self._Init.path_folder_screenshots
        self.path_file_xsl_xmlReport = self._Init.path_file_xsl_xmlReport
