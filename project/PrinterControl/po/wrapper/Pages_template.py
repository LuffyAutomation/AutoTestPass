from src.project.PrinterControl.po.pages.Dialog_legalInformation import Dialog_legalInformation
from src.project.PrinterControl.po.pages.Page_about import Page_about
from src.project.PrinterControl.po.pages.Page_agreements import Page_agreements
from src.project.PrinterControl.po.pages.Page_endUserLicenseAgreement import Page_endUserLicenseAgreement
from src.project.PrinterControl.po.pages.Page_findNewPrinter import Page_findNewPrinter
from src.project.PrinterControl.po.pages.Page_foundANetworkPrinter import Page_foundANetworkPrinter
from src.project.PrinterControl.po.pages.Page_foundYourPrinter import Page_foundYourPrinter
from src.project.PrinterControl.po.pages.Page_home import Page_home
from src.project.PrinterControl.po.pages.Page_printerList import Page_printerList
from src.project.PrinterControl.po.pages.Page_setup import Page_setup
from src.project.PrinterControl.po.pages.Page_shareThisApp import Page_shareThisApp
from src.project.PrinterControl.po.pages.Page_welcome import Page_welcome
from src.project.PrinterControl.po.pages.Sys_general import Sys_general
from src.project.PrinterControl.po.pages.Sys_packageinstaller import Sys_packageinstaller

from project.PrinterControl.po.pages.Page_hpOnlinePrivacyStatement import Page_hpOnlinePrivacyStatement


class Pages:
    def __init__(self, Portal):
        self._Portal = Portal
        self.Page_agreements = Page_agreements(self._Portal)
        self.Page_welcome = Page_welcome(self._Portal)
        self.Page_findNewPrinter = Page_findNewPrinter(self._Portal)
        self.Page_foundANetworkPrinter = Page_foundANetworkPrinter(self._Portal)
        self.Sys_packageinstaller = Sys_packageinstaller(self._Portal)
        self.Page_foundYourPrinter = Page_foundYourPrinter(self._Portal)
        self.Page_setup = Page_setup(self._Portal)
        self.Page_printerList = Page_printerList(self._Portal)
        self.Page_home = Page_home(self._Portal)
        self.Page_about = Page_about(self._Portal)
        self.Dialog_legalInformation = Dialog_legalInformation(self._Portal)
        self.Page_endUserLicenseAgreement = Page_endUserLicenseAgreement(self._Portal)
        self.Page_hpOnlinePrivacyStatement = Page_hpOnlinePrivacyStatement(self._Portal)
        self.Page_shareThisApp = Page_shareThisApp(self._Portal)
        self.Sys_general = Sys_general(self._Portal)
