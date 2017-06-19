import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''dropbox page.'''
class Page_dropbox_model(AndroidCommonPage):
    page_name = 'page_dropbox'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_google_signup(self):
        return self.get(inspect.stack()[0][3])

    def button_tour_sign_up(self):
        return self.get(inspect.stack()[0][3])

    def button_one_account_email(self):
        return self.get(inspect.stack()[0][3])
