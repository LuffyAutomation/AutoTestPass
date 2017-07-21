from projects.HPSmart.po.pages.android.Page_link_PrintQualityTools import Page_link_PrintQualityTools
from projects.HPSmart.po.pages.android.Page_printer import Page_printer
from projects.HPSmart.po.pages.android.Page_HelpSearchForANetworkPrinter import Page_HelpSearchForANetworkPrinter
from projects.HPSmart.po.pages.android.Page_HelpSetUpANewPrinter import Page_HelpSetUpANewPrinter
from projects.HPSmart.po.pages.android.Page_ConnectionIssues import Page_ConnectionIssues
from projects.HPSmart.po.pages.android.Page_helpCenter import Page_helpCenter
from projects.HPSmart.po.pages.android.Page_MyFile import Page_MyFile
from projects.HPSmart.po.pages.android.Page_file import Page_file
from projects.HPSmart.po.pages.android.Page_link_contactHPonFacebookMessager import Page_link_contactHPonFacebookMessager
from projects.HPSmart.po.pages.android.Page_contactHPonFacebookMessager import Page_contactHPonFacebookMessager
from projects.HPSmart.po.pages.android.Page_link_OnlineSupport import Page_link_OnlineSupport
from projects.HPSmart.po.pages.android.Page_HowToPrint import Page_HowToPrint
from projects.HPSmart.po.pages.android.Page_GetHPHelpAndSupport import Page_GetHPHelpAndSupport
from projects.HPSmart.po.pages.android.Sys_general import Sys_general
from projects.HPSmart.po.pages.android.Page_shareThisApp import Page_shareThisApp
from projects.HPSmart.po.pages.android.Page_hpOnlinePrivacyStatement import Page_hpOnlinePrivacyStatement
from projects.HPSmart.po.pages.android.Page_endUserLicenseAgreement import Page_endUserLicenseAgreement
from projects.HPSmart.po.pages.android.Dialog_legalInformation import Dialog_legalInformation
from projects.HPSmart.po.pages.android.Page_appSettings import Page_appSettings
from projects.HPSmart.po.pages.android.Page_about import Page_about
from projects.HPSmart.po.pages.android.Page_home import Page_home
from projects.HPSmart.po.pages.android.Page_printerList import Page_printerList
from projects.HPSmart.po.pages.android.Page_setup import Page_setup
from projects.HPSmart.po.pages.android.Page_foundYourPrinter import Page_foundYourPrinter
from projects.HPSmart.po.pages.android.Sys_packageinstaller import Sys_packageinstaller
from projects.HPSmart.po.pages.android.Page_foundANetworkPrinter import Page_foundANetworkPrinter
from projects.HPSmart.po.pages.android.Page_findNewPrinter import Page_findNewPrinter
from projects.HPSmart.po.pages.android.Page_welcome import Page_welcome
from projects.HPSmart.po.pages.android.Page_agreements import Page_agreements


class Pages_Android:
    def __init__(self, UI):
        self._UI = UI
        self.Page_link_PrintQualityTools = Page_link_PrintQualityTools(self._UI)
        self.Page_printer = Page_printer(self._UI)
        self.Page_HelpSearchForANetworkPrinter = Page_HelpSearchForANetworkPrinter(self._UI)
        self.Page_HelpSetUpANewPrinter = Page_HelpSetUpANewPrinter(self._UI)
        self.Page_ConnectionIssues = Page_ConnectionIssues(self._UI)
        self.Page_helpCenter = Page_helpCenter(self._UI)
        self.Page_MyFile = Page_MyFile(self._UI)
        self.Page_file = Page_file(self._UI)
        self.Page_link_contactHPonFacebookMessager = Page_link_contactHPonFacebookMessager(self._UI)
        self.Page_contactHPonFacebookMessager = Page_contactHPonFacebookMessager(self._UI)
        self.Page_link_OnlineSupport = Page_link_OnlineSupport(self._UI)
        self.Page_HowToPrint = Page_HowToPrint(self._UI)
        self.Page_GetHPHelpAndSupport = Page_GetHPHelpAndSupport(self._UI)
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

    '''Custom public method'''
    def flow_goTo_PageHomeWithSpecifiedPrinter(self):
        self.Page_agreements.flow_agreements()
        self.Page_welcome.flow_welcome()
        self.Mpl.flow_foundYourPrinter_multiplePages()
        self.Page_printerList.flow_selectPrinter()

    '''Custom public method'''
    def flow_goTo_PageHomeWithoutPrinter(self):
        self.Page_welcome.button_start().waitForShown().click()
        self.Page_agreements.flow_agreements()
