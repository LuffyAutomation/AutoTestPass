import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch button_file on 'page_home'''
class Page_files_model(IosCommonPage):
    page_name = 'page_files'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_myFiles(self):
        return self.get(inspect.stack()[0][3])

    def text_addAccount(self):
        return self.get(inspect.stack()[0][3])

    def text_GoogleDrive(self):
        return self.get(inspect.stack()[0][3])
