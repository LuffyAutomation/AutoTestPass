import inspect
from project.PrinterControl.po.CommonPage import CommonPage


'''for android 6.0 'Allow xxxx to access device's location'.'''
class Sys_packageinstaller_model(CommonPage):
    page_name = 'sys_packageinstaller'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def link_AllowAccessLocation(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
