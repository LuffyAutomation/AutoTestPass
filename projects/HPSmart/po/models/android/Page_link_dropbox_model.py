import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''dropbox page.'''
class Page_link_dropbox_model(AndroidCommonPage):
    page_name = 'page_link_dropbox'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def url_dropbox(self):
        return self.get(inspect.stack()[0][3])

    def button_signInGoogle(self):
        return self.get(inspect.stack()[0][3])

    def button_account(self):
        return self.get(inspect.stack()[0][3])

    def button_passWord(self):
        return self.get(inspect.stack()[0][3])

    def button_SignIn(self):
        return self.get(inspect.stack()[0][3])
