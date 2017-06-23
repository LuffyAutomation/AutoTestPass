import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''iphone7?.'''
class Sys_general_model(IosCommonPage):
    page_name = 'sys_general'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_allow(self):
        return self.get(inspect.stack()[0][3])

    def button_donotallow(self):
        return self.get(inspect.stack()[0][3])
