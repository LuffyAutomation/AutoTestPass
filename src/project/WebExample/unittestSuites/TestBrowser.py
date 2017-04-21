# coding: utf-8
import unittest
import traceback
from src.project.WebExample.WebPortal import WebPortal
from src.project.WebExample.po.wrapper.Pages import Pages


class TestBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.Portal = WebPortal()
            cls.Pages = Pages(cls.Portal)
            cls.Result = cls.Portal.Result(cls.Portal)
            cls.Result.setTestName(cls.__name__)
        except Exception as e:
            traceback.print_exc()
            cls.Portal.logger.info(e.__str__())
            cls.Portal.quit()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.Result.afterClass(cls)
        except Exception as e:
            traceback.print_exc()
            cls.Portal.logger.info(e.__str__())

    def setUp(self):
        self.Result.beforeEachFunction(self)

    def tearDown(self):
        self.Result.afterEachFunction(self)

    def test_flow(self):
        self.Result.setDescription("1. Launch %s." % self.Portal._testType,
                                   "2. Go to www.baidu.com.")
        self.Result.setExpectedResult("Page 'www.baidu.com' is displayed.")
        self.Pages.Page_home.open_main_page()
        self.Pages.Page_home.edit_search().setValue("21212")
        pass


