import os
import logging
import logging.config
from xml.dom import minidom
from src.base.core.GlobalArgs import GlobalArgs
from src.utils.commonUtils import Common
from src.utils.utilXml.UtilXml import UtilXml
from src.utils.utilOS.UtilOS import UtilOS
from abc import abstractmethod
from src.utils.utilTime.UtilTime import UtilTime
from src.base.core.ConfigParser import ConfigParser
from src.utils.utilTime.UtilWaitEvent import UtilWaitEvent
from src.utils.utilIO.UtilFolder import UtilFolder
from src.utils.utilIO.UtilFile import UtilFile
from src.utils.utilConsole.UtilConsole import UtilConsole

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class InitializeFramework(object):
    NAME_FILE_XSL = "xmlReport.xsl"
    def __init__(self):
        self.UtilFolder = UtilFolder
        self.UtilTime = UtilTime
        self.UtilFile = UtilFile
        self.UtilXml = UtilXml
        self.UtilOS = UtilOS
        self.UtilConsole = UtilConsole
        self.UtilWaitEvent = UtilWaitEvent
        self._root = None
        self._rootLocalXml = None
        self._currentElementName = None
        self._currentElementObject = None
        self._currentPage = None
        self._currentUiMap = None
        self._elementTimeOut = None
        self.__setup()

    def __setup(self):
        self.__getFrameworkBasePaths()
        self.__getCurrentProjectArgs()
        self.__getConfigurationParameters()
        self.__initializeLogging()
        self.RunTimeConf = self.RunTimeConf(self._ConfigParser)
        self.__setupENV()

    class TestType:
        WEB = "web"
        ANDROID = "android"
        IOS = "ios"

    class Language:
        en_US = "en_US"
        list = (en_US)
        def __init__(self, language):
            if language.lower() == "en" or language.lower() == self.en_US.lower():
                return self.en_US

    class Result:
        NA = "NA"
        path_name_project = ""
        path_folder_results = ""
        path_folder_currentTest = ""
        path_folder_screenshotFail = ""
        path_folder_screenshots = ""
        path_file_xsl_xmlReport = ""
        path_file_xml_xmlReport = ""
        # currentDescripttion = ""
        # currentExpectedResult = ""
        # caseRunTime = ""
        # TestRunTime = ""

        def __init__(self, Portal):
            self._Portal = Portal
            self._UtilTime = self._Portal.UtilTime
            self._UtilFolder = self._Portal.UtilFolder
            self._UtilConsole = self._Portal.UtilConsole
            self._UtilFile = self._Portal.UtilFile
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

            self._dict_report = {self._step: 0, self._description: self.NA, self._expectedResult: self.NA, self._ErrorMessage: self.NA, self._manualCheck: self.NA,
                              self._result: self.NA, self._testName: self.NA, self._platform: self.NA, self._platformVersion: self.NA, self._language: self.NA, self._region: self.NA, self._deviceName: self.NA, self._deviceModel: self.NA, self._startTime: self.NA,
                              self._runTime: 0, self._project: self.NA, self._runTimeTotal: self.NA, self._passesNum: 0, self._failsNum: 0,
                              self._errorsNum: 0, self._blocksNum: 0, self._tbdsNum: 0, self._testsNum: 0, self._testcaseName: self.NA, self._testcaseClassName: self.NA, self._testsuitName: self.NA,
                              self._passesPercent: self.NA, self._failsPercent: self.NA, self._errorsPercent: self.NA, self._blocksPercent: self.NA, self._tbdsPercent: self.NA}

            self._list_baseInfo = [self._project, self._testName, self._platform, self._platformVersion, self._language, self._region, self._deviceName, self._deviceModel]
            self._list_resultInfo = [self._runTime, self._testsNum,
                           self._passesNum, self._failsNum, self._blocksNum, self._tbdsNum, self._errorsNum, self._passesPercent, self._failsPercent, self._errorsPercent, self._blocksPercent, self._tbdsPercent]

            self._list_testsuitAttribute = self._list_baseInfo + self._list_resultInfo

            self._list_testcaseNode = [self._step, self._description, self._expectedResult, self._manualCheck, self._result]
            self._list_testcaseAttribute = [self._testcaseName, self._testcaseClassName, self._runTime]

            self.globalTestSuiteNum = GlobalArgs.getGlobalTestSuiteNum()

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
                        instruction = xmlDoc.createProcessingInstruction("xml-stylesheet", "type=\"text/xsl\" href = \"%s\"" % self._Portal.NAME_FILE_XSL)
                        xmlDoc.insertBefore(instruction, root)
                else:
                    xmlDoc = minidom.parse(xml_Url)
                root = xmlDoc.getElementsByTagName('testsuite')[0]
                testcaseNode = xmlDoc.createElement("testcase")
                for xn in self._list_testsuitAttribute:
                    root.setAttribute(xn, str(self._dict_report[xn]))
                root.setAttribute("time", str(self._dict_report[self._runTimeTotal]))
                root.setAttribute("name", str(self._dict_report[self._testsuitName]))
                root.setAttribute(self._language, str(self._dict_report[self._language]) + "_" + str(self._dict_report[self._region]))
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
                    f.write(xmlDoc.toprettyxml(encoding='UTF-8').decode().replace("\t\t\n", "").replace("\t\n", "").replace("\n\n", "\n").replace("\n\t\t\t\t", "\n\t\t"))
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
            self._UtilFile.writeFile(os.path.join(self.path_folder_currentTest, self.__getResultName() + ".log"), "", file_mode="a")
            self.fileHandler = logging.FileHandler(filename=os.path.join("results", os.path.basename(self.path_folder_currentTest), self.__getResultName() + ".log"), mode='a', encoding="utf-8")
            self.fileHandler.setLevel(logging.DEBUG)
            self.fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s - %(message)s'))
            logging.getLogger("simpleExample").addHandler(self.fileHandler)

        def _setBaseInfo(self):
            self._dict_report[self._platform] = self._Portal.RunTimeConf.platform
            self._dict_report[self._platformVersion] = self._Portal.RunTimeConf.platformVersion
            self._dict_report[self._sdk] = self._Portal.RunTimeConf.sdk
            self._dict_report[self._deviceName] = self._Portal.RunTimeConf.deviceName
            self._dict_report[self._deviceModel] = self._Portal.RunTimeConf.deviceModel
            self._dict_report[self._language] = self._Portal.RunTimeConf.language
            self._dict_report[self._region] = self._Portal.RunTimeConf.region
            for info in self._list_baseInfo:
                self._Portal.logger.info("%s: [%s]" % (info, self._dict_report[info]))

        def setResultToBlockIfFail(self):  # for skip
            self._value_nonPass_result = self._r_block

        def setStepContinueFromFailIfBlock(self):
            self._value_nonPass_result = self._r_fail

        def setResultToTBD(self):  # for skip
            pass

        def setStepBlock(self):
            if self._value_nonPass_result == self._r_block:
                raise Exception("This step is failed since the last step was not successful.")

        def beforeEachFunction(self, TestCase):
            self._Portal.logger.debug("******************************************************************************")
            self._Portal.logger.debug("********Start Testcase********************************************************")
            self._dict_report[self._testcaseName] = TestCase._testMethodName
            self._dict_report[self._testcaseClassName] = TestCase.id().replace("." + TestCase._testMethodName, "")
            self._dict_report[self._testsuitName] = TestCase.id().replace("." + TestCase._testMethodName, "")
            self._dict_report[self._project] = self.path_name_project
            if self._dict_report[self._testName] is None or self._dict_report[self._testName] == self.NA:
                self.setTestName(self._dict_report[self._testcaseClassName])
            self._stepNum = self.__getNextStep()
            self._dict_report[self._startTime] = self._UtilTime.getDateTime()
            # for line feed > test_flow (src.project.PrinterControl.unittestCases.HomeMoreAbout.HomeMoreAbout) ... 2017-04-07 14:54:14,275 INFO - Waiting for the element [checkbox_accept] to be shown on page['page_agreements'].
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
                #print("\n%s: %s\n     %s" % (typ, TestCase.id(), msg))
                self._dict_report[self._failsNum] += 1
                self._dict_report[self._result] = self._r_fail
                self.setResultToBlockIfFail()
                self._dict_report[self._ErrorMessage] = self.__getActualReuslt(msg)
            else:
                self._dict_report[self._passesNum] += 1
                self._dict_report[self._result] = self._r_pass
            self._dict_report[self._testsNum] += 1
            self.setScreenshot()
            self._dict_report[self._passesPercent] = self.__getPercent(self._dict_report[self._passesNum], self._dict_report[self._testsNum])
            self._dict_report[self._failsPercent] = self.__getPercent(self._dict_report[self._failsNum], self._dict_report[self._testsNum])
            self._dict_report[self._errorsPercent] = self.__getPercent(self._dict_report[self._errorsNum], self._dict_report[self._testsNum])
            self._dict_report[self._blocksPercent] = self.__getPercent(self._dict_report[self._blocksNum], self._dict_report[self._testsNum])
            self._dict_report[self._tbdsPercent] = self.__getPercent(self._dict_report[self._tbdsNum], self._dict_report[self._testsNum])
            # GlobalArgs.setPathXmlResult(os.path.join(self.path_folder_currentTest, self.__getResultName()) + ".xml")
            self.path_file_xml_xmlReport = os.path.join(self.path_folder_currentTest, self.__getResultName()) + ".xml"

            self.addResultToXML(os.path.join(self.path_folder_currentTest, self.__getResultName()) + ".xml")
            self._Portal.logger.debug("------------------------------------------------------------------------------")
            self._Portal.logger.debug("[[[Step]]]: %s" % self._dict_report[self._step])
            self._Portal.logger.debug("[[[Description]]]: %s" % self._dict_report[self._description])
            self._Portal.logger.debug("[[[ExpectedResult]]]: %s" % self._dict_report[self._expectedResult])
            self._Portal.logger.debug("[[[ErrorMessage]]]: %s" % self._dict_report[self._ErrorMessage])
            self._Portal.logger.debug("[[[ManualCheck]]]: %s" % self._dict_report[self._manualCheck])
            self._Portal.logger.debug("[[[Result]]]: %s" % self._dict_report[self._result])
            self._Portal.logger.debug("[[[Time(s)]]]: %s" % self._dict_report[self._runTime])
            self.__restoreSomeProperties()
            self._Portal.logger.debug("********End Testcase**********************************************************")
            self._Portal.logger.debug("******************************************************************************")

        def beforeClass(self, TestCase):
            self.__addLoggingForEachTestCase()
            self._setBaseInfo()
            self.path_folder_testSuiteNumScreenshots = os.path.join(self.path_folder_currentTest,
                                                                    self.__getResultName())
            self._UtilFolder.createFolder(self.path_folder_testSuiteNumScreenshots)

        def afterClass(self, TestCase):
            self._Portal.quit()
            if self._Portal.RunTimeConf.isDevicePassTest:
                # print self.path_file_xml_xmlReport
                # print self.path_file_xsl_xmlReport
                # print os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self.__getResultName() + ".xml.png")
                # print os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self._Portal.NAME_FILE_XSL + ".png")
                # print os.path.join(self.path_folder_currentTest, self._Portal.NAME_FILE_XSL)
                self._Portal.UtilFile.copyFile(os.path.join(self.path_folder_currentTest, self._Portal.NAME_FILE_XSL), os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self._Portal.NAME_FILE_XSL + ".png"))
                self._Portal.UtilFile.copyFile(self.path_file_xsl_xmlReport, os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self._Portal.NAME_FILE_XSL + ".png"))
                self._Portal.UtilFile.copyFile(self.path_file_xml_xmlReport, os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self.__getResultName() + ".xml.png"))
                self._Portal.UtilFile.copyFile(self.path_file_xsl_xmlReport, os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), self._Portal.NAME_FILE_XSL + ".png"))

        def __getResultName(self):
            return "%s_%s" % (str(self.globalTestSuiteNum), self._dict_report[self._testName])

        def setScreenshot(self, name="stepEnd", comment="Step ended"):
            path_screenShot = self._Portal.getScreenShot(name, self)
            if self._Portal.RunTimeConf.isDevicePassTest:
                tmp = os.path.join(path_screenShot.replace(self.path_folder_testSuiteNumScreenshots, "")[1:])
            else:
                tmp = os.path.join(path_screenShot.replace(self.path_folder_currentTest, "")[1:])
            tmp = self.__setManualCheck(comment, tmp)
            if self._dict_report[self._manualCheck] == self.NA:
                self._dict_report[self._manualCheck] = ""
            self._dict_report[self._manualCheck] += self._setAsLink(tmp)
            return self._setAsLink(tmp)

        def setComment(self, comment=""):
            if self._dict_report[self._manualCheck] == self.NA:
                self._dict_report[self._manualCheck] = ""
            self._dict_report[self._manualCheck] += self._setLine(comment)
            return self._dict_report[self._manualCheck]

        def __getActualReuslt(self, str):
            return str.replace("Exception: ", "").replace("AssertionError: ", "").replace("AttributeError: ", "")

        def __getPercent(self, num1, num2):
            return "%.1f%%" % (float(num1*100) / num2)

        def __getTime(self):
            self._dict_report[self._runTime] = self._UtilTime.dateDiff(self._dict_report[self._startTime], self._UtilTime.getDateTime())
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
            self.setStepBlock()

        def setDescription(self, *description):
            tmp = ""
            for idx in range(len(description)):
                if idx + 1 != len(description):
                    tmp += self._setLine(description[idx])
                else:
                    tmp += description[idx]
            self._dict_report[self._description] = tmp

    class RunTimeConf:
        isDevicePassTest = False
        isLocalTest = False
        isMobileTest = False
        isWebTest = False
        platform = ""
        platformVersion = ""
        deviceName = ""
        newCommandTimeout = ""
        appPackage = ""
        appActivity = ""
        appWaitActivity = ""
        app = ""
        appiumServerIP = ""
        appiumServerPort = ""
        automationName = ""
        browser = ""
        sdk = ""
        deviceModel = ""
        language = ""
        region = ""

        # get
        def __init__(self, _ConfigParser):
            self._UtilOS = UtilOS
            self._ConfigParser = _ConfigParser
            if os.getenv("APPIUM_PLATFORM") is not None:
                self.isDevicePassTest = True

                self.isMobileTest = True
                self.isWebTest = False
                self.platform = os.getenv("APPIUM_PLATFORM")
                self.platformVersion = os.getenv("APPIUM_DEVICE_VERSION")
                self.automationName = os.getenv("APPIUM_AUTOMATION_NAME")
                self.deviceName = os.getenv("APPIUM_DEVICE_NAME")
                self.newCommandTimeout = os.getenv("APPIUM_NEW_COMMAND_TIMEOUT")
                # desired_caps['newCommandTimeout'] = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_NEWCOMMAND_TIMEOUT)
                self.app = PATH(os.getenv("APPIUM_APP_FILE"))
                self.appPackage = os.getenv("APPIUM_APP_PACKAGE")
                self.appActivity = os.getenv("APPIUM_APP_ACTIVITY")
                self.appiumUrl = os.getenv("APPIUM_URL")
            elif self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_ACTIVITY) is not None:
                self.isDevicePassTest = False

                self.isMobileTest = True
                self.isWebTest = False

                self._ConfigParser = _ConfigParser
                self.platform = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_DEVICE_PLATFORMNAME)
                # self.platformVersion = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_DEVICE_VERSION)
                self.platformVersion = "NA"
                self.deviceName = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_DEVICE_NAME)
                self.newCommandTimeout = self._ConfigParser.getRunTimeConfigCapsValue(
                    self._ConfigParser.APP_NEWCOMMAND_TIMEOUT)
                self.appPackage = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_PACKAGE)
                self.appActivity = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_ACTIVITY)
                self.appWaitActivity = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_WAITACTIVITY)
                self.app = PATH(self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_PATH))
                self.appiumServerIP = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_APPIUM_SERVERIP)
                self.appiumServerPort = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_APPIUM_SERVERPORT)
                self.appiumUrl = "http://" + self.appiumServerIP + ":" + self.appiumServerPort + "/wd/hub"
                self.automationName = "LocalTest"
            else:
                self.isDevicePassTest = False

                self.isMobileTest = False
                self.isWebTest = True
                self.deviceName = "NA"
                self.deviceModel = "NA"
                self.browser = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.BROWSER)
                self.language = self._UtilOS.getOSLocale().split("_")[0]
                self.region = self._UtilOS.getOSLocale().split("_")[1]
                self.platform = self._UtilOS.getOSName()
                self.platformVersion = self._UtilOS.getOSRelease()
                pass

        def getMobileInfo(self, Portal):
            self.Portal = Portal
            lines = self.Portal.getMobilePropReadlines(self.deviceName)
            self.__setMobileDetails(lines)

        def getWebInfo(self, Portal):
            self.Portal = Portal

        def __setMobileDetails(self, lines):
            #self.Portal.logger.info(self.platform.lower().strip() == "android")
            if self.platform.lower().strip() == "android":
                for line in lines:
                    if line.decode('utf-8').strip().split("=")[0] == "ro.product.locale.language":
                        self.language = line.decode('utf-8').strip().split("=")[1]
                    elif line.decode('utf-8').strip().split("=")[0] == "ro.product.locale.region":
                        self.region = line.decode('utf-8').strip().split("=")[1]
                    elif line.decode('utf-8').strip().split("=")[0] == "ro.product.model":
                        self.deviceModel = line.decode('utf-8').strip().split("=")[1]
                    elif line.decode('utf-8').strip().split("=")[0] == "ro.build.version.release":
                        self.platformVersion = line.decode('utf-8').strip().split("=")[1]
                    elif line.decode('utf-8').strip().split("=")[0] == "ro.build.version.sdk":
                        self.sdk = line.decode('utf-8').strip().split("=")[1]
            if self.language == "" or self.region == "":  # 6.0
                t = self.Portal.getBuildInMobileLanguage(self.deviceName)
                self.language = t.split("-")[0]
                self.region = t.split("-")[1]
            self._path_file_localXml = os.path.join(self.Portal._path_folder_uiMaps, self.Portal.getMobileLanguageRegion() + ".xml")
            if self.language != "en":  # en_US.xml needn't be loaded.
                self._xmlTreeLocalXml = self.Portal.UtilXml.getTree(self._path_file_localXml)
                self._rootLocalXml = self.Portal.UtilXml.getRootElement(self._xmlTreeLocalXml)

    def __addLogForCountDown(self, log, interval):
        self.logger.info(log)
        self.UtilTime.sleep(interval)

    def log_countDown(self, log, range_max=30, interval=5, range_min=0):
        # reLog = lambda x: self.logger.info(log + " > Time left: %s s." % str(x))
        reLog = lambda x: self.__addLogForCountDown(log + " > Time left: %s s." % str(x), interval)
        self.UtilTime.countDown(range_max, reLog, interval, range_min)

    def __addLogForWaitEvent(self, method, log):
        if ". 0s elapsed" not in log:  # ignore this
            self.logger.info(log)
        return method()

    def waitUntil(self, method, error_message="Wait failed.", time_out=None, poll_frequency=2, log_prefix=None):
        if log_prefix is None:
            log_prefix = "Finding element [" + str(self.getCurrentElementName()) + "] of page [" + str(self.getCurrentPage()) + "]."
        if time_out is None:
            try:
                time_out = float(self._elementTimeOut)
            except Exception:
                time_out = 60
        self.UtilWaitEvent(time_out, poll_frequency).until(
            lambda start_time: self.__addLogForWaitEvent(method, "......%s %ss elapsed. Timeout is %ss. Interval is %s." % (log_prefix, start_time, time_out, poll_frequency)), error_message
        )

    def __getOSLanguage(self):
        self._osLanguage = self.UtilOS.getOSLocale() # not work in dp

    def __setupENV(self):
        self.Result.path_name_project = self._name_project
        self.Result.path_folder_results = os.path.join(self._path_folder_AutoTestPass, "results")

        #self.Result.path_folder_currentTest = os.path.join(self.Result.path_folder_results, self.UtilTime.getCurrentTime())
        self.Result.path_folder_currentTest = os.path.join(self.Result.path_folder_results, GlobalArgs.getGlobalStartTime())

        self.Result.path_folder_screenshots = os.path.join(self.Result.path_folder_currentTest, "screenshots")
        self.Result.path_file_xsl_xmlReport = os.path.join(self._path_folder_src, "base", "report", "xml", self.NAME_FILE_XSL)

        self.UtilFolder.createFolder(self.Result.path_folder_results)
        self.UtilFolder.createFolder(self.Result.path_folder_currentTest)
        # self.UtilFolder.createFolder(self.Result.path_folder_screenshots)
        self.UtilFile.copyFile(self.Result.path_file_xsl_xmlReport, os.path.join(self.Result.path_folder_currentTest, self.NAME_FILE_XSL))

    def __getFrameworkBasePaths(self):
        self._name_project = self.getProjectName()
        self._path_folder_project = self.getProjectPath()
        self._path_folder_AutoTestPass = PATH("../../..")
        self._path_folder_resources = PATH("../../../resources")
        self._path_folder_src = PATH("../../../src")
        self._path_folder_conf = os.path.join(self._path_folder_resources, "conf")
        # self._path_folder_browserDriver = os.path.join(self._path_folder_resources, "browserDriver")
        self._path_folder_browserDriver = PATH("./../../../../browserDriver")
        self._path_file_mainConf = os.path.join(self._path_folder_conf, "main.conf")
        self._path_folder_data = os.path.join(self._path_folder_project, "data")

    def __getCurrentProjectArgs(self):
        self._ConfigParser = ConfigParser()
        self.__MainConfig = self.__getConfigObject(self._path_file_mainConf)
        self._ConfigParser.setMainConfig(self.__MainConfig)
        self._testType = self._ConfigParser.getMainConfigValue(self._name_project, self._ConfigParser.CURRENT_TEST_TYPE)
        #self._browser = self._ConfigParser.getMainConfigValue(self._name_project, self._ConfigParser.BROWSER)
        try:
            self._path_file_runTimeConf = os.path.join(self._path_folder_data, self._testType, 'runTime.conf')
        except:
            if self._testType is None:
                self.logger.error("faild to find [%s] in [%s]." % (self._name_project, self._path_file_mainConf))

        self.__RunTimeConfig = self.__getConfigObject(self._path_file_runTimeConf)
        self._ConfigParser.setRunTimeConfig(self.__RunTimeConfig)
        self._path_folder_uiMaps = os.path.join(self._path_folder_data, self._testType, 'uiMaps')
        self._path_file_uiMap = os.path.join(self._path_folder_uiMaps, self._ConfigParser.getRunTimeConfigArgsValue(self._ConfigParser.TEST_UIMAP_FILENAME))

    def __getConfigurationParameters(self):
        self._xmlTree = self.UtilXml.getTree(self._path_file_uiMap)
        self._root = self.UtilXml.getRootElement(self._xmlTree)

        self._elementTimeOut = self._ConfigParser.getRunTimeConfigArgsValue(self._ConfigParser.TEST_TIMEOUT_ELEMENT)

    def getMobileLanguageRegion(self):
        return self.RunTimeConf.language + "_" + self.RunTimeConf.region

    def __initializeLogging(self):
        logging.config.fileConfig(os.path.join(self._path_folder_conf, "log.conf"))
        self.logger = logging.getLogger("simpleExample")

    @abstractmethod
    def getAndroidSDK(self, uuid=None):
        pass
    @abstractmethod
    def getBuildInMobileLanguage(self, uuid=None):
        pass
    @abstractmethod
    def getProjectName(self):
        pass
    @abstractmethod
    def getProjectPath(self):
        pass
    @abstractmethod
    def updateCurrentElementStatus(self, element_name):
        pass
    @abstractmethod
    def setCurrentElementName(self, element_name):
        pass
    @abstractmethod
    def getCurrentElementName(self):
        pass
    @abstractmethod
    def setCurrentPage(self, page):
        pass
    @abstractmethod
    def getCurrentPage(self):
        pass
    @abstractmethod
    def setCurrentElementObject(self, element):
        pass
    @abstractmethod
    def getCurrentElementObject(self):
        pass
    # @abstractmethod
    # def getScreenShot(self, name, Result):
    #     pass
        #self._getAppInfo()

    def _getAppInfo(self):
        self._DefaultPage = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//DefaultPage"))
        self.__appConfFolderName = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//AppName"))
        self.__Version = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Version"))
        self.__Environment = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Environment"))
        self.__TestCategory = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//TestCategory"))
        self.__NetWork = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Network"))
        self.__Description = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Description"))

        self.logger.info("Default Page : " + self._DefaultPage)
        self.logger.info("App Name : " + self.__appConfFolderName)
        self.logger.info("App Version : " + self.__Version)
        self.logger.info("Test Environment : " + self.__Environment)
        self.logger.info(self.__TestCategory)
        self.logger.info("Test NewWork : " + self.__NetWork)
        self.logger.info("Description : " + self.__Description)

    def __getConfigObject(self, configFileName):
        return Common.configParser(configFileName)

    def __defaultIfEmpty(self, str, defaultStr):
        if str == "" or str is None:
            return defaultStr
        else:
            return str

    def log(self, message, level=1):
        if level == 1:
            self.logger.info(message)
        if level == 2:
            self.logger.warning(message)
        if level == 3:
            self.logger.debug(message)
        if level == 4:
            self.logger.error(message)

