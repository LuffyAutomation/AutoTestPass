# coding: utf-8
import traceback
import unittest

from project.PrinterControl.AndroidPortal import AndroidPortal

from project.PrinterControl.po.wrapper.Pages import Pages


class CommonUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.Portal = AndroidPortal()
            cls.Pages = Pages(cls.Portal)
            cls.Result = cls.Portal.Result(cls.Portal, cls.__name__)
        except Exception as e:
            traceback.print_exc()
            cls.Portal.logger.error(e.__str__())
            cls.Portal.quit()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.Result.afterClass(cls)
        except Exception as e:
            cls.Portal.logger.error(e.__str__())

    def setUp(self):
        self.Result.beforeEachFunction(self)

    def tearDown(self):
        self.Result.afterEachFunction(self)



