import inspect
from project.PrinterControl.po.CommonPage import CommonPage


'''dialog_legalInformation'''
class Dialog_legalInformation_model(CommonPage):
    page_name = 'dialog_legalInformation'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def text_title_legalInformation(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def area_content_legalInformation(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def button_ok(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
