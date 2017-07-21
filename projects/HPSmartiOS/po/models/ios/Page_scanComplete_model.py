import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_scanComplete_model(IosCommonPage):
    page_name = 'page_scanComplete'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_save(self):
        return self.get(inspect.stack()[0][3])

    def button_addJob(self):
        return self.get(inspect.stack()[0][3])
