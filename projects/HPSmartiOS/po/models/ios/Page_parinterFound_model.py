import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_parinterFound_model(IosCommonPage):
    page_name = 'page_parinterFound'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_yes(self):
        return self.get(inspect.stack()[0][3])

    def button_no(self):
        return self.get(inspect.stack()[0][3])
