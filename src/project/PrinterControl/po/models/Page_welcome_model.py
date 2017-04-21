import inspect
from src.project.PrinterControl.po.CommonPage import CommonPage


'''Welcome page'''
class Page_welcome_model(CommonPage):
    page_name = 'page_welcome'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def button_start(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def link_setupLater(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])