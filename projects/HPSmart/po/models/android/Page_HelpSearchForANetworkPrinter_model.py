import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''HelpSearchForANetworkPrinter page.'''
class Page_HelpSearchForANetworkPrinter_model(AndroidCommonPage):
    page_name = 'page_HelpSearchForANetworkPrinter'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def checkBox_1(self):
        return self.get(inspect.stack()[0][3])

    def checkBox_2(self):
        return self.get(inspect.stack()[0][3])

    def checkBox_3(self):
        return self.get(inspect.stack()[0][3])

    def button_tryAgain(self):
        return self.get(inspect.stack()[0][3])
