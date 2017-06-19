import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''We find new printer.'''
class Page_findNewPrinter_model(AndroidCommonPage):
    page_name = 'page_findNewPrinter'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_continue(self):
        return self.get(inspect.stack()[0][3])
