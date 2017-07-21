import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch Add printer button from printers page.'''
class Page_connectThePrinter_model(IosCommonPage):
    page_name = 'page_connectThePrinter'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def enterComment(self):
        return self.get(inspect.stack()[0][3])

    def keyboard_done(self):
        return self.get(inspect.stack()[0][3])
