# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmart.po.wrapper.Pages_Android import Pages_Android

from projects.HPSmart.data.testData.TestData_Android import TestData_Android
class HomeMoreHelpCenter(CommonUnittest):
    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
        cls.Pages = cls.Pages_Android  # Just make it simple since generally only one of Android, Ios and Web may be tested.

    def test_flow(self):
        self.Result.set_description("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.set_expected_result("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()
        # self.Pages.Page_home.button_MoreOptions().waitForShown().click()
        # self.Pages.Page_home.Menu_moreOptions.menuItem_helpCenter_().waitForShown().click()
        # self.Pages.Page_helpCenter.option_OnlineSupport().waitForShown().click()
        # self.Pages.Page_link_OnlineSupport.title_selectCountryHeader().verifyIsShown(120)

    def test_HelpCenter(self):
        self.Result.set_description("Verify that the GA for Help Center from More Options menu is the same as Get HP Help and Support tile;",
                                   "at least for triggering such page;")
        self.Result.set_expected_result("'Help Center' GA is the same regardless where it was opened;",
                                      "but More Options trigger might have extra tracking;")
        self.Pages.Page_home.button_MoreOptions().click()
        self.Pages.Page_home.Menu_moreOptions.menuItem_helpCenter_().waitForShown().click()
        self.Pages.Page_helpCenter.option_HowToPrint_().verifyIsShown()
        self.Pages.Page_helpCenter.option_ConnectionIssues().verifyIsShown()
        self.Pages.Page_helpCenter.option_OnlineSupport().verifyIsShown()
        self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().verifyIsShown()
        self.UI_Android.back()
        self.UI_Android.swipeOfType(self.UI_Android.SwipeTo.UP)
        self.Pages.Page_home.tile_GetHPHelpAndSupport().waitForShown().click()
        self.Pages.Page_GetHPHelpAndSupport.option_HowToPrint_().verifyIsShown()
        self.Pages.Page_GetHPHelpAndSupport.option_ConnectionIssues().verifyIsShown()
        self.Pages.Page_GetHPHelpAndSupport.option_OnlineSupport().verifyIsShown()
        self.Pages.Page_GetHPHelpAndSupport.option_ContactHPonFacebookMessenger().verifyIsShown()
        self.UI_Android.back()

    def test_HowToPrint(self):
        self.Result.set_description("1. From Home page > More Options > Help Center, ",
                                   "2. click on the 'How to Print' option.",
                                   "3. Verify that the 'How to Print' page is launched and it should be the same as if launched via 'How to Print'tile;")
        self.Result.set_expected_result(
            "1. For this test case, just need to verify that the 'How to Print' page can be launched from Help Center."
            "2. The How to Print focused test plan will test that page more in-depth.")
        self.UI_Android.swipeOfType(self.UI_Android.SwipeTo.UP)
        self.Pages.Page_home.tile_HowToPrint().waitForShown().click()
        self.Pages.Page_HowToPrint.button_Cancel().waitForShown().click()
        self.Pages.Page_HowToPrint.title_HowToPrint_().waitForShown().click()
        self.Pages.Page_home.button_MoreOptions().click()
        self.Pages.Page_home.Menu_moreOptions.menuItem_helpCenter_().waitForShown().click()
        self.Pages.Page_helpCenter.option_HowToPrint_().waitForShown().click()
        self.Pages.Page_HowToPrint.button_Cancel().waitForShown().click()
        self.Pages.Page_HowToPrint.title_HowToPrint_().verifyIsShown()
        self.UI_Android.back()

    def test_OnlineSupport(self):
        self.Result.set_description("1. From Home page > More Options > Help Center, click on Online Support.",
                                   "2. Verify the following link is opened via external browser.",
                                   "3. http://support.hp.com/us-en/document/c03722645?openCLC=true")
        self.Result.set_expected_result(
            "1. The HP support page should open in an external browser",
            "2. and the overlay for choosing country/language should always show on top.")
        self.Pages.Page_helpCenter.option_OnlineSupport().waitForShown().click()
        self.Pages.Page_link_OnlineSupport.url_OnlineSupport().verifyIsShown().wait(20)
        self.UI_Android.swipeOfType(self.UI_Android.SwipeTo.DOWN)
        self.Pages.Page_link_OnlineSupport.title_selectCountryHeader().verifyIsShown()
        self.UI_Android.back()

    # def test_contactHPonFacebookMessager_step1_step2(self):
    #     self.Result.set_description("1. Mobile device is set to a country which is not supported by Facebook (e.g. China).",
    #                                "2. In Home page > More Options > Help Center, verify that there is no 'Contact HP on Facebook Messenger' option;",
    #                                "3. Mobile device is set to a country which is supported by Facebook",
    #                                "4. In Home page > More Options > Help Center, verify that 'Contact HP on Facebook Messenger' option is available.")
    #     self.Result.set_expected_result("1. If chosen country is not supported by Facebook, the option to 'Contact HP on Facebook Messenger' will not be shown;",
    #                                   "2. If chosen country is supported by Facebook, the option to 'Contact HP on Facebook Messenger' should be shown;")
    #     self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().verifyIsShown()
    #     #self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().verifyIsNotShown()

    def test_contactHPonFacebookMessager_step3(self):
        self.Result.set_description("1. Click on 'Contact HP on Facebook Messenger' option on Help Center page;",
                                   "2. Click on CANCEL;")
        self.Result.set_expected_result(
            "1. Verify that the 'Contact HP on Facebook Messenger' popup is shown;",
            "2. Verify the popup is dismissed and app returns to Help Center;")
        self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().click()
        self.Pages.Page_contactHPonFacebookMessager.button_Cancel().waitForShown().click()
        self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().verifyIsShown()

    # def test_contactHPonFacebookMessager_step4(self):
    #     self.Result.set_description("Trigger the 'Contact HP on Facebook Messenger' popup again;",
    #                                "Click on MESSAGE;")
    #     self.Result.set_expected_result(
    #          "Verify the Open-with android popup would show with options like Messenger or Chrome;",
    #          "In any condition, browser or Messenger, it should be able to eventually open up a chat with HP Support;")
    #     self.Pages.Page_home.button_MoreOptions().click()
    #     self.Pages.Page_home.Menu_moreOptions.menuItem_helpCenter_().waitForShown().click()
    #
    #     self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().click()
    #     self.Pages.Popup_contactHPonFacebookMessager.button_Message().waitForShown().click()
    #     self.Pages.Page_link_contactHPonFacebookMessager.button_OpenInMessenger().verifyIsShown()

    def test_contactHPonFacebookMessager_step5(self):
        self.Result.set_description("1. Click on 'Contact HP on Facebook Messenger' option on Help Center page;",
                                   "2. Check the 'Don't show me this again' checkbox;",
                                   "3. Click CANCEL;",
                                   "4. Click on 'Contact HP on Facebook Messenger' option again;")
        self.Result.set_expected_result(
             "1. Verify that the 'Contact HP on Facebook Messenger' popup no longer shows and app proceed straight to open-with dialog;",
             "2. With the  'Don't show me this again' option set, app will no longer show the  'Contact HP on Facebook Messenger' popup and proceed straight to open-with dialog;")
        self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().click()
        self.Pages.Page_contactHPonFacebookMessager.checkBox_dialog_do_not_show().waitForShown().click()
        self.Pages.Page_contactHPonFacebookMessager.button_Cancel().waitForShown().click()
        self.Pages.Page_helpCenter.option_ContactHPonFacebookMessenger().click()
        self.Pages.Page_contactHPonFacebookMessager.checkBox_dialog_do_not_show().verifyIsNotShown().wait(10)
        self.UI_Android.back()

    def test_connectionIssues_step1(self):
        self.Result.set_description("From Home page > More Options > Help Center, click on 'Connection Issues' option;")
        self.Result.set_expected_result(
            "Verify the 'My printer is not listed' popup is shown;",
            "The popup is the same one shown when no printer / WiFi Direct printer is found on printer list page;")
        self.Pages.Page_helpCenter.option_ConnectionIssues().waitForShown().click()
        self.Pages.Page_ConnectionIssues.title_MyPrinterIsNotListed().verifyIsShown()
        self.UI_Android.back()

    def test_connectionIssues_step2(self):
        self.Result.set_description("From Connection Issues, click on 'Help Set Up a New Printer';",
                                   "Use both back arrow and HW back button to go back;")
        self.Result.set_expected_result(
            "Verify app goes to Add Printer page of Printer List;",
            "App goes back to Help Center when any back button is pressed;")
        self.Pages.Page_helpCenter.option_ConnectionIssues().waitForShown().click()
        self.Pages.Page_ConnectionIssues.button_HelpSetUpANewPrinter().waitForShown().click()
        self.Pages.Page_HelpSetUpANewPrinter.button_image_back().waitForShown().click()
        self.Pages.Page_helpCenter.option_ConnectionIssues().verifyIsShown()

    def test_connectionIssues_step3(self):
        self.Result.set_description("From Connection Issues, click on ""Help Search for a Network Printer")
        self.Result.set_expected_result(
            "1. Verify the ""Help Search for a Network Printer"" page is shown;",
            "2. Verify all three ""How do I do this?"" link triggers tips popup;",
            #"and the OK button can dismiss the popup;",
            "3. Verify all three checkboxes works;",
            "4. Verify that Try Again button is disabled and ineffective until all three checkboxes are selected.")
        self.Pages.Page_helpCenter.option_ConnectionIssues().waitForShown().click()
        self.Pages.Page_ConnectionIssues.button_HelpSearchForANetworkPrinter().waitForShown().click()
        self.UI_Android.verifyDisable(self.Pages.Page_HelpSearchForANetworkPrinter.button_tryAgain().isEnabled())
        self.Pages.Page_HelpSearchForANetworkPrinter.checkBox_1().waitForShown().click()
        self.Pages.Page_HelpSearchForANetworkPrinter.checkBox_2().waitForShown().click()
        self.Pages.Page_HelpSearchForANetworkPrinter.checkBox_3().waitForShown().click()
        self.UI_Android.verifyEnabled(self.Pages.Page_HelpSearchForANetworkPrinter.button_tryAgain().isEnabled())

    def test_connectionIssues_step4(self):
        self.Result.set_description("1. From 'Help Search for a Network Printer' page, click on Try Again button when all checkboxes are marked;",
                                   "2. Verify the Printer List page is shown;",
                                   "3. Use both back arrow and HW back button to go back;")
        self.Result.set_expected_result(
            "1. The Printer List page should show when Try Again;",
            "2. App goes back to Help Center when any back button is pressed;")
        self.Pages.Page_HelpSearchForANetworkPrinter.button_tryAgain().click()
        self.Pages.Page_printer.button_addPrinter().verifyIsShown()
        self.Pages.Page_printer.button_image_back().click()
        #self.UI.back()

    def test_PrintQualityTools_step1(self):
        self.Result.set_description("1. App is connected to a EWS-available printer;",
                                   "2. Go to Home page > More Options > Help Center;",
                                   "3. Verify there is a 'Print Quality Tools' option;",
                                   "4. Tap on 'Print Quality Tools'.")
        self.Result.set_expected_result("Verify the corresponding EWS page is launched via an extrenal browser;")
        self.UI_Android.back()

        self.UI_Android.swipeOfType(self.UI_Android.SwipeTo.DOWN)
        self.Pages.Page_home.button_add_printer_link_gray().waitForShown().click()
        self.Pages.Page_printer.printers_1().waitForShown().click()

        self.Pages.Page_home.button_MoreOptions().waitForShown().click()
        self.Pages.Page_home.Menu_moreOptions.menuItem_helpCenter_().waitForShown().click()
        self.Pages.Page_helpCenter.option_PrintQualityTools().verifyIsShown().click().wait(10)
        self.Pages.Page_link_PrintQualityTools.url_PrintQualityTools().verifyIsShown()

    # def test_PrintQualityTools_step2(self):
    #     self.Result.set_description("Precondition:App is connected to a EWS-unavailable printer;",
    #                                "Go to Home page > More Options > Help Center;")
    #     self.Result.set_expected_result("Verify there is NO ""Print Quality Tools"" option;")
    #     # self.UI.back()
    #
    #     self.Pages.Page_home.button_action_add_printer().click()
    #     self.Pages.Page_printer.printers_2().waitForShown().click()
    #     self.Pages.Page_home.button_MoreOptions().waitForShown().click()
    #     self.Pages.Page_home.Menu_moreOptions.menuItem_helpCenter_().waitForShown().click()
    #     self.Pages.Page_helpCenter.option_PrintQualityTools().verifyIsNotShown()






