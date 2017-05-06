# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
# import one or multiple kind of Pages_ that you need.
from projects.PLACEHOLDER.po.wrapper.Pages_Android import Pages_Android
# from projects.PLACEHOLDER.po.wrapper.Pages_Ios import Pages_Ios
# from projects.PLACEHOLDER.po.wrapper.Pages_Web import Pages_Web

class PLACEHOLDER(CommonUnittest):
    # 1. self.Result.setDescription and self.Result.setExpectedResult can be ignored.
    # 2. Do not write tearDownClass, setUp and tearDown functions in this file.
    # 3. Please use following 3 instance for the invocking of page objects of whole Test Case.
    # self.Pages_Android = Pages_Android(self.UI_Android)
    # self.Pages_Ios = Pages_Ios(self.UI_Ios)
    # self.Pages_Web = Pages_Web(self.UI_Web)
    # self.Pages = self.Pages_Android

    # def test_exmaple(self):
    # self.Pages_Android = Pages_Android(self.UI_Android)
    # self.Pages = self.Pages_Android
    #     self.Result.setDescription("1. xxxxx.",
    #                                "2. xxxxx.")
    #     self.Result.setExpectedResult("xxxxxx is displayed.")
    #     self.Result.setScreenshot("begin", "This is a begin.")
    #     self.Result.setComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue())
    #     self.Pages.Page_XXX.button_xxxx.click()

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass() #setup test before starting.
        cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
        # cls.Pages_Web = Pages_Web(cls.UI_Web)
        # cls.Pages_Ios = Pages_Android(cls.UI_Ios)
        cls.Pages = cls.Pages_Android  # Just make it simple, you can ignore this step.

    def test_your_flow(self):
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

