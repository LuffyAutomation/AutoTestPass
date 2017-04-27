# coding: utf-8
import traceback
import unittest
from src.base.core.InitFwk import InitFwk

from project.PrinterControl.ProjectPortal import ProjectPortal
from src.base.fwk.WebFwk import WebFwk
from src.base.fwk.IosFwk import IosFwk
from project.PrinterControl.po.wrapper.Pages import Pages
from src.base.fwk.AndroidFwk import AndroidFwk
from src.base.fwk.Result import Result


class CommonUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.InitFwk = InitFwk(ProjectPortal.getProjectName(), ProjectPortal.getProjectPath())
            if cls.InitFwk.TestType.ANDROID.lower() == cls.InitFwk.testType.lower():
                cls.UI = AndroidFwk(cls.InitFwk)
            elif cls.InitFwk.TestType.IOS.lower() == cls.InitFwk.testType.lower():
                cls.UI = IosFwk(cls.InitFwk)
            elif cls.InitFwk.TestType.WEB.lower() == cls.InitFwk.testType.lower():
                cls.UI = WebFwk(cls.InitFwk)
            cls.UI.getDriver()
            cls.Pages = Pages(cls.UI)
            cls.Result = Result(cls.UI, cls.InitFwk, cls.__name__)
        except Exception as e:
            traceback.print_exc()
            if cls.UI is not None:
                cls.UI.quit()
            cls.UI.logger.error(e.__str__())

    @classmethod
    def tearDownClass(cls):
        try:
            if cls.UI is not None:
                cls.UI.quit()
            cls.Result.afterClass(cls)
        except Exception as e:
            cls.UI.logger.error(e.__str__())

    def setUp(self):
        self.Result.beforeEachFunction(self)

    def tearDown(self):
        self.Result.afterEachFunction(self)

