import inspect
from projects.PrinterControl.po.models.android.Page_agreements_model import Page_agreements_model


'''Default first page.'''
class Page_agreements(Page_agreements_model):
    def __init__(self, UI):
        self.UI = UI
        Page_agreements_model.__init__(self)

    def flow_agreements(self):
        # self.UI.wait(30)
        self.checkbox_accept().waitForShown().wait(3).click()
        self.button_continue().click()
