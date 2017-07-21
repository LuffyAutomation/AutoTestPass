import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch quality go to here'''
class Page_quality_model(IosCommonPage):
    page_name = 'page_quality'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_draft(self):
        return self.get(inspect.stack()[0][3])

    def text_normal(self):
        return self.get(inspect.stack()[0][3])

    def text_best(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])
