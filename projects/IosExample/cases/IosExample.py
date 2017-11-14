# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
# import one or multiple kind of Pages_ that you need.
from projects.IosExample.po.wrapper.Pages_Android import Pages_Android
from projects.IosExample.po.wrapper.Pages_Ios import Pages_Ios
# from projects.IosExample.po.wrapper.Pages_Web import Pages_Web
from projects.IosExample.data.testData.TestData_Android import TestData_Android
# from projects.IosExample.data.testData.TestData_Ios import TestData_Ios
# from projects.IosExample.data.testData.TestData_Web import TestData_Web

class IosExample(CommonUnittest):
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
    5. self.Result.setStepContinueFromFailIfBlock()  # By using this function, current step will not be blocked if the last step was failed or blocked.
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
        cls.setUpBeforClass()  # setup test before starting.
        # cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
        # cls.Pages_Web = Pages_Web(cls.UI_Web)
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)
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
        cls.UI_Android.loadTestDataFromExcel()/cls.UI_Web.loadTestDataFromExcel()/cls.UI_Ios.loadTestDataFromExcel().
        2. There are 2 methods to get test data strings.
            2.1 testData_string_1 = cls.UI_Android.getTestData("dp_msg_upload_waiting")
            2.2 Run createTestDataStrings.py to create TestData_Android/TestData_Ios/TestData_Web. 
                Invoke cls.TestData_Android = TestData_Android(cls.UI_Android) 
                Invoke testData_string_1 = cls.TestData_Android.Sheet_example.dp_msg_upload_waiting()
        '''
        # cls.UI_Android.loadTestDataFromExcel()
        # testData_string_1 = cls.UI_Android.getTestData("dp_msg_upload_waiting")
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
        self.Result.set_description("1. xxxx.",
                                   "2. xx.",
                                   "3. xxxx.")
        self.Result.set_expected_result("xxxxxx.")
        self.Pages.Page_welcome.image_welcome().waitForShown()
        self.Pages.Page_welcome.button_start().click()

    def test_your_other_flow(self):
        self.Result.set_description("1. xxxx.",
                                   "2. xx.",
                                   "3. xxxx.")
        self.Result.set_expected_result("xxxxxx.")
        self.Pages.Page_termsAndConditions.checkbox_1().waitForShown()
        self.Pages.Page_termsAndConditions.checkbox_1().click()
        self.Pages.Page_termsAndConditions.button_Continue().click().wait(3)
        self.Pages.Sys_general.button_doNotAllow().clickIfVisible()
        # self.Pages.Page_home.button_moreOptions().waitForShown().click()
        # self.Pages.Page_moreOptions.toggleSwitchOn_offerToReduceSize().waitForShown()
        self.Pages.Page_home.button_moreOptions().waitForShown().wait(2)
        self.UI_Ios.swipeUpFromBottomToTop(0, 10)
        self.Pages.Page_home.tile_personalizeIcon_image().waitForShown().tap()

        self.Pages.Page_personalizeIcon.buttonOrder_scanToEmail().waitForShown()
        self.Pages.Page_personalizeIcon.buttonOrder_scanToEmail().dragToElement(self.Pages.Page_personalizeIcon.buttonOrder_scan())
        pass

