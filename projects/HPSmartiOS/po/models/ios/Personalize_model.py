import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch personalize button on home screen'''
class Personalize_model(IosCommonPage):
    page_name = 'personalize'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def printPhotos(self):
        return self.get(inspect.stack()[0][3])

    def scanToEmale(self):
        return self.get(inspect.stack()[0][3])

    def printFacebookPhotos(self):
        return self.get(inspect.stack()[0][3])

    def printDocuments(self):
        return self.get(inspect.stack()[0][3])

    def printerSettings(self):
        return self.get(inspect.stack()[0][3])

    def hpHelpandSupport(self):
        return self.get(inspect.stack()[0][3])

    def scan(self):
        return self.get(inspect.stack()[0][3])

    def printfromGoogleDrive(self):
        return self.get(inspect.stack()[0][3])

    def printfromDropbox(self):
        return self.get(inspect.stack()[0][3])

    def scanTocloud(self):
        return self.get(inspect.stack()[0][3])

    def scan_switchButton(self):
        return self.get(inspect.stack()[0][3])

    def printfromGoogleDrive_switchButton(self):
        return self.get(inspect.stack()[0][3])
