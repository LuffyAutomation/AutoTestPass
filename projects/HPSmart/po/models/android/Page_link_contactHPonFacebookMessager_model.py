import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''contact HP on facebook messager page.'''
class Page_link_contactHPonFacebookMessager_model(AndroidCommonPage):
    page_name = 'page_link_contactHPonFacebookMessager'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_OpenInMessenger (self):
        return self.get(inspect.stack()[0][3])

    def button_GetTheMessengerApp (self):
        return self.get(inspect.stack()[0][3])
