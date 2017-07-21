from projects.HPSmartiOS.po.pages.android.Page_about import Page_about
from projects.HPSmartiOS.po.pages.android.Page_appsettings import Page_appsettings
from projects.HPSmartiOS.po.pages.android.Page_home import Page_home
from projects.HPSmartiOS.po.pages.android.Page_welcome import Page_welcome
from projects.HPSmartiOS.po.pages.android.Page_agreements import Page_agreements
from projects.HPSmartiOS.po.pages.android.Dialog import Dialog
from projects.HPSmartiOS.po.pages.android.Page_other import Page_other
from projects.HPSmartiOS.po.pages.android.Page_first import Page_first


class Pages_Android:
    def __init__(self, UI):
        self._UI = UI
        self.Page_about = Page_about(self._UI)
        self.Page_appsettings = Page_appsettings(self._UI)
        self.Page_home = Page_home(self._UI)
        self.Page_welcome = Page_welcome(self._UI)
        self.Page_agreements = Page_agreements(self._UI)
        self.Dialog = Dialog(self._UI)
        self.Page_other = Page_other(self._UI)
        self.Page_first = Page_first(self._UI)


