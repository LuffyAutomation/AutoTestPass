import os
import logging
import logging.config
from xml.dom import minidom
from src.base.core.GlobalArgs import GlobalArgs
from src.utils.commonUtils import Common
from src.utils.utilXml.UtilXml import UtilXml
from src.utils.utilOS.UtilOS import UtilOS

from src.utils.utilTime.UtilTime import UtilTime
from src.base.core.ConfigParser import ConfigParse
from src.utils.utilTime.UtilWaitEvent import UtilWaitEvent
from src.utils.utilIO.UtilFolder import UtilFolder
from src.utils.utilIO.UtilFile import UtilFile
from src.utils.utilConsole.UtilConsole import UtilConsole


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class InitFwk:
    NAME_FILE_XSL = "xmlReport.xsl"

    class TestType:
        ANDROID = 'Android'
        IOS = "Ios"
        WEB = "Web"

    def __init__(self, name_project, path_folder_project):
        self.UtilFolder = UtilFolder
        self.UtilTime = UtilTime
        self.UtilFile = UtilFile
        self.UtilXml = UtilXml
        self.UtilOS = UtilOS
        self.UtilConsole = UtilConsole
        self.UtilWaitEvent = UtilWaitEvent
        self._name_project = name_project
        self._path_folder_project = path_folder_project
        self.__setup()

    def __setup(self):
        self.__getFrameworkBasePaths()
        self.__getCurrentProjectArgs()
        # self.__getConfigurationParameters()
        self.__initializeLogging()
        # self.RunTimeConf = self.RunTimeConf(self._ConfigParser)
        self.__setupENV()

    class TestType:
        WEB = "ui"
        ANDROID = "android"
        IOS = "ios"

    class Language:
        en_US = "en_US"
        list = (en_US)
        def __init__(self, language):
            if language.lower() == "en" or language.lower() == self.en_US.lower():
                return self.en_US

    def __addLogForCountDown(self, log, interval):
        self.logger.info(log)
        self.UtilTime.sleep(interval)

    def log_countDown(self, log, range_max=30, interval=5, range_min=0):
        # reLog = lambda x: self.logger.info(log + " > Time left: %s s." % str(x))
        reLog = lambda x: self.__addLogForCountDown(log + " > Time left: %s s." % str(x), interval)
        self.UtilTime.countDown(range_max, reLog, interval, range_min)

    def __getOSLanguage(self):
        self._osLanguage = self.UtilOS.getOSLocale() # not work in dp

    def __setupENV(self):
        # self._ConfigParser.getRunTimeConfigArgsValue(self._ConfigParser.TEST_TIMEOUT_ELEMENT)
        self.path_folder_results = os.path.join(self._path_folder_AutoTestPass, "results")

        #self.Result.path_folder_currentTest = os.path.join(self.Result.path_folder_results, self.UtilTime.getCurrentTime())
        self.path_folder_currentTest = os.path.join(self.path_folder_results, GlobalArgs.getGlobalStartTime())

        self.path_folder_screenshots = os.path.join(self.path_folder_currentTest, "screenshots")
        self.path_file_xsl_xmlReport = os.path.join(self._path_folder_src, "base", "report", "xml", self.NAME_FILE_XSL)

        self.UtilFolder.createFolder(self.path_folder_results)
        self.UtilFolder.createFolder(self.path_folder_currentTest)
        # self.UtilFolder.createFolder(self.Result.path_folder_screenshots)
        self.UtilFile.copyFile(self.path_file_xsl_xmlReport, os.path.join(self.path_folder_currentTest, self.NAME_FILE_XSL))

    def __getFrameworkBasePaths(self):
        self._path_folder_AutoTestPass = PATH("../../..")
        self._path_folder_resources = PATH("../../../resources")
        self._path_folder_src = PATH("../../../src")
        self._path_folder_conf = os.path.join(self._path_folder_resources, "conf")
        # self._path_folder_browserDriver = os.path.join(self._path_folder_resources, "browserDriver")
        self._path_folder_browserDriver = PATH("./../../../../browserDriver")
        self._path_file_mainConf = os.path.join(self._path_folder_conf, "main.conf")
        self._path_folder_data = os.path.join(self._path_folder_project, "data")

    def __getCurrentProjectArgs(self):
        self._ConfigParser = ConfigParse()
        self.__MainConfig = self._ConfigParser.getConf(self._path_file_mainConf)
        self._ConfigParser.setMainConfig(self.__MainConfig)
        self.testType = self._ConfigParser.getMainConfigValue(self._name_project, self._ConfigParser.CURRENT_TEST_TYPE)
        # self._browser = self._ConfigParser.getMainConfigValue(self._name_project, self._ConfigParser.BROWSER)

    def __initializeLogging(self):
        logging.config.fileConfig(os.path.join(self._path_folder_conf, "log.conf"))
        self.logger = logging.getLogger("simpleExample")

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

