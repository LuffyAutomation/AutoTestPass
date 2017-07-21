import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''touch printer image'''
class Page_printerInfor_model(IosCommonPage):
    page_name = 'page_printerInfor'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def test_differentPrinter(self):
        return self.get(inspect.stack()[0][3])
