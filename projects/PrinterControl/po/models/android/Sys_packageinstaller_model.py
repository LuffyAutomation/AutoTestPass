import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''for android 6.0 'Allow xxxx to access device's location'.'''
class Sys_packageinstaller_model(AndroidCommonPage):
    page_name = 'sys_packageinstaller'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def link_AllowAccessLocation(self):
        return self.get(inspect.stack()[0][3])
