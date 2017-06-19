import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''contact HP on facebook messager page.'''
class Popup_contactHPonFacebookMessager_model(AndroidCommonPage):
    page_name = 'popup_contactHPonFacebookMessager'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_Message(self):
        return self.get(inspect.stack()[0][3])
