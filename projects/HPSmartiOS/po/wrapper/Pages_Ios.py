from projects.HPSmartiOS.po.pages.ios.Page_mainHome import Page_mainHome
from projects.HPSmartiOS.po.pages.ios.Page_edit import Page_edit
from projects.HPSmartiOS.po.pages.ios.Page_printPhotos import Page_printPhotos
from projects.HPSmartiOS.po.pages.ios.Page_googleDriveSafari import Page_googleDriveSafari
from projects.HPSmartiOS.po.pages.ios.Page_addAccount_pageFiles import Page_addAccount_pageFiles
from projects.HPSmartiOS.po.pages.ios.Page_GoogleDrive import Page_GoogleDrive
from projects.HPSmartiOS.po.pages.ios.Page_files import Page_files
from projects.HPSmartiOS.po.pages.ios.Page_myPhotoStream import Page_myPhotoStream
from projects.HPSmartiOS.po.pages.ios.Page_myPhotos import Page_myPhotos
from projects.HPSmartiOS.po.pages.ios.Page_photos import Page_photos
from projects.HPSmartiOS.po.pages.ios.Page_parinterFound import Page_parinterFound
from projects.HPSmartiOS.po.pages.ios.Page_scanComplete import Page_scanComplete
from projects.HPSmartiOS.po.pages.ios.Page_connectThePrinter import Page_connectThePrinter
from projects.HPSmartiOS.po.pages.ios.Page_inputSource import Page_inputSource
from projects.HPSmartiOS.po.pages.ios.Page_color import Page_color
from projects.HPSmartiOS.po.pages.ios.Page_quality import Page_quality
from projects.HPSmartiOS.po.pages.ios.Page_inputTpye import Page_inputTpye
from projects.HPSmartiOS.po.pages.ios.Page_scanSettings import Page_scanSettings
from projects.HPSmartiOS.po.pages.ios.Page_scan import Page_scan
from projects.HPSmartiOS.po.pages.ios.Page_linkPrivacyStatement import Page_linkPrivacyStatement
from projects.HPSmartiOS.po.pages.ios.Page_addPrinter import Page_addPrinter
from projects.HPSmartiOS.po.pages.ios.Page_printers import Page_printers
from projects.HPSmartiOS.po.pages.ios.Page_printerInfor import Page_printerInfor
# coding: utf-8
from projects.HPSmartiOS.po.pages.ios.Page_personalize import Page_personalize
from projects.HPSmartiOS.po.pages.ios.Dialog_legalInformation import Dialog_legalInformation


from projects.HPSmartiOS.po.pages.ios.Page_appsettings import Page_appsettings
from projects.HPSmartiOS.po.pages.ios.Page_about import Page_about
#from projects.HPSmartiOS.po.pages.ios.Page_app_settings import Page_app_settings
from projects.HPSmartiOS.po.pages.ios.Page_home import Page_home
from projects.HPSmartiOS.po.pages.ios.Page_welcome import Page_welcome
from projects.HPSmartiOS.po.pages.ios.Page_agreements import Page_agreements
from projects.HPSmartiOS.po.pages.ios.Page_other import Page_other
from projects.HPSmartiOS.po.pages.ios.Page_first import Page_first

from selenium import webdriver
from fwk.base.UiBaseWebDriverFwk import UiBaseWebDriverFwk



class Pages_Ios:
    def __init__(self, UI):
        self._UI = UI
        self.Page_mainHome = Page_mainHome(self._UI)
        self.Page_edit = Page_edit(self._UI)
        self.Page_printPhotos = Page_printPhotos(self._UI)
        self.Page_googleDriveSafari = Page_googleDriveSafari(self._UI)
        self.Page_addAccount_pageFiles = Page_addAccount_pageFiles(self._UI)
        self.Page_GoogleDrive = Page_GoogleDrive(self._UI)
        self.Page_files = Page_files(self._UI)
        self.Page_myPhotoStream = Page_myPhotoStream(self._UI)
        self.Page_myPhotos = Page_myPhotos(self._UI)
        self.Page_photos = Page_photos(self._UI)
        self.Page_parinterFound = Page_parinterFound(self._UI)
        self.Page_scanComplete = Page_scanComplete(self._UI)
        self.Page_connectThePrinter = Page_connectThePrinter(self._UI)
        self.Page_inputSource = Page_inputSource(self._UI)
        self.Page_color = Page_color(self._UI)
        self.Page_quality = Page_quality(self._UI)
        self.Page_inputTpye = Page_inputTpye(self._UI)
        self.Page_scanSettings = Page_scanSettings(self._UI)
        self.Page_scan = Page_scan(self._UI)
        self.Page_linkPrivacyStatement = Page_linkPrivacyStatement(self._UI)
        self.Page_addPrinter = Page_addPrinter(self._UI)
        self.Page_printers = Page_printers(self._UI)
        self.Page_printerInfor = Page_printerInfor(self._UI)
        self.Page_personalize = Page_personalize(self._UI)
        self.Dialog_legalInformation = Dialog_legalInformation(self._UI)
        self.Page_appsettings = Page_appsettings(self._UI)
        self.Page_about = Page_about(self._UI)
        self.Page_home = Page_home(self._UI)
        self.Page_welcome = Page_welcome(self._UI)
        self.Page_agreements = Page_agreements(self._UI)
        self.text_copyRightCompany = Page_about(self._UI)
        self.Page_other = Page_other(self._UI)
        self.Page_first = Page_first(self._UI)




    # This is function template of how to write your Business Logic.
    def example(self):
        pass
    '''Custom public method'''
    # def flow_goTo_PageHomeWithSpecifiedPrinter(self):
    #     self.Page_agreements.flow_agreements()
    #     self.Page_welcome.flow_welcome()
    #     self.Mpl.flow_foundYourPrinter_multiplePages()
    #     self.Page_printerList.flow_selectPrinter()

    '''Custom public method'''
    def flow_goTo_PageHomeWithoutPrinter(self):
        #self.Page_welcome.button_start().click()
        self.Page_welcome.button_start().waitForShown().click()
        self.Page_agreements.flow_agreements()
        self.Dialog_legalInformation.dialog_all().wait(5).click()   #ios allow dialog.

    # def getValueTest(self):
    #     a = self.Personalize.scan_switchButton().swipe()
    #     return a

    def gotoAppSettingsScreen(self):
        self.Page_home.button_settings().swipeDownFromMid().wait(2).click()

    def swipeDownScreen(self):
        self._UI.swipeUpFromBottomToTop(bottom_offset_percent=10)

    def findElementIsShow(self, element,swipeNum = 10):
        for i in range(1,swipeNum):
            if element.isVisible():
                return True
            else:
                self._UI.swipeUpFromMid()
        return False

    def aa(self):
        a = self._UI.getDriver()
        a.execute_script('mobile:keyevent',3)
        print 1
        #a.find_element_by_xpath("//XCUIElementTypeApplication[@name='HP Smart']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]//XCUIElementTypeButton")


    #   self._UI.kangxiaowen(self.Page_addPrinter.area_improvementProgram(),"checkbox_improvementProgram","area_improvementProgram").click()

    def background_app(self, seconds):
    #     """Puts the application in the background on the device for a certain
    #         duration.
    #
    #         :Args:
    #          - seconds - the duration for the application to remain in the background
    #     """
    #     data = {
    #             'seconds': seconds,
    #         }
    #     self.execute(Command.BACKGROUND, data)
    #     return self


        """


        # statTime = time.time()
        # while True:
        #     element_name = self._get_current_element_name_when_none(element_name)
        #     returnValue = self.__verifyIs(time_out, verify_shown, idx_or_match, element_name, log_head)
        #     if returnValue == True:
        #         self.logger.info("Passed!")
        #         return True
        #     else:
        #         nowTime = time.time()
        #         if (nowTime - statTime) < time_out:
        #             self.swipeDownFromMid()
        #             self.logger.info("Continue find element.")
        #         else:
        #             self.logger.info("Faile find element.")
        #             break
        # return False

    # def gotoAboutScreen(self):
    #     self.Page_appsettings.more_about().click()
    #
    # def verify_Icon_Version_APPName(self):
    #     self.Page_about.image_appIcon().verifyIsShown()
    #     #self.Page_about.text_versionLable().verifyEqual(self.Page_about.text_versionLable().getValue(), "Version: 5.4")
    #     # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")
    #     self.Page_about.text_appName().verifyEqual(self.Page_about.text_appName().getValue(), "HP Smart")
    #
    # def verify_CopyRight(self):
    #     self.Page_about.text_copyRightCompany().verifyEqual(self.Page_about.text_copyRightCompany().getValue()," Copyright 2011-2017 HP Development Company, L.P.")
    #     # This is function template of how to write your Business Logic.
    #
    # def verify_hpOnlinePrivacyStatement(self):
    #     self.Page_about.link_hpOnlinePrivacyStatement().verifyIsShown()"""