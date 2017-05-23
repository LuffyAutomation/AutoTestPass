# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
# import one or multiple kind of Pages_ that you need.
from projects.PLACEHOLDER.po.wrapper.Pages_Android import Pages_Android
# from projects.PLACEHOLDER.po.wrapper.Pages_Ios import Pages_Ios
# from projects.PLACEHOLDER.po.wrapper.Pages_Web import Pages_Web

class PLACEHOLDER(CommonUnittest):
    '''
    1. self.Result.setDescription and self.Result.setExpectedResult don't have to be written.
    2. Do not write setUpClass, tearDownClass, setUp and tearDown
    3. If other drivers are needed, please select the following statements according to related test requirement:
        cls.UI_Android.getDriver()
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
        cls.setUpBeforClass() #setup test before starting.
        cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
        # cls.Pages_Web = Pages_Web(cls.UI_Web)
        # cls.Pages_Ios = Pages_Android(cls.UI_Ios)
        cls.Pages = cls.Pages_Android  # Just make it simple since generally only one of Android, Ios and Web may be tested.
        '''
        1. Description and Expected Result will be loaded automatically from caseInfo.xlsx if you invoke
        cls.Result.loadAndroidCaseInfoFromExcel()/cls.Result.loadIosCaseInfoFromExcel()/cls.Result.loadWebCaseInfoFromExcel().
        2. You also can specify the sheet name cls.Result.loadAndroidCaseInfoFromExcel("xxxx"), if you leave it as empty, the 
        class name will be the as default sheet name.
        '''
        # cls.Result.loadAndroidCaseInfoFromExcel()

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

        self.Result.setDescription("1. xxxx.",
                                   "2. xx.",
                                   "3. xxxx.")
        self.Result.setExpectedResult("xxxxxx.")
        # self.Pages.Page_XXX.button_xxxx.click()

    def test_your_other_flow(self):
        self.Result.setDescription("1. xxxx.",
                                   "2. xx.",
                                   "3. xxxx.")
        self.Result.setExpectedResult("xxxxxx.")
        # self.Pages.Page_XXX.button_xxxx.click()

