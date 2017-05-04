import logging
import logging.config
import os

from fwk.base.GlobalArgs import GlobalArgs
from fwk.utils.utilConsole.UtilConsole import UtilConsole
from fwk.utils.utilIO.UtilFile import UtilFile
from fwk.utils.utilIO.UtilFolder import UtilFolder
from fwk.utils.utilOS.UtilOS import UtilOS
from fwk.utils.utilTime.UtilTime import UtilTime
from fwk.utils.utilTime.UtilWaitEvent import UtilWaitEvent

from fwk.other.ConfigParser import ConfigParse
from fwk.utils.utilXml.UtilXml import UtilXml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class InitFwk:
    NAME_FILE_XSL = "xmlReport.xsl"

    class TestType:
        ANDROID = 'Android'
        IOS = "Ios"
        WEB = "Web"

    def __init__(self, name_project=None, path_folder_project=None):
        self.UtilFolder = UtilFolder
        self.UtilTime = UtilTime
        self.UtilFile = UtilFile
        self.UtilXml = UtilXml
        self.UtilOS = UtilOS
        self.UtilConsole = UtilConsole
        self.UtilWaitEvent = UtilWaitEvent
        self.name_project = name_project
        self._path_folder_project = path_folder_project
        self.__setup()

    def __setup(self):
        self.__getFrameworkBasePaths()
        self.__getCurrentProjectArgs()
        self.__initializeLogging()

    def __addLogForCountDown(self, log, interval):
        self.logger.info(log)
        self.UtilTime.sleep(interval)

    def log_countDown(self, log, range_max=30, interval=5, range_min=0):
        # reLog = lambda x: self.logger.info(log + " > Time left: %s s." % str(x))
        reLog = lambda x: self.__addLogForCountDown(log + " > Time left: %s s." % str(x), interval)
        self.UtilTime.countDown(range_max, reLog, interval, range_min)

    def __getOSLanguage(self):
        self._osLanguage = self.UtilOS.getOSLocale()  # not work in dp

    def createResultFolder(self):
        # self._ConfigParser.getRunTimeConfigArgsValue(self._ConfigParser.TEST_TIMEOUT_ELEMENT)
        self.path_folder_results = os.path.join(self._path_folder_AutoTestPass, "results")

        #self.Result.path_folder_currentTest = os.path.join(self.Result.path_folder_results, self.UtilTime.getCurrentTime())
        self.path_folder_currentTest = os.path.join(self.path_folder_results, GlobalArgs.getGlobalStartTime())

        self.path_folder_screenshots = os.path.join(self.path_folder_currentTest, "screenshots")
        self.path_file_xsl_xmlReport = os.path.join(self._path_folder_fwk, "report", "xml", self.NAME_FILE_XSL)

        self.UtilFolder.createFolder(self.path_folder_results)
        self.UtilFolder.createFolder(self.path_folder_currentTest)
        # self.UtilFolder.createFolder(self.Result.path_folder_screenshots)
        self.UtilFile.copyFile(self.path_file_xsl_xmlReport, os.path.join(self.path_folder_currentTest, self.NAME_FILE_XSL))

    def __getFrameworkBasePaths(self):
        self._path_folder_AutoTestPass = PATH("../..")
        self._path_folder_fwk = os.path.join(self._path_folder_AutoTestPass, "fwk")
        self._path_folder_projects = os.path.join(self._path_folder_AutoTestPass, "projects")
        self._path_folder_env = os.path.join(self._path_folder_fwk, "env")
        self._path_folder_conf = os.path.join(self._path_folder_env, "conf")
        # self._path_folder_browserDriver = os.path.join(self._path_folder_resources, "browserDriver")
        # self._path_folder_browserDriver = PATH("./../../../../browserDriver")
        self._path_file_mainConf = os.path.join(self._path_folder_conf, "main.conf")

    def __getCurrentProjectArgs(self):
        self._ConfigParser = ConfigParse()
        self.__MainConfig = self._ConfigParser.getConf(self._path_file_mainConf)
        self._ConfigParser.setMainConfig(self.__MainConfig)
        if self.name_project is None or self.name_project == "":
            self.name_project = self._ConfigParser.getMainConfigValue(self._ConfigParser.DEFAULTPROJECT, self._ConfigParser.DEFAULT_PROJECT)

        self._path_folder_data = os.path.join(self._path_folder_projects, self.name_project, "data")
        self.testType = self._ConfigParser.getMainConfigValue(self.name_project, self._ConfigParser.CURRENT_TEST_TYPE)
        # self._browser = self._ConfigParser.getMainConfigValue(self._name_project, self._ConfigParser.BROWSER)

    def __initializeLogging(self):
        logging.config.fileConfig(os.path.join(self._path_folder_conf, "log.conf"))
        self.logger = logging.getLogger("simpleExample")

    # def _getAppInfo(self):
    #     self._DefaultPage = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//DefaultPage"))
    #     self.__appConfFolderName = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//AppName"))
    #     self.__Version = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Version"))
    #     self.__Environment = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Environment"))
    #     self.__TestCategory = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//TestCategory"))
    #     self.__NetWork = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Network"))
    #     self.__Description = self.UtilXml.getEelmentText(self.UtilXml.getElementByXpath(self._root, ".//Description"))
    #
    #     self.logger.info("Default Page : " + self._DefaultPage)
    #     self.logger.info("App Name : " + self.__appConfFolderName)
    #     self.logger.info("App Version : " + self.__Version)
    #     self.logger.info("Test Environment : " + self.__Environment)
    #     self.logger.info(self.__TestCategory)
    #     self.logger.info("Test NewWork : " + self.__NetWork)
    #     self.logger.info("Description : " + self.__Description)

    def isEmpty(self, str, defaultStr):
        if str == "" or str is None:
            return defaultStr
        else:
            return str

    # def log(self, message, level=1):
    #     if level == 1:
    #         self.logger.info(message)
    #     if level == 2:
    #         self.logger.warning(message)
    #     if level == 3:
    #         self.logger.debug(message)
    #     if level == 4:
    #         self.logger.error(message)
