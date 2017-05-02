# coding: utf-8
import unittest

from src.base.testFwk.CommonUnittest import CommonUnittest
from project.PrinterControl.po.wrapper.Pages_Android import Pages_Android
from project.PrinterControl.po.wrapper.Pages_Ios import Pages_Ios
from project.PrinterControl.po.wrapper.Pages_Web import Pages_Web

class HomeMoreAbout(CommonUnittest):
    # 1. self.Result.setDescription and self.Result.setExpectedResult can be ignored.
    # 2. Do not write setUpClass, tearDownClass, setUp and tearDown
    # def test_exmaple(self):
    #     self.Result.setDescription("1. xxxxx.",
    #                                "2. xxxxx.")
    #     self.Result.setExpectedResult("xxxxxx is displayed.")
    #     self.Result.setScreenshot("begin", "This is a begin.")
    #     self.Result.setComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue())
    #     self.Pages.xxxxxxxxx

    def test_flow(self):
        self.Pages_Android = Pages_Android(self.UI_Android)
        self.Pages = self.Pages_Android
        #self.Pages_Ios = Pages_Android(self.UI_Ios)
        #self.Pages_Web = Pages_Android(self.UI_Web)
        self.Result.setDescription("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.setExpectedResult("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()

    # @unittest.skip("temporarilly")
    def test_aioVersion(self):
        self.Result.setDescription("1. Tap on the top right drop down menu.",
                                   "2. Tap on the item About.")
        self.Result.setExpectedResult("1. AiO application version text and version number is display correctly.(Check the number on log or screenshot)",
                                      "2. AiO application name is displayed correctly.",
                                      "3. AiO application icon is displayed correctly.")
        self.Pages.Page_home.flow_open_menuItemAbout()
        self.Pages.Page_about.verify_Icon_Version_APPName()
        self.Result.setComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue())

    def test_copyRight(self):
        self.Result.setDescription("Fllow the last step.")
        self.Result.setExpectedResult("1. AiO application copy right text is display correctly",
                                      "2. AiO application copy right start year is displayed correctly",
                                      "3. AiO application copy right end year is displayed correctly")
        self.Pages.Page_about.verify_CopyRight()

    def test_legalInformaion(self):
        self.Result.setDescription("Fllow the last step.",
                                   "1. Tap on the Legal Information link.",
                                   "2. Tap on the OK button.")
        self.Result.setExpectedResult("1. Legal information popup is opened.",
                                      "2. Popup tile is Legal information.",
                                      "3. Popup content matches the latest wireframe (Only verify this exists.)")
        self.Pages.Page_about.link_legalInformation().click()
        self.Pages.Dialog_legalInformation.verify_TitleLegalInformation()
        self.Pages.Dialog_legalInformation.button_ok().click()
        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_endUserLicenseAgreement(self):
        self.Result.setDescription("Fllow the last step.",
                                   "1. Tap on the License agreement link.")
        self.Result.setExpectedResult("1. License agreement web page is opened.",
                                      "2. HP logo is displayed.",
                                      "3. HP license content is correct.(Ignore this step, since there is no correct result now.)")
        self.Pages.Page_about.link_endUserLicenseAgreement().verifyIsShown().click().wait(3)
        self.Pages.Sys_general.text_chrome().clickIfPresent().wait(2)
        self.Pages.Sys_general.text_always().clickIfPresent().wait(1)
        #self.Pages.Page_endUserLicenseAgreement.text_404PageNotFound().verifyIsShown(120)
        self.Pages.Page_endUserLicenseAgreement.image_logo().verifyIsShown(120)
        #' HP® Official Site | Laptops, Computers, Desktops , Printers, and more HP® Official Site | Laptops, Computers, Desktops , Printers, and more'


    def test_endUserLicenseAgreement_back(self):
        self.Result.setStepContinueFromFailIfBlock()
        self.Result.setDescription("Follow the last step. Tap on the Back key.")
        self.Result.setExpectedResult("Back to About screen displayed.")
        self.UI.back()
        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_hpOnlinePrivacyStatement(self):
        self.Result.setDescription("Follow the last step. Tap on the HP Online Privacy link.")
        self.Result.setExpectedResult("1. HP Online Privacy web page is opened.",
                                      "2. HP logo is displayed.",
                                      "3. HP Privacy statement is displayed correctly.")
        self.Pages.Page_about.link_hpOnlinePrivacyStatement().verifyIsShown().click().wait(3)
        self.Pages.Sys_general.text_chrome().clickIfPresent().wait(2)
        self.Pages.Sys_general.text_always().clickIfPresent().wait(1)
        self.Pages.Page_hpOnlinePrivacyStatement.text_hpPrivacyStatementWorldwide().verifyIsShown(90)
        self.Pages.Page_hpOnlinePrivacyStatement.image_logo().verifyIsShown()

    def test_hpOnlinePrivacyStatement_back(self):
        self.Result.setStepContinueFromFailIfBlock()
        self.Result.setDescription("Follow the last step. Tap on the OK button.")
        self.Result.setExpectedResult("Back to About screen displayed.")
        self.UI.back()

        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_shareThisApp(self):
        # self.Result.setDescription("Fllow the last step.",
        #                            "1. Tap on the Share this app button.",
        #                            "2. Tap on the Back key.")
        # self.Result.setExpectedResult("1. Share with popup is opened.",
        #                               "2. 163 is displayed.",
        #                               "3. Choose a mail provider is displayed.",
        #                               "4. Microsoft exchange active sync is displayed.",
        #                               "5. Other is displayed.",
        #                               "6. QQ is displayed.",
        #                               "7. Sina is displayed.",
        #                               "8. Back to About screen displayed after tapping the Back key.")
        self.Result.setDescription("Follow the last step. Tap on the Share this app button.")
        self.Result.setExpectedResult("1. Share with popup is opened.",
                                      "2. Email is displayed under Android 6, QQ is displayed under Android 5.",
                                      "3. Back to About screen displayed after tapping the Back key.")
        self.Pages.Page_about.button_shareThisApp().verifyIsShown().click().wait(1)
        if "5." in self.UI.RunTimeConf.platformVersion:
            self.Pages.Page_shareThisApp.text_qq().verifyIsShown()
        elif "6." in self.UI.RunTimeConf.platformVersion:
            self.Pages.Sys_general.text_email().verifyIsShown()
        # self.Pages.Page_shareThisApp.text_163().verifyIsShown()
        # self.Pages.Page_shareThisApp.text_chooseAMailProvider().verifyIsShown()
        # self.Pages.Page_shareThisApp.text_microsoftExchangeActiveSync().verifyIsShown()
        # self.Pages.Page_shareThisApp.text_other().verifyIsShown()
        # self.Pages.Page_shareThisApp.text_qq().verifyIsShown()
        # self.Pages.Page_shareThisApp.text_sina().verifyIsShown()

    def test_shareThisApp_back(self):
        self.Result.setStepContinueFromFailIfBlock()
        self.Result.setDescription("Follow the last step.")
        self.Result.setExpectedResult("Back to About screen displayed after tapping the Back key.")
        self.UI.back()
        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_headerDisplay(self):
        self.Result.setDescription("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.setExpectedResult("Screen goes back to AiO Home.")
        self.Pages.Page_about.button_back().click()
        self.Pages.Page_home.button_MoreOptions().verifyIsShown()

    def test_test(self):
        self.Result.setDescription("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.setExpectedResult("Screen goes back to AiO Home.")
        pass

