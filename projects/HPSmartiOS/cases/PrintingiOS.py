# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmartiOS.po.wrapper.Pages_Ios import Pages_Ios

from projects.HPSmartiOS.data.testData.TestData_Ios import TestData_ios

class PrintingiOS(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Ios = Pages_Ios(cls.UI_Ios)  # create page objects of Android test.
        cls.Pages = cls.Pages_Ios  # Just make it simple since generally only one of Android, Ios and Web may be tested.


    def test_flow(self):
        self.Result.setDescription("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.setExpectedResult("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()
        self.Result.addScreenshot(name="homescreenisdisplayed",comment="home screen is displayed")

    def test_addPrinter(self):
        self.Result.setDescription("1. Added printer")
        self.Result.setExpectedResult("The printer is added successfully.")
        self.Pages.Page_home.button_add_printer().waitForShown().click()
        self.Pages.Page_printers.button_addPrinter().click()
        self.Pages.Page_addPrinter.button_connectPrinterIPaddress().click()
        self.Pages.Page_connectThePrinter.enterComment().waitForShown().click()
        self.Pages.Page_connectThePrinter.enterComment().setValue(value="10.10.52.68", idx_or_match=None,
                                                                  element_name="enterComment")    # input ip address
        self.Pages.Page_connectThePrinter.keyboard_done().click()
        self.Pages.Page_parinterFound.button_yes().waitForShown().click()

    def test_printingPhoto(self):
        self.Result.setDescription("1. Select an image to preview.",
                                   "2. Tap the Settings icon on the Print Preview screen.",
                                   "3. print job via WifIpath with the print settings.")
        self.Result.setExpectedResult("1. The print job can be completed.",
                                      "2. The printout is correct according to the print settings.")
        self.Pages.Page_home.button_photo().waitForShown().click()
        self.Pages.Dialog_legalInformation.ok()#dialog ok
        self.Pages.Page_photos.text_myPhotos().click()
        self.Pages.Page_myPhotos.text_myPhotoStream().click()
        self.Pages.Page_myPhotoStream.picture_1().click()
        self.Pages.Page_printPhotos.button_changSettings().click()
        self.Pages.Page_edit.text_colorAndQuality().click()
        self.Pages.Page_edit.quality().click()
        self.Pages.Page_edit.quality_best().click()
        self.Pages.Page_edit.button_done().click()
        self.Pages.Page_printPhotos.button_print().waitForShown().click()
        self.Pages.Page_photos.button_back.back()
        self.Pages.Page_photos.button_back.back()
        self.Pages.Page_photos.button_back.back()


    def test_printingDocument(self):
        self.Pages_Ios.aa()
        self.Result.setDescription("1. Select a document to preview.",
                                   "2. chang the print settings.",
                                   "3. print job via WiFi path with the prnt settings.")
        self.Result.setExpectedResult("1. The print job can be completed.",
                                      "2. The printout is correct according to the print settings.")
        self.Pages.Page_home.button_file().click()
        self.Pages.Dialog_legalInformation.ok()  # dialog ok
        self.Pages.Page_files.text_addAccount().click()
        self.Pages.Page_addAccount_pageFiles.text_GoogleDrive().click()
        self.Pages.Page_googleDriveSafari.text_useAnotherAccount().click()
        self.Pages.Page_googleDriveSafari.text_inputEmail().setValue(value="kxw789@gmail.com", idx_or_match=None,
                                                              element_name="text_inputEmail")
        self.Pages.Page_googleDriveSafari.button_next().click()
        self.Pages.Page_googleDriveSafari.text_enterPassword().setValue(value="0.123456789", idx_or_match=None,
                                                              element_name="text_enterPassword")
        self.Pages.Page_googleDriveSafari.button_next().click()
        self.Pages.Page_googleDriveSafari.button_allow().click()
        self.Pages.Page_GoogleDrive.document_1().waitForShown().click()
        self.Pages.Page_printPhotos.button_changSettings().click()
        self.Pages.Page_edit.text_colorAndQuality().click()
        self.Pages.Page_edit.quality().click()
        self.Pages.Page_edit.quality_best().click()
        self.Pages.Page_edit.button_done().click()
        self.Pages.Page_printPhotos.button_print().waitForShown().click()
        self.Pages.Page_photos.button_back.back()
        self.Pages.Page_photos.button_back.back()
        self.Pages.Page_photos.button_back.back()




    def test_verify_close(self):
        self.Result.setDescription("Follow the last step.",
                                   "Tap on the Back icon.")
        self.Result.setExpectedResult("Screen goes back to AiO Home.")