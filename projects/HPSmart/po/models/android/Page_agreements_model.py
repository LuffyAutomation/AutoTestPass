import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Default first page.'''
class Page_agreements_model(AndroidCommonPage):
    page_name = 'page_agreements'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def checkbox_accept(self):
        return self.get(inspect.stack()[0][3])

    def button_continue(self):
        return self.get(inspect.stack()[0][3])
