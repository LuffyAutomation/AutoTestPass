# coding: utf-8
import traceback
import unittest

from fwk.base.InitFwk import InitFwk
from fwk.object.AndroidFwk import AndroidFwk
from fwk.object.IosFwk import IosFwk
from fwk.other.Result import Result
from fwk.object.WebFwk import WebFwk


class CommonUnittest(unittest.TestCase):

    @classmethod
    def setUpBeforClass(cls):
        '''
        cls.UI and cls.Pages are default test objects, if only one of Ios, Android and Web needs to be tested.
        It is just fine to just use them.
        '''
        cls.UI = None
        cls.UI_Ios = None
        cls.UI_Android = None
        cls.UI_Web = None
        cls.Pages_Android = None
        cls.Pages = None
        cls.Pages_Ios = None
        cls.Pages_Web = None
        cls.TestData_Android = None

        try:
            cls.InitFwk = InitFwk()
            cls.InitFwk.createResultFolder()
            # cls.InitFwk = InitFwk(GlobalArgs.getProjectName(), GlobalArgs.getProjectPath())
            if cls.InitFwk.TestType.ANDROID.lower() == cls.InitFwk.testType.lower():
                cls.UI_Android = AndroidFwk(cls.InitFwk)
                # cls.Pages_Android = Pages_Android(cls.UI_Android)
                cls.UI = cls.UI_Android
                # cls.Pages = cls.Pages_Android
            elif cls.InitFwk.TestType.IOS.lower() == cls.InitFwk.testType.lower():
                cls.UI_Ios = IosFwk(cls.InitFwk)
                # cls.Pages_Ios = Pages_Ios(cls.UI_Ios)
                cls.UI = cls.UI_Ios
                # cls.Pages = cls.Pages_Ios
            elif cls.InitFwk.TestType.WEB.lower() == cls.InitFwk.testType.lower():
                cls.UI_Web = WebFwk(cls.InitFwk)
                # cls.Pages_Web = Pages_Web(cls.UI_Web)
                cls.UI = cls.UI_Web
                # cls.Pages = cls.Pages_Web
            cls.Result = Result(cls.UI, cls.InitFwk, cls.__name__)  # avoid errors when the next step failed.
            cls.UI.getDriver()
            if cls.UI_Android is None:
                cls.UI_Android = AndroidFwk(cls.InitFwk)
            if cls.UI_Ios is None:
                cls.UI_Ios = IosFwk(cls.InitFwk)
            if cls.UI_Web is None:
                cls.UI_Web = WebFwk(cls.InitFwk)
            cls.Result = Result(cls.UI, cls.InitFwk, cls.__name__)
            cls.Result.beforeClass()
        except Exception as e:
            # traceback.print_exc()
            cls.UI.logger.error(traceback.format_exc())
            cls.Result.setEnvBlockMsg(e.__str__())
            try:
                if cls.UI_Ios.hasGotDriver is True:
                    cls.UI_Ios.quit()
            except:
                pass
            try:
                if cls.UI_Android.hasGotDriver is True:
                    cls.UI_Android.quit()
            except:
                pass
            try:
                if cls.UI_Web.hasGotDriver is True:
                    cls.UI_Web.quit()
            except:
                pass
            cls.UI.logger.error(e.__str__())

    @classmethod
    def tearDownClass(cls):
        try:
            cls.UI.logger.info("Quitting connection.")
            try:
                if cls.UI_Ios.hasGotDriver is True:
                    cls.UI_Ios.quit()
            except:
                pass
            try:
                if cls.UI_Android.hasGotDriver is True:
                    cls.UI_Android.quit()
            except:
                pass
            try:
                if cls.UI_Web.hasGotDriver is True:
                    cls.UI_Web.quit()
            except:
                pass
            try:
                cls.Result.afterClass(cls)
            except:
                pass
        except Exception as e:
            cls.UI.logger.error(e.__str__())

    def setUp(self):
        try:
            self.Result.beforeEachFunction(self)
        except:
            pass

    def tearDown(self):
        try:
            self.Result.afterEachFunction(self)
        except:
            pass

