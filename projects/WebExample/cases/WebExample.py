# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.WebExample.po.wrapper.Pages_Web import Pages_Web


class WebExample(CommonUnittest):
    '''
    1. self.Result.setDescription and self.Result.setExpectedResult don't have to be written.
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
        self.Result.setDescription("1. xxxxx.",
                                   "2. xxxxx.")
        self.Result.setExpectedResult("xxxxxx is displayed.")
        self.Result.addScreenshot("begin", "This is a begin.")  # Add a screenshot. It can be added more.
        self.Result.addComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue()) #  It can be added more.
        self.Pages.xxxxxxxxx
    '''

    @classmethod
    def setUpClass(cls):
        try:
            cls.setUpBeforClass()  # setup test before starting.
            cls.Pages_Web = Pages_Web(cls.UI_Web)  # create page objects of Android test.
            cls.Pages = cls.Pages_Web  # Just make it simple since generally only one of Android, Ios and Web may be tested.
        except Exception as e:
            cls.UI.logger.error(e.__str__())
            cls.Result.setEnvBlockMsg(e.__str__())
    '''
    1. Description and Expected Result will be loaded automatically from caseInfo.xlsx if you invoke
    cls.Result.loadAndroidCaseInfoFromExcel()/cls.Result.loadIosCaseInfoFromExcel()/cls.Result.loadWebCaseInfoFromExcel().
    2. You also can specify the sheet name cls.Result.loadAndroidCaseInfoFromExcel("xxxx"), if you leave it as empty, the 
    class name will be the as default sheet name.
    '''
    # cls.Result.loadAndroidCaseInfoFromExcel()
    # TestData_Android.Sheet_example.dp_msg_upload_waiting()
    '''
    1. Test Data will be loaded from testData.xlsx if you invoke
    cls.UI_Android.loadTestDataFromExcel()/cls.UI_Web.loadTestDataFromExcel()/cls.UI_Ios.loadTestDataFromExcel().
    2. There are 2 methods to get test data strings.
        2.1 testData_string_1 = cls.UI_Web.getTestData("dp_msg_upload_waiting")
        2.2 Run createTestDataStrings.py to create TestData_Android/TestData_Ios/TestData_Web. 
            Invoke cls.TestData_Web = TestData_Web(cls.UI_Web) 
            Invoke testData_string_1 = cls.TestData_Web.Sheet_example.dp_msg_upload_waiting()
    '''

    # cls.UI_Web.loadTestDataFromExcel()
    # testData_string_1 = cls.UI_Web.getTestData("dp_msg_upload_waiting")
    # cls.TestDataWeb = TestData_Web(cls.UI_Web)
    # testData_string_1 = cls.TestData_Web.Sheet_example.dp_msg_upload_waiting()

    def test_flow1(self):
        self.Result.setDescription("1. Launch %s." % self.UI_Web.RunTimeConf.browser,
                                   "2. Go to www.baidu.com.")
        self.Result.setExpectedResult("Page 'www.baidu.com' is displayed.")
        raise Exception("Fail this step and see whether the next step will be blocked.")

    def test_flow(self):
        '''
        1. If cls.Result.loadAndroidCaseInfoFromExcel() is invoked and the class name matchs the sheet name in the excel and the function name matches the ID in the excel.
        2. self.Result.setDescriptionAndExpectedResultFromExcel("test_flow") can select any case from caseInfo.xlsx.
        3. The function name will be used as the case id if you leave the ("test_flow") as empty.
        4. self.Result.setDescriptionAndExpectedResultFromExcel can replace self.Result.setDescription and self.Result.setExpectedResult.
        5. self.Result.setDescription and self.Result.setExpectedResult are be recommenced since it is convenient for other people to check case.
        '''
        self.Result.setDescription("1. Launch %s." % self.UI_Web.RunTimeConf.browser,
                                   "2. Go to www.baidu.com.")
        self.Result.setExpectedResult("Page 'www.baidu.com' is displayed.")
        self.Pages.Page_home.open_main_page()
        self.Pages.Page_home.edit_search().setValueBySendKeys("21212")

    def test_flow2(self):

        self.Result.setStepContinueFromFailorBlock()

        self.Result.setDescription("1. Launch %s." % self.UI_Web.RunTimeConf.browser,
                                   "2. Go to www.baidu.com.")
        self.Result.setExpectedResult("Page 'www.baidu.com' is displayed.")
        self.Pages.Page_home.open_main_page()
        self.Pages.Page_home.edit_search().waitForShown()
        self.Pages.Page_home.edit_search().setValueBySendKeys("21212")
        self.Pages.Page_home.edit_search().click().click
        self.Pages.Page_home.button_continue().click()
        pass

