import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Default home page.'''
class Page_home_model(AndroidCommonPage):
    page_name = 'page_home'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def edit_search(self):
        return self.get(inspect.stack()[0][3])

    def button_continue(self):
        return self.get(inspect.stack()[0][3])
