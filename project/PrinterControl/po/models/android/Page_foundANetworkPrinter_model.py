import inspect
from src.base.fwk.CommonPage import CommonPage


'''We found a network printer!'''
class Page_foundANetworkPrinter_model(CommonPage):
    page_name = 'page_foundANetworkPrinter'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def button_continue(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
