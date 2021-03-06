import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch 'more_about' go to about screen'''
class Page_about_model(IosCommonPage):
    page_name = 'page_about'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def image_appIcon(self):
        return self.get(inspect.stack()[0][3])

    def text_appName(self):
        return self.get(inspect.stack()[0][3])

    def text_versionLable(self):
        return self.get(inspect.stack()[0][3])

    def text_copyRightCompany(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])

    def link_hpOnlinePrivacyStatement(self):
        return self.get(inspect.stack()[0][3])

    def link_endUserLicenseAgreement(self):
        return self.get(inspect.stack()[0][3])

    def link_legalInformation(self):
        return self.get(inspect.stack()[0][3])

    def rate_us(self):
        return self.get(inspect.stack()[0][3])
