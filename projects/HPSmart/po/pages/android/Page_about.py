# coding: utf-8
from projects.HPSmart.po.models.android.Page_about_model import Page_about_model


'''about page.'''
class Page_about(Page_about_model):
    def __init__(self, UI):
        self.UI = UI
        if 1 > 1:
            from fwk.object.AndroidFwk import AndroidFwk
            self.UI = AndroidFwk(None)
        Page_about_model.__init__(self)

    def verify_Icon_Version_APPName(self):
        self.image_appIcon().verifyIsShown()
        self.text_versionLable().verifyEqual(self.text_versionLable().getValue(), "Version:")
        #self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")
        self.text_appName().verifyEqual(self.text_appName().getValue(), "HP Smart")

    def verify_CopyRight(self):
        self.text_copyRightCompany().verifyEqual(self.text_copyRightCompany().getValue(), "Copyright © 2012–2017 \nHP Inc.")
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
