# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.PrinterControl.po.wrapper.Pages_Android import Pages_Android

from projects.PrinterControl.data.testData.TestData_Android import TestData_Android

class HomeMoreAbout(CommonUnittest):
    '''
    1. self.Result.set_description and self.Result.set_expected_result don't have to be written.
    2. setUpClass(cls) is reserved function, please keep it. Do not write any of tearDownClass, setUp and tearDown.
    3. If other drivers are needed, please select the following statements according to related test requirement:
        cls.UI_Android.getDriver()
        cls.UI_Web.getDriver()
        cls.UI_Ios.getDriver()
    4. Please use following 3 instance for the invoking of page objects of whole Test Case.
        cls.Pages_Android = Pages_Android(cls.UI_Android)
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)
        cls.Pages_Web = Pages_Web(cls.UI_Web)
        cls.Pages = cls.Pages_Android
    5. self.Result.setStepContinueFromFailIfBlock()  # By using this function, current step will not be blocked if the last step was failed or blocked. Please put it next to related function name.
    6. workflow example:
    def test_exmaple(self):
        self.Pages_Android = Pages_Android(self.UI_Android)
        self.Pages = self.Pages_Android
        self.Result.set_description("1. xxxxx.",
                                   "2. xxxxx.")
        self.Result.set_expected_result("xxxxxx is displayed.")
        self.Result.add_screenshot("begin", "This is a begin.")  # Add a screenshot. It can be added more.
        self.Result.add_comment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue()) #  It can be added more.
        self.Pages.xxxxxxxxx
    '''

    @classmethod
    def setUpClass(cls):
        try:
            cls.setUpBeforClass()  # setup test before starting.
            cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
            cls.Pages = cls.Pages_Android  # Just make it simple since generally only one of Android, Ios and Web may be tested.
        except Exception as e:
            cls.UI.logger.error(e.__str__())
            cls.Result.setEnvBlockMsg(e.__str__())
        '''
        1. Description and Expected Result will be loaded automatically from caseInfo.xlsx if you invoke
        cls.Result.load_android_case_info_from_excel()/cls.Result.load_ios_case_info_from_excel()/cls.Result.load_web_case_info_from_excel().
        2. You also can specify the sheet name cls.Result.load_android_case_info_from_excel("xxxx"), if you leave it as empty, the 
        class name will be the as default sheet name.
        '''
        # cls.Result.load_android_case_info_from_excel()
        # TestData_Android.Sheet_example.dp_msg_upload_waiting()
        '''
        1. Test Data will be loaded from testData.xlsx if you invoke
        cls.UI_Android.load_test_data_from_excel()/cls.UI_Web.load_test_data_from_excel()/cls.UI_Ios.load_test_data_from_excel().
        2. There are 2 methods to get test data strings.
            2.1 testData_string_1 = cls.UI_Android.get_test_data("dp_msg_upload_waiting")
            2.2 Run createTestDataStrings.py to create TestData_Android/TestData_Ios/TestData_Web. 
                Invoke cls.TestData_Android = TestData_Android(cls.UI_Android) 
                Invoke testData_string_1 = cls.TestData_Android.Sheet_example.dp_msg_upload_waiting()
        '''
        # cls.UI_Android.load_test_data_from_excel()
        # testData_string_1 = cls.UI_Android.get_test_data("dp_msg_upload_waiting")
        # cls.TestData_Android = TestData_Android(cls.UI_Android)
        # testData_string_1 = cls.TestData_Android.Sheet_example.dp_msg_upload_waiting()

    def test_flow(self):
        '''
        1. If cls.Result.load_android_case_info_from_excel() is invoked and the class name matchs the sheet name in the excel and the function name matches the ID in the excel.
        2. self.Result.set_description_and_expected_result_from_excel("test_flow") can select any case from caseInfo.xlsx.
        3. The function name will be used as the case id if you leave the ("test_flow") as empty.
        4. self.Result.set_description_and_expected_result_from_excel can replace self.Result.set_description and self.Result.set_expected_result.
        5. self.Result.set_description and self.Result.set_expected_result are be recommenced since it is convenient for other people to check case.
        '''
        # self.Result.set_description_and_expected_result_from_excel()

        self.Result.set_description("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.set_expected_result("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()

    def test_aioVersion(self):
        self.Result.set_description("1. Tap on the top right drop down menu.",
                                   "2. Tap on the item About.")
        self.Result.set_expected_result("1. AiO application version text and version number is display correctly.(Check the number on log or screenshot)",
                                      "2. AiO application name is displayed correctly.",
                                      "3. AiO application icon is displayed correctly.")
        self.Pages.Page_home.flow_open_menuItemAbout()
        self.Pages.Page_about.verify_Icon_Version_APPName()
        self.Result.add_comment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue())

    def test_copyRight(self):
        self.Result.set_description("Follow the last step.")
        self.Result.set_expected_result("1. AiO application copy right text is display correctly",
                                      "2. AiO application copy right start year is displayed correctly",
                                      "3. AiO application copy right end year is displayed correctly")
        self.Pages.Page_about.verify_CopyRight()

    def test_legalInformaion(self):
        self.Result.set_description("Follow the last step.",
                                   "1. Tap on the Legal Information link.",
                                   "2. Tap on the OK button.")
        self.Result.set_expected_result("1. Legal information popup is opened.",
                                      "2. Popup tile is Legal information.",
                                      "3. Popup content matches the latest wireframe (Only verify this exists.)")
        self.Pages.Page_about.link_legalInformation().click()
        self.Pages.Dialog_legalInformation.verify_TitleLegalInformation()
        self.Pages.Dialog_legalInformation.button_ok().click()
        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_endUserLicenseAgreement(self):
        self.Result.set_description("Follow the last step.",
                                   "1. Tap on the License agreement link.")
        self.Result.set_expected_result("1. License agreement ui page is opened.",
                                      "2. HP logo is displayed.",
                                      "3. HP license content is correct.(Ignore this step, since there is no correct result now.)")
        self.Pages.Page_about.link_endUserLicenseAgreement().verifyIsShown().click().wait(3)
        self.Pages.Sys_general.text_chrome().clickIfVisible().wait(2)
        self.Pages.Sys_general.text_always().clickIfVisible().wait(1)
        #self.Pages.Page_endUserLicenseAgreement.text_404PageNotFound().verifyIsShown(120)
        self.Pages.Page_endUserLicenseAgreement.image_logo().verifyIsShown(120)
        #' HP® Official Site | Laptops, Computers, Desktops , Printers, and more HP® Official Site | Laptops, Computers, Desktops , Printers, and more'


    def test_endUserLicenseAgreement_back(self):
        self.Result.set_step_continue_from_fail_or_block()  # By using this function, this step will not be blocked if the last step was failed or blocked.
        self.Result.set_description("Follow the last step. Tap on the Back key.")
        self.Result.set_expected_result("Back to About screen displayed.")
        self.UI.back()
        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_hpOnlinePrivacyStatement(self):
        self.Result.set_description("Follow the last step. Tap on the HP Online Privacy link.")
        self.Result.set_expected_result("1. HP Online Privacy ui page is opened.",
                                      "2. HP logo is displayed.",
                                      "3. HP Privacy statement is displayed correctly.")
        self.Pages.Page_about.link_hpOnlinePrivacyStatement().verifyIsShown().click().wait(3)
        self.Pages.Sys_general.text_chrome().clickIfVisible().wait(2)
        self.Pages.Sys_general.text_always().clickIfVisible().wait(1)
        self.Pages.Page_hpOnlinePrivacyStatement.text_hpPrivacyStatementWorldwide().verifyIsShown(90)
        self.Pages.Page_hpOnlinePrivacyStatement.image_logo().verifyIsShown()

    def test_hpOnlinePrivacyStatement_back(self):
        self.Result.set_step_continue_from_fail_or_block()
        self.Result.set_description("Follow the last step. Tap on the OK button.")
        self.Result.set_expected_result("Back to About screen displayed.")
        self.UI.back()

        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_shareThisApp(self):
        # self.Result.set_description("Follow the last step.",
        #                            "1. Tap on the Share this app button.",
        #                            "2. Tap on the Back key.")
        # self.Result.set_expected_result("1. Share with popup is opened.",
        #                               "2. 163 is displayed.",
        #                               "3. Choose a mail provider is displayed.",
        #                               "4. Microsoft exchange active sync is displayed.",
        #                               "5. Other is displayed.",
        #                               "6. QQ is displayed.",
        #                               "7. Sina is displayed.",
        #                               "8. Back to About screen displayed after tapping the Back key.")
        self.Result.set_description("Follow the last step. Tap on the Share this app button.")
        self.Result.set_expected_result("1. Share with popup is opened.",
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
        self.Result.set_step_continue_from_fail_or_block()
        self.Result.set_description("Follow the last step.")
        self.Result.set_expected_result("Back to About screen displayed after tapping the Back key.")
        self.UI.back()
        self.Pages.Page_about.text_title_about().verifyIsShown()

    def test_headerDisplay(self):
        self.Result.set_description("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.set_expected_result("Screen goes back to AiO Home.")
        self.Pages.Page_about.button_back().click()
        self.Pages.Page_home.button_MoreOptions().verifyIsShown()

    def test_test(self):
        self.Result.set_description("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.set_expected_result("Screen goes back to AiO Home.")
        pass


