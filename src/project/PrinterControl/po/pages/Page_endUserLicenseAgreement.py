# coding: utf-8
from src.project.PrinterControl.po.models.Page_endUserLicenseAgreement_model import Page_endUserLicenseAgreement_model


'''page_endUserLicenseAgreement'''
class Page_endUserLicenseAgreement(Page_endUserLicenseAgreement_model):
    def __init__(self, Portal):
        self.Portal = Portal
        Page_endUserLicenseAgreement_model.__init__(self)

    def flow_agreements(self):

        self.Portal.verifyIsShown("link_endUserLicenseAgreement")
        self.Portal.clickOn("link_endUserLicenseAgreement", 3)
        if self.Portal.isPresent("text_chrome"):
            self.Portal.clickOn("text_chrome", 2)
            if self.Portal.isPresent("text_always"):
                self.Portal.clickOn("text_always", 1)
        self.Portal.verifyIsShown("text_404PageNotFound")
        self.Portal.verifyIsShown("image_logo")
        #  HP® Official Site | Laptops, Computers, Desktops , Printers, and more HP® Official Site | Laptops, Computers, Desktops , Printers, and more
        #' HP® Official Site | Laptops, Computers, Desktops , Printers, and more HP® Official Site | Laptops, Computers, Desktops , Printers, and more'
        self.Portal.back()
        self.Portal.setPage("page_about")
        self.Portal.verifyIsShown("text_title_About")