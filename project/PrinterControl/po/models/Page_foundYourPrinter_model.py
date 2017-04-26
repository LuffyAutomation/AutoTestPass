import inspect

from project.PrinterControl.po.CommonPage import CommonPage

'''We found your printer.'''
class Page_foundYourPrinter_model(CommonPage):
    page_name = 'page_foundYourPrinter'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def link_changePrinter(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def button_continue(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def button_later(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
