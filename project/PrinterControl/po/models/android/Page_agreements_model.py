import inspect
from src.base.fwk.CommonPage import CommonPage


'''Default first page.'''
class Page_agreements_model(CommonPage):
    page_name = 'page_agreements'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def checkbox_accept(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def button_continue(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
