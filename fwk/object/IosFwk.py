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

    def updateCurrentElementStatus(self, element_name, uiMap, currentPage):
        if self._currentElementName != element_name:
            self._currentElementObject = None
        self._currentUiMap = uiMap
        self._currentPage = currentPage
        self._currentElementName = element_name
        return self

    def getMobilePropReadlines(self, uuid=None):
        if uuid is None:
            uuid = self.RunTimeConf.deviceName
        str = "adb -s %s shell cat /system/build.prop" % uuid
        data = subprocess.Popen(str, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        lines = data.stdout.readlines()
        # for prop in li:
        #     prop.decode('utf-8').strip().split("=")
        return lines

    def openApp(self,bundleId=None, page=""):
        self.UiMapSetPage(page)
        if os.getenv('APP_DEVICE_PLATFORMNAME') == None:
            self.__launch_app(bundleId)
        else:
            self.__launch_app_DP()
        self.wda = wdaRun()

    def tapForPoint(self, x, y):
        self.wda.tap(x, y)

    def keys(self, value):
        self.wda.keys(value)

    def home(self):
        self.wda.home()

    def launchApp(self,bundleId):
        self.openApp(bundleId)


    def flick(self, start_x, start_y, end_x, end_y):
        self._driver.flick(start_x, start_y, end_x, end_y)