import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Connection Issues page.'''
class Page_ConnectionIssues_model(AndroidCommonPage):
    page_name = 'page_ConnectionIssues'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def title_MyPrinterIsNotListed(self):
        return self.get(inspect.stack()[0][3])

    def button_HelpSetUpANewPrinter(self):
        return self.get(inspect.stack()[0][3])

    def button_HelpSearchForANetworkPrinter(self):
        return self.get(inspect.stack()[0][3])
