from projects.IosExample.po.pages.ios.Page_home import Page_home
from projects.IosExample.po.pages.ios.Sys_general import Sys_general
from projects.IosExample.po.pages.ios.Page_termsAndConditions import Page_termsAndConditions
from projects.IosExample.po.pages.ios.Page_welcome import Page_welcome


class Pages_Ios:
    def __init__(self, UI):
        self._UI = UI
        self.Page_home = Page_home(self._UI)
        self.Sys_general = Sys_general(self._UI)
        self.Page_termsAndConditions = Page_termsAndConditions(self._UI)
        self.Page_welcome = Page_welcome(self._UI)
