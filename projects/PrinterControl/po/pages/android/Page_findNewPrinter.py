import inspect
from projects.PrinterControl.po.models.android.Page_findNewPrinter_model import Page_findNewPrinter_model


'''We find new printer.'''
class Page_findNewPrinter(Page_findNewPrinter_model):
    def __init__(self, UI):
        self.UI = UI
        Page_findNewPrinter_model.__init__(self)

    # This is function template of how to write your Business Logic.
    def flow_example(self):
        pass
        # self.checkbox_accept().waitForShown().click()
        # self.Pages.Page_endUserLicenseAgreement.text_always().clickIfPresent().wait(1)
        # self.button_continue().click()
        # self.button_search().waitForShown().click().wait(1)
        # self.Edit_search().setValue("10.10.63.128")
        # self.text_printerIp().relocateByText("10.10.63.128").click()
        # self.image_appIcon().verifyIsShown()
        # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")
