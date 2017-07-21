import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Allow/ok button'''
class Dialog_legalInformation_model(IosCommonPage):
    page_name = 'dialog_legalInformation'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def dialog_all(self):
        return self.get(inspect.stack()[0][3])

    def dialog_ok(self):
        return self.get(inspect.stack()[0][3])
