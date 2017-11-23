from projects.WebExample.po.pages.web.Page_home2 import Page_home2
from projects.WebExample.po.pages.web.Page_home import Page_home

class Pages_Web:
    def __init__(self, UI):
        self._UI = UI
        self.Page_home2 = Page_home2(self._UI)
        self._UI.getDriver()
        self.Page_home = Page_home(self._UI)
