import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''set up printer.'''
class Page_setup_model(AndroidCommonPage):
    page_name = 'page_setup'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_ExitSetup(self):
        return self.get(inspect.stack()[0][3])
