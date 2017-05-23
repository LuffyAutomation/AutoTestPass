import os

from fwk.base.UiFwk import UiFwk
from fwk.utils.ApiRequest import wdaRun

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class IosFwk(UiFwk):

    def __init__(self, Init):
        UiFwk.__init__(self, Init)
        self.path_file_xlsx_testData = Init.path_file_xlsx_testData_ios

    def updateCurrentElementStatus(self, element_name, uiMap, currentPage):
        if self._currentElementName != element_name:
            self._currentElementObject = None
        self._currentUiMap = uiMap
        self._currentPage = currentPage
        self._currentElementName = element_name
        return self

    def getDriver(self):
        self._getCurrentTestArgs(self.TestType.IOS)
        # if self._driver == None:
        #     self._driver = WebDriver(self).getDriver()
        #     self.wait(2)
        self.hasGotDriver = True
        return self._driver


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