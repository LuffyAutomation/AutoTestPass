# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmartiOS.po.wrapper.Pages_Ios import Pages_Ios

from projects.HPSmartiOS.data.testData.TestData_Ios import TestData_ios

class HomePersonalizeiOS(CommonUnittest):
    '''
    1. self.Result.setDescription and self.Result.setExpectedResult don't have to be written.
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
        self.Result.setDescription("1. xxxxx.",
                                   "2. xxxxx.")
        self.Result.setExpectedResult("xxxxxx is displayed.")
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
        1. If cls.Result.loadAndroidCaseInfoFromExcel() is invoked and the class name matchs the sheet name in the excel and the function name matchs the ID inthe  excel,
        self.Result.setDescriptionAndExpectedResultFromExcel() can be omitted.
        2. self.Result.setDescriptionAndExpectedResultFromExcel("test_flow") can select any case from caseInfo.xlsx.
        3. The function name will be used as the case id if you leave the ("test_flow") as empty.
        4. self.Result.setDescriptionAndExpectedResultFromExcel can replace self.Result.setDescription and self.Result.setExpectedResult.
        5. self.Result.setDescription and self.Result.setExpectedResult are be recommenced since it is convenient for other pepole to check case.
        '''
        # self.Result.setDescriptionAndExpectedResultFromExcel()

        self.Result.setDescription("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.setExpectedResult("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()
        self.Result.addScreenshot(name="homescreenisdisplayed",comment="home screen is displayed")

    def test_gotoPersonalizeScreen(self):
        self.Result.setDescription("1. Verify for the 'Personalize' screen.")
        self.Result.setExpectedResult("Personalize screen is displayed.")
        #self.UI_Ios.wait()
        self.Pages.swipeDownScreen()
        self.Pages.Page_home.tile_Personalize().click()
        #self.Pages.Page_personalize.moveThreeTilesUpOrDown()



    def test_verifyPersonalizeScreen(self):
        self.Result.setDescription("1. Verify for the all the tiles options avavilable.",
                                   "2. Tap on the button done, I've got it.")
        self.Result.setExpectedResult("1. Below tiles options is displayed."
                                      "- Print Photos"
                                      "- Camera/scan to email"
                                      "- Get HP Help and Support"
                                      "- Camera/Scan to CLoud"
                                      "- Print Box documents"
                                      "- Print Dropbox Documents"
                                      "- Check HP Instant Ink Dashboard"
                                      "- Print Instagram Photos"
                                      "- Print Google Drive documents"
                                      "- Print Documents"
                                      "- Print Facebook Photos",
                                      "Tiles name with option for on/off.",
                                      "Three lines bar to move the tiles up or down."
                                      "2. The home screen is displayed.")
        self.Pages.Page_personalize.verifyTlesOptions()
        self.Pages.Page_personalize.turnoffONswitchButton()
        self.Pages.Page_personalize.button_done().click()
        self.Pages.Page_home.verifyHomeIsDisplayed()

    def chooseSomeTiles(self):
        self.Result.setDescription("1. Chose some of the tiles and tap on done button.")
        self.Result.setExpectedResult("1. Home screen should display only the tiles in the order the user is choosen.")
        self.Pages.Page_personalize().closeSometiles()
        self.Pages.Page_personalize().button_done().click()
        self.Result.addScreenshot(name="verifyHometiles")
        print "The home screen is displayed some tiles."
        self.Pages.Page_home.verifySomeTiles()

    def test_changPersonalizeSettings(self):
        self.Result.setDescription("1. Change the order of the tiles and tap on done button.",
                                   "2. Verify the home screen.")
        self.Result.setExpectedResult("Home screen should display only the tiles in the order the user is choosen")
        self.Pages.Page_home.verifyHomeIsDisplayed()

    def test_verify_close(self):
        self.Result.setDescription("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.setExpectedResult("Screen goes back to AiO Home.")