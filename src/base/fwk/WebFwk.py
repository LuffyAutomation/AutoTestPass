import os
from src.base.core.UiBaseFwk import UiBaseFwk
from src.base.core.WebDriver import WebDriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WebFwk(UiBaseFwk):

    def __init__(self):
        UiBaseFwk.__init__(self)
        self.getDriver()

    def getDriver(self):
        if self._driver == None:
            self._driver = WebDriver(self).getDriver()
            self.wait(2)

    def openUrl(self, url):
        self.logger.info("Navigate to [" + url + "].")
        self._driver.get(url)
        #self.RunTimeConf.getMobileInfo(self)
