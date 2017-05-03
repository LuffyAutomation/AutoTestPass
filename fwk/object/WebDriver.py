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

    def getDriver(self):
        os.environ["PATH"] += ";" + str(self._RunTimeConf.browserDriverFolderPath)
        if self._RunTimeConf.browser.lower() == "firefox":
            return self.getFireFoxDriver()
        elif self._RunTimeConf.browser.lower() == "chrome":
            return self.getChromeDriver()


    def __getDesiredCapsList(self):
        self.desired_caps = {
            self.BROWSER: self._RunTimeConf.browser
        }
        return self.desired_caps