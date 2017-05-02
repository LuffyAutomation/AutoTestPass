from configparser import ConfigParser

class ConfigParse:
    def __init__(self):
        pass

    def setMainConfig(self, MainConfig):
        self._MainConfig = MainConfig

    # def addMainConfig(self, section, MainConfig):
    #     self._MainConfigSection = section
    #     self._MainConfig = MainConfig

    SECTION_CAPS = "caps"
    SECTION_ARGS = "args"
    TEST_TIMEOUT_ELEMENT = "test.timeout.element"
    TEST_RESULTS_FOLDERPATH = "test.results.folderPath "
    TEST_SCREENSHOTS_FOLDERPATH = "test.screenshots.folderPath"
    TEST_UIMAP_FILENAME = "test.uiMap.fileName"
    CURRENT_TEST_TYPE = "current.test.type"

    BROWSER = "browser"

    APP_DEVICE_PLATFORMNAME = "app.device.platformName"
    APP_DEVICE_VERSION = "app.device.version"
    APP_DEVICE_NAME = "app.device.name"
    APP_NEWCOMMAND_TIMEOUT = "app.newCommand.timeout"
    APP_PACKAGE = "app.package"
    APP_ACTIVITY = "app.activity"
    APP_WAITACTIVITY = "app.waitActivity"
    APP_PATH = "app.path"
    APP_APPIUM_SERVERIP = "app.appium.serverIP"
    APP_APPIUM_SERVERPORT = "app.appium.serverPort"

    def setRunTimeConfig(self, RunTimeConfig):
        self._RunTimeConfig = RunTimeConfig

    def getRunTimeConfigCapsValue(self, key):
        try:
            return self.getConfigValue(self._RunTimeConfig, self.SECTION_CAPS, key)
        except:
            return None

    def getRunTimeConfigArgsValue(self, key):
        try:
            return self.getConfigValue(self._RunTimeConfig, self.SECTION_ARGS, key)
        except:
            return None

    def getMainConfigValue(self, section, key):
        try:
            return self.getConfigValue(self._MainConfig, section, key)
        except:
            return None

    def getConf(self, path):
        conf = ConfigParser()
        conf.read(path, "utf-8")
        return conf

    def getSection(self, conf):
        return conf.sections()

    def getConfigValue(self, conf, section, key):
        return conf.get(section, key)