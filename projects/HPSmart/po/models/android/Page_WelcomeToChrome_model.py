import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Welcome to Chrome page.'''
class Page_WelcomeToChrome_model(AndroidCommonPage):
    page_name = 'page_WelcomeToChrome'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_AcceptOrContinue(self):
        return self.get(inspect.stack()[0][3])

    def button_NoThanks(self):
        return self.get(inspect.stack()[0][3])

    def button_Continue(self):
        return self.get(inspect.stack()[0][3])
