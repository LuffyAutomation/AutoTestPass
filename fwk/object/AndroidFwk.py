import os
import subprocess

from fwk.object.MobileDriver import MobileDriver

from fwk.base.UiFwk import UiFwk

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidFwk(UiFwk):
    def __init__(self, Init):
        UiFwk.__init__(self, Init)
        self._Init = Init
        self.path_file_xlsx_testData = self._Init.path_file_xlsx_testData_android

    def __launch_app(self):
        self._driver = MobileDriver(self).getDriver()
        self.hasGotDriver = True
        self._Init.log_countDown("Connecting......", 3)
        return self._driver

    def getDriver(self):
        self.logger.info("Connecting Android driver.")
        self._get_current_test_args(self.TestType.ANDROID)
        if self._driver is None:
           self.__launch_app()
           self.RunTimeConf.get_mobile_info(self)
        else:
            self.logger.info("The Android driver has existed.")
        return self._driver

    def updateCurrentElementStatus(self, element_name, uiMap, page_name):
        if self.CurrentElement.name != element_name:
            self.LastElement.object = self.CurrentElement.object
            self.LastElement.page_uiMap = self.CurrentElement.page_uiMap
            self.LastElement.page_name = self.CurrentElement.page_name
            self.LastElement.list_locators = self.CurrentElement.list_locators
            self.LastElement.index = self.CurrentElement.index
            self.CurrentElement.object = None
            self.CurrentElement.list_locators = None
        self.CurrentElement.page_uiMap = uiMap
        self.LastElement.name = self.CurrentElement.name
        self.CurrentElement.page_name = page_name
        self.CurrentElement.name = element_name
        return self

    def openMobileBrowser(self):
        self.__launch_browser()
        self.wait(1)
        self._driver.get(self._getSutFullFileName("test.url"))

    # def swipeOfType(self, type, duration=1500):
    #     self.logger.info("Swiping " + type + ".")
    #     windows_x = self.getWindowWidth()
    #     windows_y = self.getWindowHeight()
    #     # Sliding screen to the left
    #     if type.lower() == self.SwipeTo.LEFT.lower():
    #         self._driver.swipe((windows_x * 0.9), (windows_y * 0.5), (windows_x * 0.2), (windows_y * 0.5), duration)
    #     # From the left of screen to began to slip
    #     if type.lower() == self.SwipeTo.LEFT_SIDE.lower():
    #         self._driver.swipe(1, (windows_y * 0.5), (windows_x * 0.9), (windows_y * 0.5), 1500)
    #     # Sliding screen to the right
    #     if type.lower() == self.SwipeTo.RIGHT.lower():
    #         self._driver.swipe((windows_x * 0.2), (windows_y * 0.5), (windows_x * 0.9), (windows_y * 0.5), duration)
    #     # From the right of screen to began to slip
    #     if type.lower() == self.SwipeTo.RIGHT_SIDE.lower():
    #         self._driver.swipe((windows_x * 0.9), (windows_y * 0.5), (windows_x * 0.2), (windows_y * 0.5), duration)
    #     # Screen upward sliding
    #     if type.lower() == self.SwipeTo.UP.lower():
    #         self._driver.swipe((windows_x * 0.5), (windows_y * 0.9), (windows_x * 0.5), (windows_y * 0.4), duration)
    #     # From the top of screen to began to slip
    #     if type.lower() == self.SwipeTo.TOP.lower():
    #         self._driver.swipe((windows_x * 0.5), 0, (windows_x * 0.5), (windows_y * 0.8), duration)
    #     # Slide down the screen
    #     if type.lower() == self.SwipeTo.DOWN.lower():
    #         self._driver.swipe((windows_x * 0.5), (windows_y * 0.4), (windows_x * 0.5), (windows_y * 0.9), duration)
    #     # From the bottom of screen to began to slip
    #     if type.lower() == self.SwipeTo.BOTTOM.lower():
    #         self._driver.swipe((windows_x * 0.5), (windows_y * 0.9), (windows_x * 0.5), (windows_y * 0.1), duration)
    #     return self

    def back(self):
        self.logger.info("Click back of the mobile.")
        self._driver.back()
        return self

    def pressKey(self, code):
        self._driver.press_keycode(code)
        return self

    def switchToWebView(self, viewName):
        self._driver.switch_to.context(viewName)
        return self

    def setValueByKeys(self, value):
        letterToCodeHashMap = {}
        lettersStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z @ . + _ 0 1 2 3 4 5 6 7 8 9".split()
        androidCodes = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                        53, 54, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                        51, 52, 53, 54, 77, 56, 81, 69, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        for index in range(len(lettersStr)):
            letterToCodeHashMap[lettersStr[index]] = androidCodes[index]
        for i in range(len(value)):
            code = letterToCodeHashMap.get(value[i])
            self.pressKey(code)
            self.sleep(0.5)
        return self

    def switchToContext(self, webView):
        contextName = self._driver.contexts
        for context in iter(contextName):
            if context == webView:
                self.logger.info("Switch to ui view : " + context)
                self.switchToWebView(context)
        return self

    def logContext(self):
        contextName = self._driver.contexts
        for context in iter(contextName):
            self.logger.info("Context : " + context)
        return self

    def set_networkConnection(self, name):
        self._driver.set_network_connection(connectionType=2)
        """Sets the network connection type. Android only.
           Possible values:
               Value (Alias)      | Data | Wifi | Airplane Mode
               -------------------------------------------------
               0 (None)           | 0    | 0    | 0
               1 (Airplane Mode)  | 0    | 0    | 1
               2 (Wifi only)      | 0    | 1    | 0
               4 (Data only)      | 1    | 0    | 0
               6 (All network on) | 1    | 1    | 0
           These are available through the enumeration `appium.webdriver.ConnectionType"""
        return self
    def setValueByAdbInput(self, value):
        self.logger.info("adb -s " + self.udid + " shell input text " + value)
        os.system("adb -s " + self.udid + " shell input text " + value)
        return self

    def setValueByAdbInputDoubleByte(self, value):
        self.logger.info("adb -s " + self.udid + " shell am broadcast -a ADB_INPUT_TEXT --es msg '" + value + "'")
        os.system("adb -s " + self.udid + " shell am broadcast -a ADB_INPUT_TEXT --es msg '" + value + "'")
        return self

    def crop(self, element, direction):
        x = self.getElemenX(element)
        y = self.getElementY(element)
        if direction == "left":
            self.swipeByNative(x + self.getElementWidth(element) - 1, y, x + self.getElementWidth(element) - 200, y, 1500)
        if direction == "right":
            self.swipeByNative(x, y, x + 200, y, 1500)
        if direction == "up":
            self.swipeByNative(x, y + self.getElementHeight(element) - 1, x, y + self.getElementHeight(element) - 200, 1500)
        if direction == "down":
            self.swipeByNative(x, y, x, y + 200, 1500)

    def getBuildInMobileLanguage(self, uuid=None):
        if uuid is None:
            uuid = self.RunTimeConf.deviceName
        str = "adb -s %s shell getprop persist.sys.language" % uuid  # for 5.0
        if int(self.RunTimeConf.sdk) > 21:
            str = "adb -s %s shell getprop persist.sys.locale" % uuid  # for 6.0
        data = subprocess.Popen(str, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        lines = data.stdout.readlines()
        return lines[0].strip()
        # ret = subprocess.check_output(str)
        # return str(ret.strip()).replace("b", "").replace("'", "")

    # subprocess.check_output not work in DP
    def getAndroidSDK(self, uuid=None):
        if uuid is None:
            uuid = self.RunTimeConf.deviceName
        getLang = "adb -s %s shell getprop ro.build.version.sdk" % uuid
        ret = subprocess.check_output(getLang)
        return int(ret.strip())

    def getMobilePropReadlines(self, uuid=None):
        if uuid is None:
            uuid = self.RunTimeConf.deviceName
        str = "adb -s %s shell cat /system/build.prop" % uuid
        data = subprocess.Popen(str, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        lines = data.stdout.readlines()
        # for prop in li:
        #     prop.decode('utf-8').strip().split("=")
        return lines

    def switchApp(self, app_package, app_activity):
        self.logger.info("Switch to App - app_package: [%s] app_activity: [%s]." % (app_package, app_activity))
        self._driver.start_activity(app_package, app_activity)

    def removeApp(self, app_package):
        self.logger.info("Remove App - app_package: [%s]." % app_package)
        self._driver.remove_app(app_package)  # "com.dropbox.android"

    def installApp(self, app_path):
        self.logger.info("Install App - app_path: [%s]." % app_path)
        self._driver.install_app(self, app_path)
        #  ("adb install your-apk-path.apk");
