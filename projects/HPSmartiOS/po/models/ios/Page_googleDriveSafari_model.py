import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Google Drive safari'''
class Page_googleDriveSafari_model(IosCommonPage):
    page_name = 'page_googleDriveSafari'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_useAnotherAccount(self):
        return self.get(inspect.stack()[0][3])

    def text_inputEmail(self):
        return self.get(inspect.stack()[0][3])

    def button_next(self):
        return self.get(inspect.stack()[0][3])

    def text_enterPassword(self):
        return self.get(inspect.stack()[0][3])

    def button_allow(self):
        return self.get(inspect.stack()[0][3])
