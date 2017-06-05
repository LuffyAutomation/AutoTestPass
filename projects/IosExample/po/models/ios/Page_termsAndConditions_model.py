import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Terms and Conditions.'''
class Page_termsAndConditions_model(IosCommonPage):
    page_name = 'page_termsAndConditions'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def checkbox_1(self):
        return self.get(inspect.stack()[0][3])
