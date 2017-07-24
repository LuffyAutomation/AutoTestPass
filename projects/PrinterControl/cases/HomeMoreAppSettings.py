# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.PrinterControl.po.wrapper.Pages_Android import Pages_Android

from projects.PrinterControl.data.testData.TestData_Android import TestData_Android

class HomeMoreAppSettings(CommonUnittest):
    '''
    1. self.Result.setDescription and self.Result.setExpectedResult don't have to be written.
    2. setUpClass(cls) is reserved function, please keep it. Do not write any of tearDownClass, setUp and tearDown.
    3. If other drivers are needed, please select the following statements according to related test requirement:
        cls.UI_Android.getDriver()
        cls.UI_Web.getDriver()
        cls.UI_Ios.getDriver()
    4. Please use following 3 instance for the invoking of page objects of whole Test Case.
        cls.Pages_Android = Pages_Android(cls.UI_Android)
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)
        cls.Pages_Web = Pages_Web(cls.UI_Web)
        cls.Pages = cls.Pages_Android
    5. self.Result.setStepContinueFromFailIfBlock()  # By using this function, current step will not be blocked if the last step was failed or blocked. Please put it next to related function name.
    6. workflow example:
    def test_exmaple(self):
        self.Pages_Android = Pages_Android(self.UI_Android)
        self.Pages = self.Pages_Android
        self.Result.setDescription("1. xxxxx.",
                                   "2. xxxxx.")
        self.Result.setExpectedResult("xxxxxx is displayed.")
        self.Result.addScreenshot("begin", "This is a begin.")  # Add a screenshot. It can be added more.
        self.Result.addComment("The Aio application version is %s?" % self.Pages.Page_about.text_version().getValue()) #  It can be added more.
        self.Pages.xxxxxxxxx
    '''

    @classmethod
    def setUpClass(cls):
        try:
            cls.setUpBeforClass()  # setup test before starting.
            cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
            cls.Pages = cls.Pages_Android  # Just make it simple since generally only one of Android, Ios and Web may be tested.
        except Exception as e:
            cls.UI.logger.error(e.__str__())
            cls.Result.setEnvBlockMsg(e.__str__())
        '''
        1. Description and Expected Result will be loaded automatically from caseInfo.xlsx if you invoke
        cls.Result.loadAndroidCaseInfoFromExcel()/cls.Result.loadIosCaseInfoFromExcel()/cls.Result.loadWebCaseInfoFromExcel().
        2. You also can specify the sheet name cls.Result.loadAndroidCaseInfoFromExcel("xxxx"), if you leave it as empty, the 
        class name will be the as default sheet name.
        '''
        # cls.Result.loadAndroidCaseInfoFromExcel()
        # TestData_Android.Sheet_example.dp_msg_upload_waiting()
        '''
        1. Test Data will be loaded from testData.xlsx if you invoke
        cls.UI_Android.loadTestDataFromExcel()/cls.UI_Web.loadTestDataFromExcel()/cls.UI_Ios.loadTestDataFromExcel().
        2. There are 2 methods to get test data strings.
            2.1 testData_string_1 = cls.UI_Android.getTestData("dp_msg_upload_waiting")
            2.2 Run createTestDataStrings.py to create TestData_Android/TestData_Ios/TestData_Web. 
                Invoke cls.TestData_Android = TestData_Android(cls.UI_Android) 
                Invoke testData_string_1 = cls.TestData_Android.Sheet_example.dp_msg_upload_waiting()
        '''
        # cls.UI_Android.loadTestDataFromExcel()
        # testData_string_1 = cls.UI_Android.getTestData("dp_msg_upload_waiting")
        # cls.TestData_Android = TestData_Android(cls.UI_Android)
        # testData_string_1 = cls.TestData_Android.Sheet_example.dp_msg_upload_waiting()

    def test_flow(self):
        '''
        1. If cls.Result.loadAndroidCaseInfoFromExcel() is invoked and the class name matchs the sheet name in the excel and the function name matches the ID in the excel.
        2. self.Result.setDescriptionAndExpectedResultFromExcel("test_flow") can select any case from caseInfo.xlsx.
        3. The function name will be used as the case id if you leave the ("test_flow") as empty.
        4. self.Result.setDescriptionAndExpectedResultFromExcel can replace self.Result.setDescription and self.Result.setExpectedResult.
        5. self.Result.setDescription and self.Result.setExpectedResult are be recommenced since it is convenient for other people to check case.
        '''
        # self.Result.setDescriptionAndExpectedResultFromExcel()

        self.Result.setDescription("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.setExpectedResult("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()

    def test_verifyCheckbox(self):
        self.Result.setDescription("1. XXXX.",
                                   "2. XXXXXX.")
        self.Result.setExpectedResult("1. xxxxx.",
                                      "2. xxxx.",
                                      "3. xxxxx.")
        self.Pages.Page_home.flow_open_menuItemAppSettings()

        '''How to identify a non-unique element by a nearby/Left/Right/Upper/Lower unique element, please related uiMaps for details."
        ***Method: uiMap.xml configuration***'''
        self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_refNearby().click()
        self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_refLeft().click()
        '''How to identify a non-unique element by a nearby unique element, please related uiMaps for details."
        ***Method: Code***'''
        self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_forNearby1().getByNearbyUniqueElement(self.Pages.Page_appSettings.text_HPSuppliesShopping_forNearby1()).waitForShown().click()
        '''"How to identify a non-unique element by a unique element, please related uiMaps for details. The waitForShown() method does not take effect on following 4 lines. "
        ***Method: Code***'''
        self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_forNearby1().getByLeftUniqueElement(self.Pages.Page_appSettings.text_HPSuppliesShopping_forNearby1()).waitForShown().click()
        #self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_forNearby1().getByRightUniqueElement(self.Pages.Page_appSettings.text_HPSuppliesShopping_forNearby1()).waitForShown().click()
        #self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_forNearby1().getByUpperUniqueElement(self.Pages.Page_appSettings.text_HPSuppliesShopping_forNearby1()).waitForShown().click()
        #self.Pages.Page_appSettings.checkBox_HPSuppliesShopping_forNearby1().getByLowerUniqueElement(self.Pages.Page_appSettings.text_HPSuppliesShopping_forNearby1()).waitForShown().click()

        '''
        How to use matcher signs, see related uiMaps for details.
        '''
        self.Pages.Page_appSettings.text_HPSuppliesShopping1().waitForShown()
        self.Pages.Page_appSettings.text_HPSuppliesShopping2().waitForShown()
        self.Pages.Page_appSettings.text_HPSuppliesShopping3().waitForShown()
        self.Pages.Page_appSettings.text_HPSuppliesShopping4().waitForShown()
        self.Pages.Page_appSettings.text_HPSuppliesShopping5().waitForShown()

        '''
        How to verify Enabled.
        '''
        self.UI_Android.verifyEnabled(self.Pages.Page_appSettings.checkBox_usageTracking().isEnabled())
        '''
        How to verify Selected.
        '''
        self.UI_Android.verifyUnselected(self.Pages.Page_appSettings.checkBox_usageTracking().isSelected())
        '''
        How to verify Checked.
        '''
        self.UI_Android.verifyChecked(self.Pages.Page_appSettings.checkBox_usageTracking().isChecked())
        ''' 
        Or any of the following.
        1. self.UI_Android.verifyChecked(self.Pages.Page_appSettings.checkBox_usageTracking().getValue())
        2. self.Pages.Page_appSettings.UI.verifyChecked(self.Pages.Page_appSettings.checkBox_usageTracking().getValue())
        3. self.UI_Android.verifyEqual(self.Pages.Page_appSettings.checkBox_usageTracking().getValue(), self.UI_Android.VerifyString.CHECKED)
        4. self.Pages.Page_appSettings.UI.verifyEqual(self.Pages.Page_appSettings.checkBox_usageTracking().getValue(), self.UI_Android.VerifyString.CHECKED)
        '''

        '''
        How to verify count.
        '''
        self.UI_Android.verifyCount(self.Pages.Page_appSettings.checkBox_All_setIndex().getItemsCount(), 3)

        '''
        How to handle the elements that have the same property. There are 3 ways to do it.
        '''
        '''1. Set the index of the element <= 0 in uiMap.xml.'''
        self.Pages.Page_appSettings.checkBox_All_setIndex().getItem(1).click()
        self.Pages.Page_appSettings.checkBox_All_setIndex().getItem(2).click()
        self.Pages.Page_appSettings.checkBox_All_setIndex().getItem(3).click()
        '''2. Set the value of the index of the element according to the actual sequence in uiMap.xml.'''
        self.Pages.Page_appSettings.checkBox_usageTracking().click()
        self.Pages.Page_appSettings.checkBox_hpSuppliesShopping().click()
        self.Pages.Page_appSettings.checkBox_wirelessNetwork().click()
        '''3. Without setting the index in uiMap.xml.'''
        self.Pages.Page_appSettings.checkBox_All_noIndex().getItems().getItem(1).click()
        self.Pages.Page_appSettings.checkBox_All_noIndex().getItems().getItem(2).click()
        self.Pages.Page_appSettings.checkBox_All_noIndex().getItems().getItem(3).click()
        self.UI_Android.verifyCount(self.Pages.Page_appSettings.checkBox_All_noIndex().getItems().getItemsCount(), 3)

        '''
        How to verify if all specifiled elements are Checked or not.
        '''
        self.UI_Android.verifyUnchecked(self.Pages.Page_appSettings.checkBox_All_noIndex().isAllChecked())
        self.UI_Android.verifyUnchecked(self.Pages.Page_appSettings.checkBox_All_setIndex().isAllChecked())
        '''Only return the checked status of the first element of all.'''
        self.UI_Android.verifyUnchecked(self.Pages.Page_appSettings.checkBox_All_setIndex().isChecked())
        self.UI_Android.verifyUnchecked(self.Pages.Page_appSettings.checkBox_All_noIndex().isChecked())
        self.UI_Android.verifyUnchecked(self.Pages.Page_appSettings.checkBox_All_noIndex().getItems().isChecked())

        '''other'''
        self.UI_Android.verifyContain("ere", "e")
        self.UI_Android.verifyNotContain("ere", "3")
        self.UI_Android.verifyNotEqual("erer", "wewe")

