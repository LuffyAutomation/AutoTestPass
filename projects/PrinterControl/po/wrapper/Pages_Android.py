from projects.PrinterControl.po.pages.android.Sys_general import Sys_general
from projects.PrinterControl.po.pages.android.Page_shareThisApp import Page_shareThisApp
from projects.PrinterControl.po.pages.android.Page_hpOnlinePrivacyStatement import Page_hpOnlinePrivacyStatement
from projects.PrinterControl.po.pages.android.Page_endUserLicenseAgreement import Page_endUserLicenseAgreement
from projects.PrinterControl.po.pages.android.Dialog_legalInformation import Dialog_legalInformation
from projects.PrinterControl.po.pages.android.Page_appSettings import Page_appSettings
from projects.PrinterControl.po.pages.android.Page_about import Page_about
from projects.PrinterControl.po.pages.android.Page_home import Page_home
from projects.PrinterControl.po.pages.android.Page_printerList import Page_printerList
from projects.PrinterControl.po.pages.android.Page_setup import Page_setup
from projects.PrinterControl.po.pages.android.Page_foundYourPrinter import Page_foundYourPrinter
from projects.PrinterControl.po.pages.android.Sys_packageinstaller import Sys_packageinstaller
from projects.PrinterControl.po.pages.android.Page_foundANetworkPrinter import Page_foundANetworkPrinter
from projects.PrinterControl.po.pages.android.Page_findNewPrinter import Page_findNewPrinter
from projects.PrinterControl.po.pages.android.Page_welcome import Page_welcome
from projects.PrinterControl.po.pages.android.Page_agreements import Page_agreements


class Pages_Android:
    def __init__(self, UI):
        self._UI = UI
        self.Sys_general = Sys_general(self._UI)
        self.Page_shareThisApp = Page_shareThisApp(self._UI)
        self.Page_hpOnlinePrivacyStatement = Page_hpOnlinePrivacyStatement(self._UI)
        self.Page_endUserLicenseAgreement = Page_endUserLicenseAgreement(self._UI)
        self.Dialog_legalInformation = Dialog_legalInformation(self._UI)
        self.Page_appSettings = Page_appSettings(self._UI)
        self.Page_about = Page_about(self._UI)
        self.Page_home = Page_home(self._UI)
        self.Page_printerList = Page_printerList(self._UI)
        self.Page_setup = Page_setup(self._UI)
        self.Page_foundYourPrinter = Page_foundYourPrinter(self._UI)
        self.Sys_packageinstaller = Sys_packageinstaller(self._UI)
        self.Page_foundANetworkPrinter = Page_foundANetworkPrinter(self._UI)
        self.Page_findNewPrinter = Page_findNewPrinter(self._UI)
        self.Page_welcome = Page_welcome(self._UI)
        self.Page_agreements = Page_agreements(self._UI)
        
    def flow_goTo_PageHomeWithSpecifiedPrinter(self):
        self.Page_agreements.flow_agreements()
        self.Page_welcome.flow_welcome()
        self.Mpl.flow_foundYourPrinter_multiplePages()
        self.Page_printerList.flow_selectPrinter()

    def flow_goTo_PageHomeWithoutPrinter(self):
        self.Page_agreements.flow_agreements()
        self.Page_welcome.flow_welcome_setupLater()
