import os
from src.base.core.UiFramework import UIFramework
from src.base.core.WebDriver import WebDriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Web(UIFramework):

    def __init__(self):
        UIFramework.__init__(self)
        self.__get_driver()

    def __get_driver(self):
        self._driver = WebDriver(self).getDriver()
        self.wait(2)

    def openUrl(self, url):
        self.logger.info("Navigate to [" + url + "].")
        self._driver.get(url)
        #self.RunTimeConf.getMobileInfo(self)

