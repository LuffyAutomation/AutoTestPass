import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_myPhotoStream_model(IosCommonPage):
    page_name = 'page_myPhotoStream'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def picture_1(self):
        return self.get(inspect.stack()[0][3])
