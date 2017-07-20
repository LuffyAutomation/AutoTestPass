import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''facebook'''
class Page_facebook_model(AndroidCommonPage):
    page_name = 'page_facebook'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def text_EmailOrPhone(self):
        return self.get(inspect.stack()[0][3])
