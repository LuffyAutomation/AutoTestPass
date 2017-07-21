import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch 'button_photo' on page_home'''
class Page_photos_model(IosCommonPage):
    page_name = 'page_photos'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_myPhotos(self):
        return self.get(inspect.stack()[0][3])

    def text_addAccount(self):
        return self.get(inspect.stack()[0][3])
