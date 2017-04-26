import inspect

from project.PrinterControl.po.CommonPage import CommonPage

'''for android 6.0 'Allow xxxx to access device's location'.'''
class Sys_general_model(CommonPage):
    page_name = 'sys_general'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def link_AllowAccessLocation(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_always(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_chrome(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def text_email(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
