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
        if self._driver is None:
            self._driver = WebDriver(self).getDriver()
            self.wait(2)
        self.hasGotDriver = True
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


