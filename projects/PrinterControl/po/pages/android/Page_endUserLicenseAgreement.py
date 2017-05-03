# coding: utf-8
from projects.PrinterControl.po.models.android.Page_endUserLicenseAgreement_model import Page_endUserLicenseAgreement_model


'''page_endUserLicenseAgreement'''
class Page_endUserLicenseAgreement(Page_endUserLicenseAgreement_model):
    def __init__(self, UI):
        self.UI = UI
        Page_endUserLicenseAgreement_model.__init__(self)

    def flow_agreements(self):
        self.UI.verifyIsShown("link_endUserLicenseAgreement")
        self.UI.clickOn("link_endUserLicenseAgreement", 3)
        if self.UI.isPresent("text_chrome"):
            self.UI.clickOn("text_chrome", 2)
            if self.UI.isPresent("text_always"):
                self.UI.clickOn("text_always", 1)
        self.UI.verifyIsShown("text_404PageNotFound")
        self.UI.verifyIsShown("image_logo")
        #  HP® Official Site | Laptops, Computers, Desktops , Printers, and more HP® Official Site | Laptops, Computers, Desktops , Printers, and more
        #' HP® Official Site | Laptops, Computers, Desktops , Printers, and more HP® Official Site | Laptops, Computers, Desktops , Printers, and more'
        self.UI.back()
        self.UI.setPage("page_about")
        self.UI.verifyIsShown("text_title_About")