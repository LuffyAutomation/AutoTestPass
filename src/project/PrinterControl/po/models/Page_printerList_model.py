import inspect
from src.project.PrinterControl.po.CommonPage import CommonPage


'''Printer list.'''
class Page_printerList_model(CommonPage):
    page_name = 'page_printerList'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def button_search(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def Edit_search(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_printerIp(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
