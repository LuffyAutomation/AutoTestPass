import os
from selenium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class WebDriver:
    BROWSER = "Browser"

    def __init__(self, UI):
        self.desired_caps = {}
        self._UI = UI
        self._RunTimeConf = self._UI.RunTimeConf
        #self.__getDesiredCapsList()

    def getFireFoxDriver(self):
        return webdriver.Firefox()

    def getChromeDriver(self):
        return webdriver.Chrome()

    def getIeDriver(self):
        return webdriver.Ie()

    def getEdgeDriver(self):
        return webdriver.Edge()

    _driver_FireFox = None
    _driver_Chrome = None
    _driver_IE = None
    _driver_Edge = None
    def getDriver(self):
        self.logger.info("Connecting Web > %s driver." % self._RunTimeConf.browser.lower())
        os.environ["PATH"] += ";" + str(self._RunTimeConf.browserDriverFolderPath)
        if self._driver is None:
            if self._RunTimeConf.browser.lower() == "firefox":
                self._driver = self.getFireFoxDriver()
            elif self._RunTimeConf.browser.lower() == "chrome":
                self._driver = self.getChromeDriver()
        else:
            self.logger.info("The Android driver has existed.")
        if self._driver is not None:
            self.hasGotDriver = True
        return self._driver
    def __getDesiredCapsList(self):
        self.desired_caps = {
            self.BROWSER: self._RunTimeConf.browser
        }
        return self.desired_caps