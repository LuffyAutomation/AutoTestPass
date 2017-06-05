import os

from fwk.utils.utilOS.UtilOS import UtilOS

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class RunTimeConf:
    isDevicePassTest = False
    isLocalTest = False
    isMobileTest = False
    isWebTest = False
    platform = ""
    platformVersion = ""
    deviceName = ""
    newCommandTimeout = ""
    appPackage = ""
    appActivity = ""
    appWaitActivity = ""
    app = ""
    appiumServerIP = ""
    appiumServerPort = ""
    automationName = ""
    browser = ""
    sdk = ""
    deviceModel = ""
    language = ""
    region = ""

    # get
    def __init__(self, _ConfigParser):
        self._UtilOS = UtilOS
        self._ConfigParser = _ConfigParser
        if os.getenv("APPIUM_PLATFORM") is not None:
            self.isDevicePassTest = True

            self.isMobileTest = True
            self.isWebTest = False
            self.platform = os.getenv("APPIUM_PLATFORM")
            self.platformVersion = os.getenv("APPIUM_DEVICE_VERSION")
            self.automationName = os.getenv("APPIUM_AUTOMATION_NAME")
            self.deviceName = os.getenv("APPIUM_DEVICE_NAME")
            self.newCommandTimeout = os.getenv("APPIUM_NEW_COMMAND_TIMEOUT")
            # desired_caps['newCommandTimeout'] = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_NEWCOMMAND_TIMEOUT)
            self.app = PATH(os.getenv("APPIUM_APP_FILE"))
            self.appPackage = os.getenv("APPIUM_APP_PACKAGE")
            self.appActivity = os.getenv("APPIUM_APP_ACTIVITY")
            self.appiumUrl = os.getenv("APPIUM_URL")

            self.appBundleId = os.getenv("APP_BUNDLEIDENTIFIER")
            self.appUdid = os.getenv("APP_UDID")

        elif self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_ACTIVITY) is not None or self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_UDID) is not None:
            self.isDevicePassTest = False

            self.isMobileTest = True
            self.isWebTest = False

            self._ConfigParser = _ConfigParser
            self.platform = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_DEVICE_PLATFORMNAME)
            self.platformVersion = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_DEVICE_VERSION)
            if self.platformVersion is None:
                self.platformVersion = "NA"
            self.deviceName = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_DEVICE_NAME)
            self.newCommandTimeout = self._ConfigParser.getRunTimeConfigCapsValue(
                self._ConfigParser.APP_NEWCOMMAND_TIMEOUT)
            self.appPackage = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_PACKAGE)
            self.appActivity = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_ACTIVITY)
            self.appWaitActivity = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_WAITACTIVITY)
            self.app = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_PATH)

            if not self.app.lower().startswith("/volumes"):
                self.app = PATH(self.app)

            self.appiumServerIP = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_APPIUM_SERVERIP)
            self.appiumServerPort = self._ConfigParser.getRunTimeConfigCapsValue(
                self._ConfigParser.APP_APPIUM_SERVERPORT)
            self.appiumUrl = "http://" + self.appiumServerIP + ":" + self.appiumServerPort + "/wd/hub"
            # self.automationName = "LocalTest" # do not work for 164
            self.automationName = None

            self.appBundleId = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_BUNDLEID)
            self.appUdid = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.APP_UDID)
        else:  # web
            self.isDevicePassTest = False
            self.isMobileTest = False
            self.isWebTest = True
            self.deviceName = "NA"
            self.deviceModel = "NA"
            self.browser = self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.BROWSER)
            self.browserDriverFolderPath = PATH(self._ConfigParser.getRunTimeConfigCapsValue(self._ConfigParser.TEST_BROWSERDRIVER_FOLDERPATH))
            self.language = self._UtilOS.getOSLocale().split("_")[0]
            self.region = self._UtilOS.getOSLocale().split("_")[1]
            self.platform = self._UtilOS.getOSName()
            self.platformVersion = self._UtilOS.getOSRelease()

    def getMobileInfo(self, UI):
        self.UI = UI
        global lines
        lines = []
        if self.platform.lower().strip() == "android":
            lines = self.UI.getMobilePropReadlines(self.deviceName)
        elif self.platform.lower().strip() == "ios":
            lines = ['ro.product.locale.language=en', 'ro.product.locale.region=US', 'ro.product.model=' + self.deviceName, 'ro.build.version.release=' + self.platformVersion, 'ro.build.version.sdk=' + self.platformVersion]
        if len(lines) == 0:
            raise Exception("Can not get mobile information. Please check if mobile [%s] connected correctly." % self.deviceName)
        self.__setMobileDetails(lines)

    def getWebInfo(self, UI):
        self.UI = UI

    def __setMobileDetails(self, lines):
        #self.UI.logger.info(self.platform.lower().strip() == "android")
        if self.platform.lower().strip() == "android" or self.platform.lower().strip() == "ios":
            for line in lines:
                if line.decode('utf-8').strip().split("=")[0] == "ro.product.locale.language":
                    self.language = line.decode('utf-8').strip().split("=")[1]
                elif line.decode('utf-8').strip().split("=")[0] == "ro.product.locale.region":
                    self.region = line.decode('utf-8').strip().split("=")[1]
                elif line.decode('utf-8').strip().split("=")[0] == "ro.product.model":
                    self.deviceModel = line.decode('utf-8').strip().split("=")[1]
                elif line.decode('utf-8').strip().split("=")[0] == "ro.build.version.release":
                    self.platformVersion = line.decode('utf-8').strip().split("=")[1]
                elif line.decode('utf-8').strip().split("=")[0] == "ro.build.version.sdk":
                    self.sdk = line.decode('utf-8').strip().split("=")[1]
        if self.language == "" or self.region == "":  # 6.0
            if self.platform.lower().strip() == "android":
                t = self.UI.getBuildInMobileLanguage(self.deviceName)
                self.language = t.split("-")[0]
                self.region = t.split("-")[1]
            else:
                self.language = "en"
                self.region = "US"
        self._path_file_localXml = os.path.join(self.UI._path_folder_uiMaps, self.UI.getLanguageRegion() + ".xml")
        if self.language != "en":  # en_US.xml needn't be loaded.
            self._xmlTreeLocalXml = self.UI.UtilXml.getTree(self._path_file_localXml)
            self._rootLocalXml = self.UI.UtilXml.getRootElement(self._xmlTreeLocalXml)
