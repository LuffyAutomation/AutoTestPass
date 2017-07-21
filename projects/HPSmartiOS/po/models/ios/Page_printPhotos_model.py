import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_printPhotos_model(IosCommonPage):
    page_name = 'page_printPhotos'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_print(self):
        return self.get(inspect.stack()[0][3])

    def button_changSettings(self):
        return self.get(inspect.stack()[0][3])

    def button_back(self):
        return self.get(inspect.stack()[0][3])

    def button_share(self):
        return self.get(inspect.stack()[0][3])
