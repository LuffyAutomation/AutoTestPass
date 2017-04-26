import inspect

from project.PrinterControl.po.CommonPage import CommonPage

'''page_shareThisApp'''
class Page_shareThisApp_model(CommonPage):
    page_name = 'page_shareThisApp'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def text_chooseAMailProvider(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_microsoftExchangeActiveSync(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_sina(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_qq(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_163(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_other(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
