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
    # IOS
    APP_BUNDLEID = "bundleId"
    APP_UDID = "udid"
    BROWSER_NAME = "browserName"

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
        }
        if self._RunTimeConf.platformVersion.lower() != "na":  # don't have to write this in runTimConf but NA will cause error.
            self.desired_caps[self.PLATFORM_VERSION] = self._RunTimeConf.platformVersion.lower()
        if self._UI.testType.lower() == "ios":
            if self._RunTimeConf.appBundleId is not None:
                self.desired_caps[self.APP_BUNDLEID] = self._RunTimeConf.appBundleId

            self.desired_caps[self.APP_UDID] = self._RunTimeConf.appUdid
            self.desired_caps[self.AUTOMATION_NAME] = "XCUITest"
        else:
            if self._RunTimeConf.appPackage is not None:
                self.desired_caps[self.APP_PACKAGE] = self._RunTimeConf.appPackage
            if self._RunTimeConf.appActivity is not None:
                self.desired_caps[self.APP_ACTIVITY] = self._RunTimeConf.appActivity
        # if self._RunTimeConf.automationName is not None:
        #     self.desired_caps[self.AUTOMATION_NAME] = self._RunTimeConf.automationName
        if self._RunTimeConf.mobileBrowserName is not None and self._RunTimeConf.mobileBrowserName != "":
            self.desired_caps[self.BROWSER_NAME] = self._RunTimeConf.mobileBrowserName
            if self._UI.testType.lower() == "ios":
                self.desired_caps["startIWDP"] = True
                self.desired_caps["autoWebView"] = True
                self.desired_caps['safariInitialUrl'] = 'https://www.baidu.com'
        if self._RunTimeConf.app is not None:
            self.desired_caps[self.APP] = self._RunTimeConf.app
        # 'autoWebView': True,
        # 'clearSystemFiles': True
        # 'webkitResponseTimeout': 50000,
            self.desired_caps["clearSystemFiles"] = True
        if self._RunTimeConf.automationName is not None and self._RunTimeConf.appWaitActivity is not None:
            self.desired_caps[self.APP_WAIT_ACTIVITY] = self._RunTimeConf.appWaitActivity
        return self.desired_caps
        # capabilities.setCapability("browserName", "Chrome");
        # capabilities.setCapability("appPackage", "com.android.browser");
        # capabilities.setCapability("appActivity", ".BrowserActivity");
        # capabilities.setCapability("unicodeKeyboard", true);
        # capabilities.setCapability("resetKeyboard", true);