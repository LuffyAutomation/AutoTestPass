import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch inputSource go to here'''
class Page_inputSource_model(IosCommonPage):
    page_name = 'page_inputSource'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_automatic(self):
        return self.get(inspect.stack()[0][3])

    def text_scannerGlass(self):
        return self.get(inspect.stack()[0][3])

    def text_documentFeeder(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])
