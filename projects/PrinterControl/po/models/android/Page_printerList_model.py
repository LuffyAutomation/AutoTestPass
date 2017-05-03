import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Printer list.'''
class Page_printerList_model(AndroidCommonPage):
    page_name = 'page_printerList'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_search(self):
        return self.get(inspect.stack()[0][3])

    def Edit_search(self):
        return self.get(inspect.stack()[0][3])

    def text_printerIp(self):
        return self.get(inspect.stack()[0][3])
