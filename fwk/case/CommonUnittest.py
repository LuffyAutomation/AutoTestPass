# coding: utf-8
import traceback
import unittest
from abc import abstractmethod

from fwk.base.GlobalArgs import GlobalArgs
from fwk.base.InitFwk import InitFwk
from fwk.object.AndroidFwk import AndroidFwk
from fwk.object.IosFwk import IosFwk
from fwk.other.Result import Result

from fwk.object.WebFwk import WebFwk


class CommonUnittest(unittest.TestCase):

    @classmethod
    def setUpBeforClass(self):
        # self.UI and self.Pages are default test objects, if only one of Ios, Android and Web needs to be tested.
        # It is just fine to just use them.
        self.UI = None
        self.UI_Ios = None
        self.UI_Android = None
        self.UI_Web = None
        self.Pages_Android = None
        self.Pages = None
        self.Pages_Ios = None
        self.Pages_Web = None
        try:
            self.InitFwk = InitFwk()
            self.InitFwk.createResultFolder()
            # self.InitFwk = InitFwk(GlobalArgs.getProjectName(), GlobalArgs.getProjectPath())
            if self.InitFwk.TestType.ANDROID.lower() == self.InitFwk.testType.lower():
                self.UI_Android = AndroidFwk(self.InitFwk)
                # self.Pages_Android = Pages_Android(self.UI_Android)
                self.UI = self.UI_Android
                # self.Pages = self.Pages_Android
            elif self.InitFwk.TestType.IOS.lower() == self.InitFwk.testType.lower():
                self.UI_Ios = IosFwk(self.InitFwk)
                # self.Pages_Ios = Pages_Ios(self.UI_Ios)
                self.UI = self.UI_Ios
                # self.Pages = self.Pages_Ios
            elif self.InitFwk.TestType.WEB.lower() == self.InitFwk.testType.lower():
                self.UI_Web = WebFwk(self.InitFwk)
                # self.Pages_Web = Pages_Web(self.UI_Web)
                self.UI = self.UI_Web
                # self.Pages = self.Pages_Web
            self.UI.getDriver()
            self.Result = Result(self.UI, self.InitFwk, self.__name__)
        except Exception as e:
            traceback.print_exc()
            if self.UI_Ios is not None:
                self.UI_Ios.quit()
            if self.UI_Android is not None:
                self.UI_Android.quit()
            if self.UI_Web is not None:
                self.UI_Web.quit()
            self.UI.logger.error(e.__str__())

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