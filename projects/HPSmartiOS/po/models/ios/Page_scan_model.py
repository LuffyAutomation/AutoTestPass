import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_scan_model(IosCommonPage):
    page_name = 'page_scan'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_settings(self):
        return self.get(inspect.stack()[0][3])

    def text_scanner(self):
        return self.get(inspect.stack()[0][3])

    def text_camera(self):
        return self.get(inspect.stack()[0][3])

    def button_capture(self):
        return self.get(inspect.stack()[0][3])

    def button_picture(self):
        return self.get(inspect.stack()[0][3])

    def button_cancel(self):
        return self.get(inspect.stack()[0][3])

    def button_scanner(self):
        return self.get(inspect.stack()[0][3])

    def button_camera(self):
        return self.get(inspect.stack()[0][3])
