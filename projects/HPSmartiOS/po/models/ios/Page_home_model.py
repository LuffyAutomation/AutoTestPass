import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''home page'''
class Page_home_model(IosCommonPage):
    page_name = 'page_home'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_home(self):
        return self.get(inspect.stack()[0][3])

    def button_file(self):
        return self.get(inspect.stack()[0][3])

    def button_scanner(self):
        return self.get(inspect.stack()[0][3])

    def button_photo(self):
        return self.get(inspect.stack()[0][3])

    def button_settings(self):
        return self.get(inspect.stack()[0][3])

    def button_add_printer(self):
        return self.get(inspect.stack()[0][3])

    def button_notifications(self):
        return self.get(inspect.stack()[0][3])

    def image_printer(self):
        return self.get(inspect.stack()[0][3])

    def image_Cartridge(self):
        return self.get(inspect.stack()[0][3])

    def button_addPrinter_small(self):
        return self.get(inspect.stack()[0][3])

    def image_status(self):
        return self.get(inspect.stack()[0][3])

    def tile_PrintPhotos(self):
        return self.get(inspect.stack()[0][3])

    def tile_ScanToEmail(self):
        return self.get(inspect.stack()[0][3])

    def tile_PrintDocuments(self):
        return self.get(inspect.stack()[0][3])

    def tile_PrintFacebookPhotos(self):
        return self.get(inspect.stack()[0][3])

    def tile_HPHelpAndSupport(self):
        return self.get(inspect.stack()[0][3])

    def tile_PrinterSettings(self):
        return self.get(inspect.stack()[0][3])

    def tile_Personalize(self):
        return self.get(inspect.stack()[0][3])

    def tile_Scan(self):
        return self.get(inspect.stack()[0][3])
