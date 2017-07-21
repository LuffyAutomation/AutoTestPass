# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.PrinterControl.po.wrapper.Pages_Android import Pages_Android

from projects.PrinterControl.data.testData.TestData_Android import TestData_Android
class Facebook(CommonUnittest):
    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
        cls.Pages = cls.Pages_Android  # Just make it simple since generally only one of Android, Ios and Web may be tested.

    def test_flow(self):
        self.Result.setDescription("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.setExpectedResult("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()


    def test_SignInOrOutOf_FaceBook_step1(self):
        self.Pages.Page_facebook.web_facebook().aaa(self.Pages.Page_facebook.web_facebook())
        self.Result.setDescription("1. 'Print Facebook Photos' tile has been enabled via Personalize tile;"
                                   "2. Not logged into Facebook yet via AiO, or Reset Data."
                                   "3. Tap on 'Print Facebook Photos' tile from Home page."    
                                   "4. Tap Allow if prompted against file permissions.")
        self.Result.setExpectedResult("Verify a webview is launched to the Facebook login page.")

        self.Pages.Page_home.tile_PrintFacebookPhotos().waitForShown().click()