import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch inputType go to there'''
class Page_inputTpye_model(IosCommonPage):
    page_name = 'page_inputTpye'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_JPG(self):
        return self.get(inspect.stack()[0][3])

    def text_PDF(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])
