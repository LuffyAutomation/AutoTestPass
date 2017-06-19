import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''page_shareThisApp'''
class Page_shareThisApp_model(AndroidCommonPage):
    page_name = 'page_shareThisApp'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def text_chooseAMailProvider(self):
        return self.get(inspect.stack()[0][3])

    def text_microsoftExchangeActiveSync(self):
        return self.get(inspect.stack()[0][3])

    def text_sina(self):
        return self.get(inspect.stack()[0][3])

    def text_qq(self):
        return self.get(inspect.stack()[0][3])

    def text_163(self):
        return self.get(inspect.stack()[0][3])

    def text_other(self):
        return self.get(inspect.stack()[0][3])
