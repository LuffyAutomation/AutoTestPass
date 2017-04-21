import inspect
from src.project.PrinterControl.po.CommonPage import CommonPage


'''page_hpOnlinePrivacyStatement'''
class Page_hpOnlinePrivacyStatement_model(CommonPage):
    page_name = 'page_hpOnlinePrivacyStatement'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def text_hpPrivacyStatementWorldwide(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def image_logo(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
