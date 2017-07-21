import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch personalize button on home screen'''
class Page_personalize_model(IosCommonPage):
    page_name = 'page_personalize'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def button_done(self):
        return self.get(inspect.stack()[0][3])

    def text_printPhotos(self):
        return self.get(inspect.stack()[0][3])

    def text_scanToEmail(self):
        return self.get(inspect.stack()[0][3])

    def text_printFacebookPhotos(self):
        return self.get(inspect.stack()[0][3])

    def text_printDocuments(self):
        return self.get(inspect.stack()[0][3])

    def text_printerSettings(self):
        return self.get(inspect.stack()[0][3])

    def text_hpHelpandSupport(self):
        return self.get(inspect.stack()[0][3])

    def text_scan(self):
        return self.get(inspect.stack()[0][3])

    def text_printfromGoogleDrive(self):
        return self.get(inspect.stack()[0][3])

    def text_printfromDropbox(self):
        return self.get(inspect.stack()[0][3])

    def text_scanTocloud(self):
        return self.get(inspect.stack()[0][3])

    def printPhotos_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def scanToEmail_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def printFacebookPhotos_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def printDocuments_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def printerSettings_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def hpHelpandSupport_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def scan_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def printfromGoogleDrive_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def printfromDropbox_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def scanTocloud_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_printPhotos(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_scanToEmail(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_printFacebookPhotos(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_printDocuments(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_printerSettings(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_hpHelpandSupport(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_scan(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_printfromGoogleDrive(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_printfromDropbox(self):
        return self.get(inspect.stack()[0][3])

    def reorderbutton_scanTocloud(self):
        return self.get(inspect.stack()[0][3])
