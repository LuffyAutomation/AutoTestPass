import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''helpCenter page.'''
class Page_helpCenter_model(AndroidCommonPage):
    page_name = 'page_helpCenter'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def option_HowToPrint_(self):
        return self.get(inspect.stack()[0][3])

    def option_PrintQualityTools(self):
        return self.get(inspect.stack()[0][3])

    def option_ConnectionIssues(self):
        return self.get(inspect.stack()[0][3])

    def option_OnlineSupport(self):
        return self.get(inspect.stack()[0][3])

    def option_ContactHPonFacebookMessenger(self):
        return self.get(inspect.stack()[0][3])

    def option_SendFeedback(self):
        return self.get(inspect.stack()[0][3])
