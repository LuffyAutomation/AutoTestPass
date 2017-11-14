# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmartiOS.po.wrapper.Pages_Ios import Pages_Ios

from projects.HPSmartiOS.data.testData.TestData_Ios import TestData_ios

class scaniOS(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)  # create page objects of Android test.
        cls.Pages = cls.Pages_Ios  # Just make it simple since generally only one of Android, Ios and Web may be tested.


    def test_flow(self):
        self.Result.set_description("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.set_expected_result("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()
        self.Result.add_screenshot(name="homescreenisdisplayed", comment="home screen is displayed")

    def test_addPrinter(self):
        self.Result.set_description("1. Added printer")
        self.Result.set_expected_result("The printer is added successfully.")
        self.Pages.Page_home.button_add_printer().click()
        self.Pages.Page_printers.button_addPrinter().click()
        self.Pages.Page_addPrinter.button_connectPrinterIPaddress().click()
        self.Pages.Page_connectThePrinter.enterComment().waitForShown().click()
        self.Pages.Page_connectThePrinter.enterComment().setValue(value="10.10.52.68", idx_or_match=None,
                                                                  element_name="enterComment")    # input ip address
        self.Pages.Page_connectThePrinter.keyboard_done().click()
        self.Pages.Page_parinterFound.button_yes().waitForShown().click()


    def test_verifyScanSettings(self):
        self.Result.set_description("1. Verif the Scan settings displays",
                                   "-Input Type   ->Image   ->Document",
                                   "-Input Source ->Scanner Glass  ->Document Feeder(If support)",
                                   "Quality  ->Normal  ->Draft",
                                   "Color  ->Color   ->Black", )
        self.Result.set_expected_result("They are displayed.")
        self.Pages.Page_home.tile_ScanToEmail().waitForShown().click()
        self.Pages.Page_scan.text_scanner().verifyIsShown()
        self.Pages.Page_scan.text_scanner().click()
        self.Pages.Page_scan.button_settings().click()
        self.Pages.Page_scanSettings.verfiyScanSettings()

        self.Pages.Page_scanSettings.text_inputType().click()
        self.Pages.Page_inputTpye.verifyInputScreen()
        try:
            self.Pages.Page_scanSettings.text_inputSourece().verifyIsShown()
            self.Pages.Page_scanSettings.text_inputSourece().click()
            self.Pages.Page_inputSource.verifyInputScreen()
        except:
            print "The printer does net support inputSourece function."
        self.Pages.Page_scanSettings.text_quality().click()
        self.Pages.Page_quality.verfiyScanSettings()

        self.Pages.Page_scanSettings.text_color().click()
        self.Pages.Page_color.verfiyScanSettings()
        self.Pages.Page_scanSettings.button_done().click()

    def test_scanTwoWays(self):
        #  glass
        #  feeder
        self.Result.set_description("1. Initiate a scan job with Scanner Glass.",
                                   "2. Initiate a scan job with Document Feeder.")
        self.Result.set_expected_result("1. Successfully, Glass Scan function.",
                                      "2. Successfully, Feeder Scan function.")


        try:
            self.Pages.Page_scan.button_settings().waitForShown().click()
            if self.Pages.Page_inputSource.verifyInputScreen():
                self.Pages.Page_inputSource.text_scannerGlass().click()    # scan job with Scanner Glass.
                self.Pages.Page_inputSource.button_back().click()
                self.Pages.Page_scanSettings.button_done().click()
                self.Pages.Page_scan.button_scanner().waitForShown(2).click()
                self.Pages.Page_scanComplete.button_save().waitForShown(20)          #verfify successfully.
                self.Pages.Page_scanComplete.button_save().click()
                self.Pages.Page_scanComplete.button_addJob().click()         #Go to next scan

            if  self.Pages.Page_scan.button_settings().verifyIsShown():
                self.Pages.Page_scan.button_settings().click()
                self.Pages.Page_inputSource.text_documentFeeder().click()      #scan job with Document Feeder
                self.Pages.Page_inputSource.button_back().click()
                self.Pages.Page_scanSettings.button_done().click()
                self.Pages.Page_scan.button_scanner().waitForShown(2).click()
                self.Pages.Page_scanComplete.button_save().waitForShown(20)         #verfify successfully.
                self.Pages.Page_scanComplete.button_save().click()
        except:
            print "The printer does net support inputSourece function."
            self.Pages.Page_scan.button_scanner().waitForShown().click()   #Auto scan
            self.Pages.Page_scanComplete.button_save().waitForShown(20)  # verfify successfully.
            self.Pages.Page_scanComplete.button_save().click()
            self.Pages.Page_scanComplete.button_addJob().click()



    def test_verify_close(self):
        self.Result.set_description("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.set_expected_result("Screen goes back to AiO Home.")