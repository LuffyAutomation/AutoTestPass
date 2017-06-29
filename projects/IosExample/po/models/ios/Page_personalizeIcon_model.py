import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''personalizeIcon'''
class Page_personalizeIcon_model(IosCommonPage):
    page_name = 'page_personalizeIcon'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def buttonOrder_scanToEmail(self):
        return self.get(inspect.stack()[0][3])

    def buttonOrder_scan(self):
        return self.get(inspect.stack()[0][3])
