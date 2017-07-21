import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch button_settings go to here'''
class Page_scanSettings_model(IosCommonPage):
    page_name = 'page_scanSettings'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_inputType(self):
        return self.get(inspect.stack()[0][3])

    def text_inputSourece(self):
        return self.get(inspect.stack()[0][3])

    def text_quality(self):
        return self.get(inspect.stack()[0][3])

    def text_color(self):
        return self.get(inspect.stack()[0][3])

    def button_done(self):
        return self.get(inspect.stack()[0][3])
