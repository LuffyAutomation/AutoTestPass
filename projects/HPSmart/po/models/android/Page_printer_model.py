import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''add_printer_link_gray page.'''
class Page_printer_model(AndroidCommonPage):
    page_name = 'page_printer'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def printers_1(self):
        return self.get(inspect.stack()[0][3])

    def printers_2(self):
        return self.get(inspect.stack()[0][3])

    def printers_3(self):
        return self.get(inspect.stack()[0][3])

    def button_image_back(self):
        return self.get(inspect.stack()[0][3])

    def button_addPrinter(self):
        return self.get(inspect.stack()[0][3])

    def button_LookingForWiFiDirectPrinters(self):
        return self.get(inspect.stack()[0][3])
