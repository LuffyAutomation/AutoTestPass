# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.WebExample.po.wrapper.Pages_Web import Pages_Web


class TestBrowser(CommonUnittest):
    # 1. self.Result.setDescription and self.Result.setExpectedResult can be ignored.
    # 2. Do not write setUpClass, tearDownClass, setUp and tearDown
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
    #     self.Pages.xxxxxxxxx

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass() #setup test before starting.
        cls.Pages_Web = Pages_Web(cls.UI_Web)  # create page objects of Android test.
        cls.Pages = cls.Pages_Web  # Just make it simple, you can ignore this step.
    def test_flow(self):
        self.Result.setDescription("1. Launch %s." % self.Portal._testType,
                                   "2. Go to www.baidu.com.")
        self.Result.setExpectedResult("Page 'www.baidu.com' is displayed.")
        self.Pages.Page_home.open_main_page()
        self.Pages.Page_home.edit_search().setValue("21212")



