import inspect

from project.WebExample.po.CommonPage import CommonPage

'''Default home page.'''
class Page_home_model(CommonPage):
    page_name = 'page_home'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def edit_search(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def button_continue(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
