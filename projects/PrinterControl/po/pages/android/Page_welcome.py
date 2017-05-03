import inspect
from projects.PrinterControl.po.models.android.Page_welcome_model import Page_welcome_model


'''Welcome page'''
class Page_welcome(Page_welcome_model):
    def __init__(self, UI):
        self.UI = UI
        Page_welcome_model.__init__(self)

    def flow_welcome(self):
        self.button_start().waitForShown().click()

    def flow_welcome_setupLater(self):
        self.link_setupLater().waitForShown().click()