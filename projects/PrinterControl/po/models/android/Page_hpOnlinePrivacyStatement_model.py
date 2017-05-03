import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''page_hpOnlinePrivacyStatement'''
class Page_hpOnlinePrivacyStatement_model(AndroidCommonPage):
    page_name = 'page_hpOnlinePrivacyStatement'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def text_hpPrivacyStatementWorldwide(self):
        return self.get(inspect.stack()[0][3])

    def image_logo(self):
        return self.get(inspect.stack()[0][3])
