import inspect
from src.project.PrinterControl.po.models.Page_agreements_model import Page_agreements_model


'''Default first page.'''
class Page_agreements(Page_agreements_model):
    def __init__(self, Portal):
        self.Portal = Portal
        Page_agreements_model.__init__(self)

    def flow_agreements(self):
        self.checkbox_accept().waitForShown().click()
        self.button_continue().click()
