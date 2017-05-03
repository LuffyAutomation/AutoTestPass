import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''We found your printer.'''
class Page_foundYourPrinter_model(AndroidCommonPage):
    page_name = 'page_foundYourPrinter'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def link_changePrinter(self):
        return self.get(inspect.stack()[0][3])

    def button_continue(self):
        return self.get(inspect.stack()[0][3])

    def button_later(self):
        return self.get(inspect.stack()[0][3])
