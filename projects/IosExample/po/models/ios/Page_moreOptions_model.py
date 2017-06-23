import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''.'''
class Page_moreOptions_model(IosCommonPage):
    page_name = 'page_moreOptions'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def toggleSwitchOn_offerToReduceSize(self):
        return self.get(inspect.stack()[0][3])

    def toggleSwitchOff_offerToReduceSize(self):
        return self.get(inspect.stack()[0][3])
