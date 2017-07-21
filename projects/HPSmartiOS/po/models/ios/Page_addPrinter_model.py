import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_addPrinter_model(IosCommonPage):
    page_name = 'page_addPrinter'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_agreements(self):
        return self.get(inspect.stack()[0][3])

    def button_addaNewPrinter(self):
        return self.get(inspect.stack()[0][3])

    def button_connectPrinterIPaddress(self):
        return self.get(inspect.stack()[0][3])

    def button_moreDtails(self):
        return self.get(inspect.stack()[0][3])

    def area_improvementProgram(self):
        return self.get(inspect.stack()[0][3])

    def text_improvementProgram(self):
        return self.get(inspect.stack()[0][3])

    def checkbox_improvementProgram(self):
        return self.get(inspect.stack()[0][3])

    def text_suppliesShopping(self):
        return self.get(inspect.stack()[0][3])

    def checkbox_suppliesShopping(self):
        return self.get(inspect.stack()[0][3])

    def text_specialOffers(self):
        return self.get(inspect.stack()[0][3])

    def checkbox_specialOffers(self):
        return self.get(inspect.stack()[0][3])

    def link_hpOnlinePrivacyStatement(self):
        return self.get(inspect.stack()[0][3])

    def checkbox_agreement(self):
        return self.get(inspect.stack()[0][3])

    def button_Continue(self):
        return self.get(inspect.stack()[0][3])
