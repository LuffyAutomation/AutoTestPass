import os

from fwk.base.UiFwk import UiFwk
from fwk.utils.ApiRequest import wdaRun

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class IosFwk(UiFwk):

    def __init__(self):
        UiBaseFwk.__init__(self)

    def openApp(self,bundleId=None, page=""):
        self.UiMapSetPage(page)
        if os.getenv('APP_DEVICE_PLATFORMNAME') == None:
            self.__launch_app(bundleId)
        else:
            self.__launch_app_DP()
        self.wda = wdaRun()

    def tapForPoint(self, x, y):
        self.wda.tap(x, y)

    def keys(self, value):
        self.wda.keys(value)

    def home(self):
        self.wda.home()

    def launchApp(self,bundleId):
        self.openApp(bundleId)


    def flick(self, start_x, start_y, end_x, end_y):
        self._driver.flick(start_x, start_y, end_x, end_y)