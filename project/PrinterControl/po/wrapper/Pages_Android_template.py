from project.PrinterControl.po.pages.android.Page_agreements import Page_agreements
from project.PrinterControl.po.pages.android.Page_welcome import Page_welcome
from project.PrinterControl.po.pages.android.Page_findNewPrinter import Page_findNewPrinter
from project.PrinterControl.po.pages.android.Page_foundANetworkPrinter import Page_foundANetworkPrinter
from project.PrinterControl.po.pages.android.Sys_packageinstaller import Sys_packageinstaller
from project.PrinterControl.po.pages.android.Page_foundYourPrinter import Page_foundYourPrinter
from project.PrinterControl.po.pages.android.Page_setup import Page_setup
from project.PrinterControl.po.pages.android.Page_printerList import Page_printerList
from project.PrinterControl.po.pages.android.Page_home import Page_home
from project.PrinterControl.po.pages.android.Page_about import Page_about
from project.PrinterControl.po.pages.android.Dialog_legalInformation import Dialog_legalInformation
from project.PrinterControl.po.pages.android.Page_endUserLicenseAgreement import Page_endUserLicenseAgreement
from project.PrinterControl.po.pages.android.Page_hpOnlinePrivacyStatement import Page_hpOnlinePrivacyStatement
from project.PrinterControl.po.pages.android.Page_shareThisApp import Page_shareThisApp
from project.PrinterControl.po.pages.android.Sys_general import Sys_general

class Pages_Android:
    def __init__(self, UI):
        self._UI = UI
        self._UI.getDriver()
        self.Page_agreements = Page_agreements(self._UI)
        self.Page_welcome = Page_welcome(self._UI)
        self.Page_findNewPrinter = Page_findNewPrinter(self._UI)
        self.Page_foundANetworkPrinter = Page_foundANetworkPrinter(self._UI)
        self.Sys_packageinstaller = Sys_packageinstaller(self._UI)
        self.Page_foundYourPrinter = Page_foundYourPrinter(self._UI)
        self.Page_setup = Page_setup(self._UI)
        self.Page_printerList = Page_printerList(self._UI)
        self.Page_home = Page_home(self._UI)
        self.Page_about = Page_about(self._UI)
        self.Dialog_legalInformation = Dialog_legalInformation(self._UI)
        self.Page_endUserLicenseAgreement = Page_endUserLicenseAgreement(self._UI)
        self.Page_hpOnlinePrivacyStatement = Page_hpOnlinePrivacyStatement(self._UI)
        self.Page_shareThisApp = Page_shareThisApp(self._UI)
        self.Sys_general = Sys_general(self._UI)
