from projects.HPSmart.po.pages.ios.Page_other import Page_other
from projects.HPSmart.po.pages.ios.Page_first import Page_first


class Pages_Ios:
    def __init__(self, UI):
        self._UI = UI
        self.Page_other = Page_other(self._UI)
        self.Page_first = Page_first(self._UI)
