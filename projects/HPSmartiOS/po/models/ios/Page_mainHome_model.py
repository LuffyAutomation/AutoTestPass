import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Mobility phone home screen'''
class Page_mainHome_model(IosCommonPage):
    page_name = 'page_mainHome'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def home_settings(self):
        return self.get(inspect.stack()[0][3])
