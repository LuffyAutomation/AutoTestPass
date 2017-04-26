import inspect

from project.PrinterControl.po.CommonPage import CommonPage

'''set up printer.'''
class Page_setup_model(CommonPage):
    page_name = 'page_setup'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def button_ExitSetup(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
