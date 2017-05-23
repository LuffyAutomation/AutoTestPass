import os

from fwk.object.WebDriver import WebDriver

from fwk.base.UiBaseFwk import UiBaseFwk

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WebFwk(UiBaseFwk):

    def __init__(self, Init):
        UiBaseFwk.__init__(self, Init)
        self.path_file_xlsx_testData = Init.path_file_xlsx_testData_web

    def getDriver(self):
        self._getCurrentTestArgs(self.TestType.WEB)
        if self._driver == None:
            self._driver = WebDriver(self).getDriver()
            self.wait(2)
        self.hasGotDriver = True
        return self._driver

    def updateCurrentElementStatus(self, element_name, uiMap, currentPage):
        if self._currentElementName != element_name:
            self._currentElementObject = None
        self._currentUiMap = uiMap
        self._currentPage = currentPage
        self._currentElementName = element_name
        return self

    def openUrl(self, url):
        self.logger.info("Navigate to [" + url + "].")
        self._driver.get(url)
        #self.RunTimeConf.getMobileInfo(self)

