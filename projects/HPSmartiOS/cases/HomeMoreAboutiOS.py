# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmartiOS.po.wrapper.Pages_Ios import Pages_Ios

from projects.HPSmartiOS.data.testData.TestData_Ios import TestData_ios

class HomeMoreAboutiOS(CommonUnittest):
    '''
    1. self.Result.set_description and self.Result.set_expected_result don't have to be written.
    2. setUpClass(cls) is reserved function, please keep it. Do not write any of tearDownClass, setUp and tearDown.
    3. If other drivers are needed, please select the following statements according to related test requirement:
        cls.UI_.getDriver()
        cls.UI_Web.getDriver()
        cls.UI_Ios.getDriver()
    4. Please use following 3 instance for the invoking of page objects of whole Test Case.
        cls.Pages_Android = Pages_Android(cls.UI_Android)
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)
        cls.Pages_Web = Pages_Web(cls.UI_Web)
        cls.Pages = cls.Pages_Android

    def test_exmaple(self):
        self.Pages_Android = Pages_Android(self.UI_Android)
        self.Pages = self.Pages_Android
        self.Result.set_description("1. xxxxx.",
                                   "2. xxxxx.")
        self.Result.set_expected_result("xxxxxx is displayed.")
        self.Result.setScreenshot("begin", "This is a begin.")
        self.Result.setComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue())
        self.Pages.xxxxxxxxx
    '''

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)  # create page objects of Android test.
        cls.Pages = cls.Pages_Ios  # Just make it simple since generally only one of Android, Ios and Web may be tested.
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
        1. If cls.Result.load_android_case_info_from_excel() is invoked and the class name matchs the sheet name in the excel and the function name matchs the ID inthe  excel,
        self.Result.set_description_and_expected_result_from_excel() can be omitted.
        2. self.Result.set_description_and_expected_result_from_excel("test_flow") can select any case from caseInfo.xlsx.
        3. The function name will be used as the case id if you leave the ("test_flow") as empty.
        4. self.Result.set_description_and_expected_result_from_excel can replace self.Result.set_description and self.Result.set_expected_result.
        5. self.Result.set_description and self.Result.set_expected_result are be recommenced since it is convenient for other pepole to check case.
        '''
        # self.Result.set_description_and_expected_result_from_excel()

        self.Result.set_description("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.set_expected_result("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()

    def test_verify_about_sceen(self):
        self.Result.set_description("1. Launch the HP Printer Control application.",
                                   "2. Tap Settings(...)->About to launch the aBOUT Screen.",
                                   "3. Check the screen.")
        self.Result.set_expected_result("1. The app image is displayed.",
                                      "2. App name is displayed.",
                                      "3. version of the app is displayed."
                                      "4. 'HP Online Privacy Statement' is link."
                                        )

        self.Pages.gotoAppSettingsScreen()
        self.Pages.Page_about.gotoAboutScreen()
        self.Pages.Page_about.verify_Icon_Version_APPName()
        self.Pages.Page_about.verify_hpOnlinePrivacyStatement()

    def test_copyRight(self):
        self.Result.set_description("Follow the last step.")
        self.Result.set_expected_result("1. AiO application copy right text is display correctly",
                                      "2. AiO application copy right start year is displayed correctly",
                                      "3. AiO application copy right end year is displayed correctly")
        self.Pages.Page_about.verify_CopyRight()
        self.UI_Ios.back()


    def test_verify_close(self):
        self.Result.set_description("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.set_expected_result("Screen goes back to AiO Home.")