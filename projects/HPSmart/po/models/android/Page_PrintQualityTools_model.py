import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Print Quality Tools page.'''
class Page_PrintQualityTools_model(AndroidCommonPage):
    page_name = 'page_PrintQualityTools'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def url_PrintQualityTools(self):
        return self.get(inspect.stack()[0][3])
