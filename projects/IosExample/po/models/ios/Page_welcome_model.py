import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''First Page.'''
class Page_welcome_model(IosCommonPage):
    page_name = 'page_welcome'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def image_welcome(self):
        return self.get(inspect.stack()[0][3])

    def button_start(self):
        return self.get(inspect.stack()[0][3])
