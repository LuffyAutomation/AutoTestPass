import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''about page.'''
class Page_about_model(AndroidCommonPage):
    page_name = 'page_about'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def text_versionLable(self):
        return self.get(inspect.stack()[0][3])

    def text_title_about(self):
        return self.get(inspect.stack()[0][3])

    def text_version(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])

    def text_appName(self):
        return self.get(inspect.stack()[0][3])

    def image_appIcon(self):
        return self.get(inspect.stack()[0][3])

    def text_copyRightCompany(self):
        return self.get(inspect.stack()[0][3])

    def link_hpOnlinePrivacyStatement(self):
        return self.get(inspect.stack()[0][3])

    def link_endUserLicenseAgreement(self):
        return self.get(inspect.stack()[0][3])

    def link_legalInformation(self):
        return self.get(inspect.stack()[0][3])

    def button_shareThisApp(self):
        return self.get(inspect.stack()[0][3])
