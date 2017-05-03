import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Welcome page'''
class Page_welcome_model(AndroidCommonPage):
    page_name = 'page_welcome'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_start(self):
        return self.get(inspect.stack()[0][3])

    def link_setupLater(self):
        return self.get(inspect.stack()[0][3])
