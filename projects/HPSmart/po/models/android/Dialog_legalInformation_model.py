import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''dialog_legalInformation'''
class Dialog_legalInformation_model(AndroidCommonPage):
    page_name = 'dialog_legalInformation'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def text_title_legalInformation(self):
        return self.get(inspect.stack()[0][3])

    def area_content_legalInformation(self):
        return self.get(inspect.stack()[0][3])

    def button_ok(self):
        return self.get(inspect.stack()[0][3])
