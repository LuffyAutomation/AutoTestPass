import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''file page.'''
class Page_file_model(AndroidCommonPage):
    page_name = 'page_file'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def title_MyFile(self):
        return self.get(inspect.stack()[0][3])
