import inspect
from projects.PrinterControl.po.models.android.Page_findNewPrinter_model import Page_findNewPrinter_model


'''We find new printer.'''
class Page_findNewPrinter(Page_findNewPrinter_model):
    def __init__(self, UI):
        self.UI = UI
        if 1 > 1:
            from fwk.object.AndroidFwk import AndroidFwk
            self.UI = AndroidFwk(None)
        Page_findNewPrinter_model.__init__(self)

    # This is function template of how to write your Business Logic.
    def flow_example(self):
        pass
        # self.checkbox_accept().waitForShown().click()
        # self.Pages.Page_endUserLicenseAgreement.text_always().clickIfPresent().wait(1)
        # self.button_continue().click()
        # self.button_search().waitForShown(60).click().wait(1)
        # self.Edit_search().setValue("10.10.63.128")

        # if VALUE_PLACEHOLDER was defined in uimap.xml like:
        # <element name="text_printerIp" page="page_home"><xpath>//android.widget.TextView[contains(@text,'VALUE_PLACEHOLDER')]</xpath></element>
        # you can find the element by  xxx.replacePlaceholder("10").click
        # self.text_printerIp().replacePlaceholder("10.10.63.128").click()

        # self.image_appIcon().verifyIsShown()
        # A few elements' properties may be changed after a while. It should be searched again by using clearForRefinding()
        # self.image_appIcon().waitForShown().refreshMe().clickrefreshMe
        # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
