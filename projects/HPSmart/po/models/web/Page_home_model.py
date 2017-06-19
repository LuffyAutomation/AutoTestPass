import inspect
from fwk.page.WebCommonPage import WebCommonPage


'''Default home page.'''
class Page_home_model(WebCommonPage):
    page_name = 'page_home'

    def __init__(self):
        self.__WebCommonPage = WebCommonPage.__init__(self)

    def edit_search(self):
        return self.get(inspect.stack()[0][3])

    def button_continue(self):
        return self.get(inspect.stack()[0][3])
