import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''add printer page.'''
class Page_HelpSetUpANewPrinter_model(AndroidCommonPage):
    page_name = 'page_HelpSetUpANewPrinter'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_image_back(self):
        return self.get(inspect.stack()[0][3])

    def button_MyPrinterIsNotListed(self):
        return self.get(inspect.stack()[0][3])
