import inspect
from src.base.fwk.CommonPage import CommonPage


'''We find new printer.'''
class Page_findNewPrinter_model(CommonPage):
    page_name = 'page_findNewPrinter'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def button_continue(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
