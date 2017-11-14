# coding: utf-8

from fwk.case.CommonUnittest import CommonUnittest
from projects.HPSmart.po.wrapper.Pages_Android import Pages_Android

from projects.HPSmart.data.testData.TestData_Android import TestData_Android
class Files(CommonUnittest):
    @classmethod
    def setUpClass(cls):
        cls.setUpBeforClass()  # setup test before starting.
        cls.Pages_Android = Pages_Android(cls.UI_Android)  # create page objects of Android test.
        cls.Pages = cls.Pages_Android  # Just make it simple since generally only one of Android, Ios and Web may be tested.

    def test_flow(self):
        self.Result.set_description("1. Install AiO app / clear data of AiO app.",
                                   "2. Launch AiO app.",
                                   "3. Go to Home screen.")
        self.Result.set_expected_result("AiO Home screen is displayed.")
        self.Pages.flow_goTo_PageHomeWithoutPrinter()

    def test_File_Basicfunctionactionbaroption_step1(self):
        self.Result.set_description("Tap on File icon on the action bar")
        self.Result.set_expected_result("1. Verify that the navigation is taken to document selection page",
                                      "2. Verify that the following is displayed :Back Button,HP Logo,Drop down option to select,All documents,PDF,JPEG,upplies Info,Greyed out share button,Greyed out print button,Three dots button for more options,List of documents and checkboxes corresponding to each document.")
        self.Pages.Page_home.button_file().click()
        self.Pages.Page_file.title_MyFile().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()

        self.Pages.Page_MyFile.button_MoreOptions().verifyIsShown()
        self.Pages.Page_MyFile.button_Back().verifyIsShown()
        self.Pages.Page_MyFile.button_print().verifyIsShown()
        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_All().verifyIsShown()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_JPEG().verifyIsShown()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_PDF().verifyIsShown()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_SuppliesInfo().verifyIsShown()

    def test_File_Basicfunctionactionbaroption_step2_3_4_5_6(self):
        self.Result.set_description("Click on the Drop down for document type on header bar,Select All(Scan),Select PDF(Scan),Select JPEG,Select Supplies Info")
        self.Result.set_expected_result("1. Verify after selecting All, all files are displayed in the list",
                                      "2. Verify after selecting PDF, only PDF files are displayed in the list.",
                                      "3. Verify after selecting JPEG, only JPEG files are displayed in the list.")

        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_All().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_jpg_1().verifyIsShown()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_jpg_2().verifyIsShown()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_pdf_1().verifyIsShown()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_pdf_2().verifyIsShown()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_JPEG().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_JPEG.checkbox_jpg_1().verifyIsShown()
        self.Pages.Page_MyFile.Page_menuItem_JPEG.checkbox_jpg_2().verifyIsShown()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_PDF().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_PDF.checkbox_pdf_1().verifyIsShown()
        self.Pages.Page_MyFile.Page_menuItem_PDF.checkbox_pdf_2().verifyIsShown()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_SuppliesInfo().waitForShown().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.select_SuppliesInfo().verifyIsShown()

    def test_File_Basicfunctionactionbaroption_step7(self):
        self.Result.set_description("1. Click on All(Scan) option",
                                   "2. Select a single file for print from the list by checking the checkbox corresponding to the file(pdf.jpeg).")
        self.Result.set_expected_result("1. Verify that the documents are displayed.",
                                      "2. Check on the Checkbox next to a document(pdf/jpeg) is displayed",
                                      "3. Verify that the Share and Print icons in the header bar are enabled.")

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_All().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_jpg_1().waitForShown().click()
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.button_share().isEnabled())
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.button_print().isEnabled())

    def test_File_Basicfunctionactionbaroption_step8(self):
        self.Result.set_description("Click on Share button on the Header bar.")
        self.Result.set_expected_result("Verify that the pop up is displayed up on the List view containing many options to share the document. (Ex: Gmail, Bluetooth, Android Beam etc)")

        self.Pages.Page_MyFile.button_share().click()
        self.UI_Android.swipeOfType(self.UI_Android.SwipeTo.UP)
        self.Pages.Page_MyFile.Tile_share.title_BlueTooth().wait(5).verifyIsShown()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()

    def test_File_Basicfunctionactionbaroption_step9(self):
        self.Result.set_description("Select one of the option for sharing the file.(Ex: gmail)")
        self.Result.set_expected_result("1. Verify that the selected file is attached as an attachment in a new email using Gmail.",
                                      "2. Verify that the Gmail screen is opened and enables sharing the file using Gmail.", )

        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown().click()
        self.Pages.Page_MyFile.Page_Mail.title_MicrosoftExchangeActiveSync().verifyIsShown()
        self.UI_Android.back()

    # def test_File_Basicfunctionactionbaroption_step10(self):
    #     self.Result.set_description("Select on Print Icon on Header bar")
    #     self.Result.set_expected_result(
    #         "1. Veriy that one of the following is displayed",
    #         "2. HPPS Screen is opened for Print, if HPPS is selected as Print solution in App Settings",
    #         "3. ePrint Screen is opened for Print, if ePrint is selected as Print solution in App Settings")
    #
    #     self.Pages.Page_MyFile.button_print().click()
    #     self.Pages.Page_MyFile.Tile_print.button_Cancel().verifyIsShown().click()

    def test_File_Basicfunctionactionbaroption_step11(self):
        self.Result.set_description("1. Click on All(Scan) option",
                                   "2. Select multiple files by checking the checkboxes corresponding to each of the file.")
        self.Result.set_expected_result(
            "1. Verify that the documents are displayed"
            "2. Check on the checkboxes neat to the documents are displayed."
            "3. Verify that the Share icon is enabled."
            "4. Verify that the Print Icon is disabled."
            "5. Verify that the Title is changed to the number of documents selected. (Ex: if 2 files are selected, Page title changes to 2 selected)"
            "6. Note : If the selected multiple files are in JPG format, Print icon is enabled.")

        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_jpg_2().click()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_pdf_1().click()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_pdf_2().click()

        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.button_share().isEnabled())
        self.UI_Android.verifyDisable(self.Pages.Page_MyFile.button_print().isEnabled())
        self.Pages.Page_MyFile.title_action_bar().verifyEqual(self.Pages.Page_MyFile.title_action_bar().getValue(), "4 selected")
        self.Pages.Page_MyFile.button_Back().click()

    def test_FilesMoreOption_step1(self):
        self.Result.set_description("1. On the Header basic function bar, tap on the File button",
                                   "2. In the Documents page, click the More options button (Three dots on the header bar)")
        self.Result.set_expected_result("Veriify that the following are displayed",
                                      "Delete button (greyed out)",
                                      "Sort By button",
                                      "Rename Button (greyed out)",
                                      "Print Help Button.")

        self.Pages.Page_file.title_MyFile().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.UI_Android.verifyDisable(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().isEnabled())
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().isEnabled())
        self.UI_Android.verifyDisable(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().isEnabled())
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_PrintHelp().isEnabled())
        self.UI_Android.back()

    def test_FilesMoreOption_step2(self):
        self.Result.set_description("1. In the Documents screen, Select a single file by clicking the checkbox corresponding to a file in the list",
                                   "2. Click on the More options Button (Three dots button on the header bar)")
        self.Result.set_expected_result("Veriify that the following are displayed",
                                      "Delete button",
                                      "Sort By button(greyed out)",
                                      "Rename Button",
                                      "Print Help Button.")

        self.Pages.Page_MyFile.Page_menuItem_PDF.checkbox_pdf_1().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().isEnabled())
        self.UI_Android.verifyDisable(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().isEnabled())
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().isEnabled())
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_PrintHelp().isEnabled())
        self.UI_Android.back()

    def test_FilesMoreOption_step3(self):
        self.Result.set_description("1. In the Documents screen, Select multiple files by clicking the checkbox corresponding to the files in the list",
                                   "2. Click on the More options Button (Three dots button on the header bar)")
        self.Result.set_expected_result("Veriify that the following are displayed",
                                      "Delete button",
                                      "Sort By button (greyed out)",
                                      "Rename Button (greyed out)",
                                      "Print Help Button.")

        self.Pages.Page_MyFile.Page_menuItem_PDF.checkbox_pdf_2().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().isEnabled())
        self.UI_Android.verifyDisable(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().isEnabled())
        self.UI_Android.verifyDisable(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().isEnabled())
        # self.UI_Android.verifyEnabled(self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_PrintHelp().isEnabled())
        self.UI_Android.back()
        self.Pages.Page_MyFile.button_Back().waitForShown().click()

    def test_01_docs_pdf_pull_down(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - File. ",
                                   "3. Tap All from the pull-down list. ",
                                   "4. Tap Sort By button.",
                                   "5.Tap Date option.",
                                   "6.Tap JPEG from the pull-down list.",
                                   "7.Sort files by Name.",
                                   "8.Tap PDF from the pull-down list.",
                                    "9.Sort files by random option.",
                                    "10.Tap Supplies Info from the pull-down list.",
                                    "11. Sort files by random option.")
        self.Result.set_expected_result("Verify the files can be sorted correctly always in each tab."
                                      "Verify 'Documents'displays as title.")
        # self.Pages.Page_home.button_file().click()
        # self.Pages.Page_file.title_MyFile().waitForShown().click()
        # self.Pages.Page_MyFile.button_MoreOptions().click()

        self.Pages.Page_file.title_MyFile().waitForShown().click()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_All().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Tile_SortBy.button_Date().waitForShown().click()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_JPEG().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Tile_SortBy.button_Name().waitForShown().click()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_PDF().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Tile_SortBy.button_Name().waitForShown().click()

        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_SuppliesInfo().waitForShown().click()
        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Tile_SortBy.button_Name().waitForShown().click()

    def test_02_select_a_file(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - Filescreen. ",
                                   "3. Tap All from the pull-down list. ",
                                   "4. Select random file from the files list.",
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons."
                                      "2. All the valid buttons work well:"
                                      "Preview: preview screen be launched"
                                      "Share: Share Complete action using dialog displays"
                                      "Delete: Delete the selected file"
                                      "Rename: Can rename the selected file"
                                      "More: work well."
                                      "Note: For phone, only 3 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")
        self.Pages.Page_MyFile.button_DropDownOption().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_All().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_jpg_1().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_print().click()
        self.Pages.Page_MyFile.Tile_print.button_Cancel().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Rename.button_cancel().click()

    def test_03_select_multiple_jpegs(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - Filescreen. ",
                                   "3. Tap All from the pull-down list. ",
                                   "4. Select random multiple  file from the files list.",
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons.",
                                      "2. All the valid buttons work well:",
                                      "Preview: preview screen be launched",
                                      "Share: Share Complete action using dialog displays",
                                      "Delete: Delete the selected file",
                                      "Rename: Can rename the selected file",
                                      "More: work well.",
                                        "Note: For phone, only 3 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_jpg_2().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().verifyIsShown()
        self.UI_Android.back()

    def test_04_select_mixed_file_types(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - File screen. ",
                                   "3. Tap All from the pull-down list. ",
                                   "4. Select random multiple files with different format from the files list,e.g. *.jpg + *.pdf + *.html and so on."
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons."
                                      "2. All the valid buttons work well:"
                                      "Share: Share Complete action using dialog displays."
                                      "Delete: Delete the selected file"
                                      "More: work well."
                                      "Note: For phone, only 3 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")
        self.Pages.Page_MyFile.Page_menuItem_All.checkbox_pdf_1().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().verifyIsShown()
        self.UI_Android.back()
        self.Pages.Page_MyFile.button_Back().click()

    def test_05_only_jpegs(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - File screen. ",
                                   "3. Tap JPEG from the pull-down list.. ",
                                   "4. Select a file from the files list.",
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons."
                                      "2. All the valid buttons work well:"
                                      "Preview: preview screen be launched"
                                      "Share: Share Complete action using dialog displays."
                                      "Print: HP Print service plugin application be launched and the print job can be completed successfully."
                                      "Delete: Delete the selected file"
                                      "Rename: Can rename the selected file"
                                      "More: work well."
                                      "Note: For phone, only 3 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")

        self.Pages.Page_file.title_MyFile().waitForShown().click()

        self.Pages.Page_MyFile.button_DropDownOption().waitForShown().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_JPEG().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_JPEG.checkbox_jpg_1().waitForShown().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_print().click()
        self.Pages.Page_MyFile.Tile_print.button_Cancel().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Rename.button_cancel().waitForShown().click()

    def test_06_select_multiple_jpegs(self):
        self.Result.set_description("1. Open the AiO Remote application. "
                                   "2. Launch Basic Function - File screen. "
                                   "3. Tap JPEG from the pull-down list."
                                   "4. Select multiple files from the files list."
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons."
                                      "2. All the valid buttons work well:"
                                      "Share: Share Complete action using dialog displays."
                                      "Delete: Delete the selected file"
                                      "More: work well."
                                      "3. The Print icon is valid"
                                      "Note: For phone, only 2 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")
        self.Pages.Page_MyFile.Page_menuItem_JPEG.checkbox_jpg_2().waitForShown().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_print().click()
        self.Pages.Page_MyFile.Tile_print.button_Cancel().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().verifyIsShown()
        self.UI_Android.back()
        self.Pages.Page_MyFile.button_Back().click()

    def test_07_only_pdf(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - File screen. ",
                                   "3. Tap PDF from the pull-down list.. ",
                                   "4. Select a file from the files list.",
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons.",
                                      "2. All the valid buttons work well:",
                                      "Preview: preview screen be launched",
                                      "Share: Share Complete action using dialog displays.",
                                      "Print: HP Print service plugin application be launched and the print job can be completed successfully.",
                                      "Delete: Delete the selected file",
                                        "Rename: Can rename the selected file",
                                        "More: work well.",
                                        "Note: For phone, only 2 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")
        self.Pages.Page_file.title_MyFile().waitForShown().click()

        self.Pages.Page_MyFile.button_DropDownOption().waitForShown().click()
        self.Pages.Page_MyFile.Menu_DropDownOption.menuItem_PDF().waitForShown().click()
        self.Pages.Page_MyFile.Page_menuItem_PDF.checkbox_pdf_1().waitForShown().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_print().click()
        self.Pages.Page_MyFile.Tile_print.button_Cancel().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Rename.button_cancel().waitForShown().click()

    def test_08_select_multiple_pdfs(self):
        self.Result.set_description("1. Open the AiO Remote application. ",
                                   "2. Launch Basic Function - File screen. ",
                                   "3. Tap PDF from the pull-down list.",
                                   "4. Select multiple files from the files list.",
                                   "5. Check all the buttons on this screen, including the buttons that invalid.")
        self.Result.set_expected_result("1. No error occur when tapping the invalid buttons.",
                                      "2. All the valid buttons work well:",
                                      "Share: Share Complete action using dialog displays.",
                                      "Delete: Delete the selected file",
                                      "More: work well.",
                                      "3. The Print icon is valid",
                                      "Note: For phone, only 2 options displays, the rest go under More menu. For tablet, only 4 options displays, the rest go under More menu.")

        self.Pages.Page_MyFile.Page_menuItem_PDF.checkbox_pdf_2().waitForShown().click()

        self.Pages.Page_MyFile.button_share().click()
        self.Pages.Page_MyFile.Tile_share.title_Mail().verifyIsShown()
        self.UI_Android.back()

        self.Pages.Page_MyFile.button_print().click()
        self.Pages.Page_MyFile.button_print().verifyIsShown()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Delete().waitForShown().click()
        self.Pages.Page_MyFile.Tile_Delete.button_No().waitForShown().click()

        self.Pages.Page_MyFile.button_MoreOptions().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_SortBy().verifyIsShown()

        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().waitForShown().click()
        self.Pages.Page_MyFile.Menu_MoreOptions.menuItem_Rename().verifyIsShown()

        self.UI_Android.back()
        self.Pages.Page_MyFile.button_Back().click()




