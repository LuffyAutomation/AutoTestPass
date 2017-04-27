# coding: utf-8
import traceback
import unittest
from src.base.core.InitFwk import InitFwk

from project.PrinterControl.ProjectPortal import ProjectPortal
from src.base.fwk.WebFwk import WebFwk
from src.base.fwk.IosFwk import IosFwk
from project.PrinterControl.po.wrapper.Pages_Android import Pages_Android
from project.PrinterControl.po.wrapper.Pages_Ios import Pages_Ios
from project.PrinterControl.po.wrapper.Pages_Web import Pages_Web
from src.base.fwk.AndroidFwk import AndroidFwk
from src.base.fwk.Result import Result


class CommonUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.UI and cls.Pages are default test objects, if only one of Ios, Android and Web needs to be tested.
        # It is just fine to just use them.
        cls.UI = None
        cls.UI_Ios = None
        cls.UI_Android = None
        cls.UI_Web = None
        try:
            cls.InitFwk = InitFwk(ProjectPortal.getProjectName(), ProjectPortal.getProjectPath())
            if cls.InitFwk.TestType.ANDROID.lower() == cls.InitFwk.testType.lower():
                cls.UI_Android = AndroidFwk(cls.InitFwk)
                cls.Pages_Android = Pages_Android(cls.UI_Android)
                cls.UI = cls.UI_Android
                cls.Pages = cls.Pages_Android
            elif cls.InitFwk.TestType.IOS.lower() == cls.InitFwk.testType.lower():
                cls.UI_Ios = IosFwk(cls.InitFwk)
                cls.Pages_Ios = Pages_Ios(cls.UI_Ios)
                cls.UI = cls.UI_Ios
                cls.Pages = cls.Pages_Ios
            elif cls.InitFwk.TestType.WEB.lower() == cls.InitFwk.testType.lower():
                cls.UI_Web = WebFwk(cls.InitFwk)
                cls.Pages_Web = Pages_Web(cls.UI_Web)
                cls.UI = cls.UI_Web
                cls.Pages = cls.Pages_Web
            cls.UI.getDriver()
            cls.Result = Result(cls.UI, cls.InitFwk, cls.__name__)
        except Exception as e:
            traceback.print_exc()
            if cls.UI_Ios is not None:
                cls.UI_Ios.quit()
            if cls.UI_Android is not None:
                cls.UI_Android.quit()
            if cls.UI_Web is not None:
                cls.UI_Web.quit()
            cls.UI.logger.error(e.__str__())

    @classmethod
    def tearDownClass(cls):
        try:
            if cls.UI_Ios is not None:
                cls.UI_Ios.quit()
            if cls.UI_Android is not None:
                cls.UI_Android.quit()
            if cls.UI_Web is not None:
                cls.UI_Web.quit()
            cls.Result.afterClass(cls)
        except Exception as e:
            cls.UI.logger.error(e.__str__())

    def setUp(self):
        self.Result.beforeEachFunction(self)

    def tearDown(self):
        self.Result.afterEachFunction(self)

