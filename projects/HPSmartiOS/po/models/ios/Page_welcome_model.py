import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Welcome page'''
class Page_welcome_model(IosCommonPage):
    page_name = 'page_welcome'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_start(self):
        return self.get(inspect.stack()[0][3])
