import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''touch HP Online Privacy Statement'''
class Page_linkPrivacyStatement_model(IosCommonPage):
    page_name = 'page_linkPrivacyStatement'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_privacyStatement(self):
        return self.get(inspect.stack()[0][3])

    def button_close(self):
        return self.get(inspect.stack()[0][3])

    def link_privacy(self):
        return self.get(inspect.stack()[0][3])

    def link_siteTerms(self):
        return self.get(inspect.stack()[0][3])

    def text_termsAndConditions(self):
        return self.get(inspect.stack()[0][3])
