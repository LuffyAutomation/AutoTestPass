# coding: utf-8
from projects.PrinterControl.po.models.android.Page_about_model import Page_about_model


'''about page.'''
class Page_about(Page_about_model):
    def __init__(self, UI):
        self.UI = UI
        Page_about_model.__init__(self)

    def verify_Icon_Version_APPName(self):
        self.image_appIcon().verifyIsShown()
        self.text_versionLable().verifyEqual(self.text_versionLable().getValue(), "Version:")
        #self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")
        self.text_appName().verifyEqual(self.text_appName().getValue(), "HP All-in-One Printer Remote")

    def verify_CopyRight(self):
        self.text_copyRightCompany().verifyEqual(self.text_copyRightCompany().getValue(), 'Copyright © 2012–2017 \nHP Inc.')