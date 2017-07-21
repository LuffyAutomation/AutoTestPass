import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''This screen is add account from files page'''
class Page_addAccount_pageFiles_model(IosCommonPage):
    page_name = 'page_addAccount_pageFiles'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_box(self):
        return self.get(inspect.stack()[0][3])

    def text_dropbox(self):
        return self.get(inspect.stack()[0][3])

    def text_evernote(self):
        return self.get(inspect.stack()[0][3])

    def text_GoogleDrive(self):
        return self.get(inspect.stack()[0][3])

    def text_Other(self):
        return self.get(inspect.stack()[0][3])
