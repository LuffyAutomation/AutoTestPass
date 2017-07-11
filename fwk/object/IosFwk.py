import os
import subprocess
from fwk.base.UiFwk import UiFwk
from fwk.utils.ApiRequest import wdaRun
from fwk.object.MobileDriver import MobileDriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class IosFwk(UiFwk):

    def __init__(self, Init):
        UiFwk.__init__(self, Init)
        self._Init = Init
        self.path_file_xlsx_testData = self._Init.path_file_xlsx_testData_ios

    def __launch_app(self):
        self._driver = MobileDriver(self).getDriver()
        self.hasGotDriver = True
        self._Init.log_countDown("Connecting......", 3)
        return self._driver

    def getDriver(self):
        self.logger.info("Connecting Ios driver.")
        self._getCurrentTestArgs(self.TestType.IOS)
        if self._driver is None:
           self.__launch_app()
           self.RunTimeConf.getMobileInfo(self)
        else:
            self.logger.info("The Ios driver has existed.")
        return self._driver

    def updateCurrentElementStatus(self, element_name, uiMap, page_name):
        if self.CurrentElement.name != element_name:
            self.LastElement.object = self.CurrentElement.object
            self.LastElement.page_uiMap = self.CurrentElement.page_uiMap
            self.LastElement.page_name = self.CurrentElement.page_name
            self.LastElement.list_locators = self.CurrentElement.list_locators
            self.CurrentElement.object = None
            self.CurrentElement.list_locators = None
        self.CurrentElement.page_uiMap = uiMap
        self.LastElement.name = self.CurrentElement.name
        self.CurrentElement.page_name = page_name
        self.CurrentElement.name = element_name
        return self

        # self._driver.swipe((320 * 0.75), (100), (-320 * 0.25), (0), 1500)

        # def setCode(self, value):
        #     letterToCodeHashMap = {}
        #     lettersStr = "0 1 2 3 4 5 6 7 8 9".split()
        #     androidCodes = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        #     for index in range(len(lettersStr)):
        #         letterToCodeHashMap[lettersStr[index]] = androidCodes[index]
        #     for i in range(len(value)):
        #         code = letterToCodeHashMap.get(value[i])
        #         self.clickOn(code)
        #         # self.waitForTimeOut(800)
        #
        # def setPwd(self, value):
        #     # letterToCodeHashMap = {}
        #     # lettersStr = "0 1 2 3 4 5 6 7 8 9".split()
        #     androidCodes = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
        #     elementName = None
        #     for index in range(len(androidCodes)):
        #         name = self.getValueOf(androidCodes[index])
        #         if name == "0":
        #             self.log("Name : " + name)
        #             elementName = androidCodes[index]
        #             break;
        #     for k in range(6):
        #         # self.waitForTimeOut(500)
        #         self.clickOn(elementName)
    # def openApp(self,bundleId=None, page=""):
    #     self.UiMapSetPage(page)
    #     if os.getenv('APP_DEVICE_PLATFORMNAME') == None:
    #         self.__launch_app(bundleId)
    #     else:
    #         self.__launch_app_DP()
    #     self.wda = wdaRun()
    #
    # def tapForPoint(self, x, y):
    #     self.wda.tap(x, y)
    #
    # def keys(self, value):
    #     self.wda.keys(value)
    #
    # def home(self):
    #     self.wda.home()
    #
    # def launchApp(self,bundleId):
    #     self.openApp(bundleId)


