import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Home.'''
class Page_home_model(IosCommonPage):
    page_name = 'page_home'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_moreOptions(self):
        return self.get(inspect.stack()[0][3])

    def tile_personalizeIcon_image(self):
        return self.get(inspect.stack()[0][3])

    def tile_scanToEmail_image(self):
        return self.get(inspect.stack()[0][3])

    def tile_scanToEmail_title(self):
        return self.get(inspect.stack()[0][3])

    def tile_personalizeIcon_title(self):
        return self.get(inspect.stack()[0][3])
