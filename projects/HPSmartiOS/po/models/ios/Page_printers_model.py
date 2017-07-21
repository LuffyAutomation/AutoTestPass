import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''all printer list screen'''
class Page_printers_model(IosCommonPage):
    page_name = 'page_printers'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_addPrinter(self):
        return self.get(inspect.stack()[0][3])

    def printer_1(self):
        return self.get(inspect.stack()[0][3])

    def printer_2(self):
        return self.get(inspect.stack()[0][3])

    def printer_3(self):
        return self.get(inspect.stack()[0][3])

    def printer_4(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])
