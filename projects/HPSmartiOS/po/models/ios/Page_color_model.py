import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch color go to there'''
class Page_color_model(IosCommonPage):
    page_name = 'page_color'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_color(self):
        return self.get(inspect.stack()[0][3])

    def text_grayscale(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])
