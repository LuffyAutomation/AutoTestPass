import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_myPhotos_model(IosCommonPage):
    page_name = 'page_myPhotos'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_myPhotoStream(self):
        return self.get(inspect.stack()[0][3])
