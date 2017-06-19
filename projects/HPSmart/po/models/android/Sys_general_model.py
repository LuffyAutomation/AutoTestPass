import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''for android 6.0 'Allow xxxx to access device's location'.'''
class Sys_general_model(AndroidCommonPage):
    page_name = 'sys_general'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def link_AllowAccessLocation(self):
        return self.get(inspect.stack()[0][3])

    def text_always(self):
        return self.get(inspect.stack()[0][3])

    def text_chrome(self):
        return self.get(inspect.stack()[0][3])

    def text_email(self):
        return self.get(inspect.stack()[0][3])
