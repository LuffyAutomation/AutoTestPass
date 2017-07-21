# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmartiOS.po.wrapper.Pages_Ios import Pages_Ios

from projects.HPSmartiOS.data.testData.TestData_Ios import TestData_ios

class HomeFistLaunchiOS(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)  # create page objects of Android test.
        cls.Pages = cls.Pages_Ios  # Just make it simple since generally only one of Android, Ios and Web may be tested.


    def test_flow(self):
        self.Result.setDescription("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.setExpectedResult("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()
        self.Result.addScreenshot(name="homescreenisdisplayed",comment="home screen is displayed")

    def test_gotoAddPrinterScreen(self):
        self.Result.setDescription("1. There are no printer in OOBE mode and go to add printer screen.")
        self.Result.setExpectedResult("The add printer screen is displayed.")
        self.Pages.Page_home.button_add_printer().wait(5).click()
        self.Pages.Page_printers.button_addPrinter().click()
        self.Pages.Page_addPrinter.button_addaNewPrinter().wait(2).click()


    def test_verfiylinkpage(self):
        self.Result.setDescription("1. Verify that the link Displays the HP Privacy Statement in a Safari browser window.",
                                   "2. Users can tap the Close button in the upper-right corner of the screen to return to the app.")
        self.Result.setExpectedResult("1. The HP Privacy Statement is displayed.",
                                      "2. Return to app successfully.")
        #self.UI.swipeUpFromMid()
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.button_moreDtails())
        self.Pages.Page_addPrinter.button_moreDtails().click()
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.link_hpOlinePriacyStatement())
        self.Pages.Page_addPrinter.link_hpOlinePriacyStatement().click()
        self.Pages.Page_linkPrivacyStatement.verfiylinkPage()
        self.Pages.Page_linkPrivacyStatement.button_close().click()

    def test_verifyhpAgreement(self):
        self.Result.setDescription("1. Tap on check App Improvement Program Agreement.",
                                   "2. Tap on check for Special Offers Agreement.",
                                   "3. Tap on check for Supplies Shopping Agreement.")
        self.Result.setExpectedResult("1. App Improvement Program Agreement is displayed.",
                                      "2. Special Offers Agreement is displayed.",
                                      "3. Supplies Shopping Agreement is displayed.")


#self._driver.find_element('xpath', "//*[@value='A4']")
        #verify text_improvementProgram
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.text_improvementProgram())
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.checkbox_improvementProgram())
        self.Pages.Page_addPrinter.text_improvementProgram().verifyEqual(self.Pages.Page_addPrinter.checkbox_improvementProgram().getValue(),"True")
        #verify checkbox_suppliesShopping
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.text_suppliesShopping())
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.checkbox_suppliesShopping())
        self.Pages.Page_addPrinter.checkbox_suppliesShopping().verifyEqual(self.Pages.Page_addPrinter.checkbox_suppliesShopping(),"True")
        #verify test_specialOffers()
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.text_specialOffers())
        self.Pages_Ios.findElementIsShow(self.Pages.Page_addPrinter.checkbox_specialOffers())
        self.Pages.Page_addPrinter.checkbox_specialOffers().verifyEqual(self.Pages.Page_addPrinter.checkbox_specialOffers(),"True")
        self.UI_Ios.back()


    def test_verify_close(self):
        self.Result.setDescription("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.setExpectedResult("Screen goes back to AiO Home.")