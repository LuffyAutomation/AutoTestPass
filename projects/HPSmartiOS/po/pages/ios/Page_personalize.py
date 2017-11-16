# coding: utf-8
from projects.HPSmartiOS.po.models.ios.Page_personalize_model import Page_personalize_model
from fwk.base.UiBaseWebDriverFwk import UiBaseWebDriverFwk
import time


from fwk.other.Result import  Result

'''Touch personalize button on home screen'''
class Page_personalize(Page_personalize_model):
    def __init__(self, UI):
        self.result = Result
        self.UI = UI
        if 1 > 1:
            from fwk.object.IosFwk import IosFwk
            self.UI = IosFwk(None)
        Page_personalize_model.__init__(self)


    def verifyTlesOptions(self):
        self.text_printPhotos().verifyIsShown()
        self.text_scanToEmail().verifyIsShown()
        self.text_printFacebookPhotos().verifyIsShown()
        self.text_printDocuments().verifyIsShown()
        self.text_printerSettings().verifyIsShown()
        self.text_hpHelpandSupport().verifyIsShown()
        self.text_scan().verifyIsShown()
        self.text_printfromGoogleDrive().verifyIsShown()
        self.text_printfromDropbox().verifyIsShown()
        self.text_scanTocloud().verifyIsShown()


    def turnoffONswitchButton(self):
        print "Turn off scan function on personalize scsreen."
        self.scan_switchButton().click()
        self.result.add_screenshot(name="turn off scan switch button")
        time.sleep(2)
        self.scan_switchButton().click()
        self.result.add_screenshot(name="turn on scan switch button")
        print "Turn on scan function on personalize scsreen."
        time.sleep(2)

    def linesBarUporDown(self):
        print "three lines bar to move the tiles up or down."

    def closeSometiles(self):
        self.printerSettings_switchButton().click()
        self.hpHelpandSupport_switchButton().click()
        self.scan_switchButton().click()
        self.result.add_screenshot(name="turn off all switch button")

    def moveThreeTilesUpOrDown(self):
        self.reorderbutton_scan().swipeUpFromMid()

    # This is function template of how to write your Business Logic.
    def example(self):
        pass
        # self.checkbox_accept().waitForShown().click()
        # self.Pages.Page_endUserLicenseAgreement.text_always().clickIfPresent().wait(1)
        # self.button_continue().click()
        # self.button_search().waitForShown(60).click().wait(1)
        # self.Edit_search().setValueBySendKeys("10.10.63.128")
        
        # if VALUE_PLACEHOLDER was defined in uimap.xml like:
        # <element name="text_printerIp" page="page_home"><xpath>//android.widget.TextView[contains(@text,'VALUE_PLACEHOLDER')]</xpath></element>
        # you can find the element by  xxx.replacePlaceholder("10").click
        # self.text_printerIp().replacePlaceholder("10.10.63.128").click()
        
        # self.image_appIcon().verifyIsShown()
        # A few elements' properties may be changed after a while. It should be searched again by using refreshMe()
        # self.image_appIcon().waitForShown().refreshMe().click()
        # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
