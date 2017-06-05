# coding: utf-8
from projects.IosExample.po.models.android.Page_first_model import Page_first_model


'''Describe your page here.'''
class Page_first(Page_first_model):
    def __init__(self, UI):
        self.UI = UI
        if 1 > 1:
            from fwk.object.AndroidFwk import AndroidFwk
            self.UI = AndroidFwk
        Page_first_model.__init__(self)

    # This is function template of how to write your Business Logic.
    def example(self):
            pass
        # self.checkbox_accept().waitForShown().click()
        # self.Pages.Page_endUserLicenseAgreement.text_always().clickIfPresent().wait(1)
        # self.button_continue().click()
        # self.button_search().waitForShown(60).click().wait(1)
        # self.Edit_search().setValue("10.10.63.128")
        # self.text_printerIp().relocateByText("10.10.63.128").click()
        # self.image_appIcon().verifyIsShown()
        # A few elements' properties may be changed after a while. It should be searched again by using clearForRefinding()
        # self.image_appIcon().waitForShown().clearForRefinding().click()
        # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")
