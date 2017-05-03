import os
from appium import webdriver
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MobileDriver:
    PLATFORM = "platformName"
    PLATFORM_VERSION = "platformVersion"
    AUTOMATION_NAME = "automationName"
    DEVICE_NAME = "deviceName"
    NEW_COMMAND_TIMEOUT = "newCommandTimeout"
    APP = "app"
    APP_PACKAGE = "appPackage"
    APP_WAIT_ACTIVITY = "appWaitActivity"
    APP_ACTIVITY = "appActivity"

    def __init__(self, UI):
        self.desired_caps = {}
        self._UI = UI
        self._RunTimeConf = self._UI.RunTimeConf
        self.__getDesiredCapsList()

    def getDriver(self):
        try:
            return webdriver.Remote(self._RunTimeConf.appiumUrl, self.desired_caps)
        except Exception as e:
            raise Exception(str(e.__str__()))

    def __getDesiredCapsList(self):
        self.desired_caps = {
            self.PLATFORM: self._RunTimeConf.platform,
            # self.PLATFORM_VERSION: self._RunTimeConf.platformVersion,
            self.DEVICE_NAME: self._RunTimeConf.deviceName,
            self.NEW_COMMAND_TIMEOUT: self._RunTimeConf.newCommandTimeout,
            self.APP_PACKAGE: self._RunTimeConf.appPackage,
            self.APP_ACTIVITY: self._RunTimeConf.appActivity,
            self.APP: PATH(self._RunTimeConf.app)
        }
        if self._RunTimeConf.automationName is not None:
            self.desired_caps[self.AUTOMATION_NAME] = self._RunTimeConf.automationName
        if self._RunTimeConf.automationName is not None:
            self.desired_caps[self.APP_WAIT_ACTIVITY] = self._RunTimeConf.appWaitActivity
        return self.desired_caps