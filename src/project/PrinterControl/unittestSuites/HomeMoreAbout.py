# coding: utf-8
import unittest
import traceback
from src.project.PrinterControl.AndroidPortal import AndroidPortal
from src.project.PrinterControl.po.wrapper.Pages import Pages


class HomeMoreAbout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.Portal = AndroidPortal()
            cls.Pages = Pages(cls.Portal)
            cls.Portal.openApp()
            cls.Result = cls.Portal.Result(cls.Portal)
            cls.Result.setTestName(cls.__name__)
            cls.Result.beforeClass(cls)
        except Exception as e:
            traceback.print_exc()
            cls.Portal.logger.error(e.__str__())
            cls.Portal.quit()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.Result.afterClass(cls)
        except Exception as e:
            #traceback.print_exc()
            cls.Portal.logger.error(e.__str__())

    def setUp(self):
        self.Result.beforeEachFunction(self)

    def tearDown(self):
        self.Result.afterEachFunction(self)

    # 1. All of above is almost general and can be just copy & paste to your test file. only package path and cls.Portal = AndroidPortal()
    # need to be modified according to your test.
    # 2. self.Result.setDescription and self.Result.setExpectedResult can be ignored.

    # def test_exmaple(self):
    #     self.Result.setDescription("1. xxxxx.",
    #                                "2. xxxxx.")
    #     self.Result.setExpectedResult("xxxxxx is displayed.")
    #     self.Result.setScreenshot("begin", "This is a begin.")
    #     self.Result.setComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue())
    #     self.Pages.xxxxxxxxx


    def test_flow(self):
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
        self.Portal.back()
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
        self.Portal.back()
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
        if "5." in self.Portal.RunTimeConf.platformVersion:
            self.Pages.Page_shareThisApp.text_qq().verifyIsShown()
        elif "6." in self.Portal.RunTimeConf.platformVersion:
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
        self.Portal.back()
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


