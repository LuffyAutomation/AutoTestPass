import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_GoogleDrive_model(IosCommonPage):
    page_name = 'page_GoogleDrive'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def document_1(self):
        return self.get(inspect.stack()[0][3])
