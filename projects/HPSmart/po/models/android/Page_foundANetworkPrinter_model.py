import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''We found a network printer!'''
class Page_foundANetworkPrinter_model(AndroidCommonPage):
    page_name = 'page_foundANetworkPrinter'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_continue(self):
        return self.get(inspect.stack()[0][3])
