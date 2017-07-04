import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Personalize page.'''
class Page_Personalize_model(AndroidCommonPage):
    page_name = 'page_Personalize'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def buttonOrder_1(self):
        return self.get(inspect.stack()[0][3])

    def buttonOrder_2(self):
        return self.get(inspect.stack()[0][3])

    def text_CameraScanToEmail(self):
        return self.get(inspect.stack()[0][3])

    def text_PrintPhotos(self):
        return self.get(inspect.stack()[0][3])
