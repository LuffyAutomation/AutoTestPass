import os

from fwk.object.WebDriver import WebDriver

from fwk.base.UiFwk import UiFwk

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class WebFwk(UiFwk):
    def __init__(self, Init):
        UiFwk.__init__(self, Init)
        self._Init = Init
        self.path_file_xlsx_testData = self._Init.path_file_xlsx_testData_web

    def getDriver(self):
        self.logger.info("Connecting Web > %s driver." % self.RunTimeConf.browser.lower())
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


