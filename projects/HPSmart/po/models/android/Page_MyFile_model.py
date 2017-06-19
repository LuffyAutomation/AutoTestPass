import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''MyFile page.'''
class Page_MyFile_model(AndroidCommonPage):
    page_name = 'page_MyFile'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)
        self.Menu_DropDownOption = self._Menu_DropDownOption_model(self.__AndroidCommonPage)
        self.Page_menuItem_All = self._Page_menuItem_All_model(self.__AndroidCommonPage)
        self.Page_menuItem_PDF = self._Page_menuItem_PDF_model(self.__AndroidCommonPage)
        self.Page_menuItem_JPEG = self._Page_menuItem_JPEG_model(self.__AndroidCommonPage)
        self.Tile_share = self._Tile_share_model(self.__AndroidCommonPage)
        self.Page_Mail = self._Page_Mail_model(self.__AndroidCommonPage)
        self.Tile_print = self._Tile_print_model(self.__AndroidCommonPage)
        self.Menu_MoreOptions = self._Menu_MoreOptions_model(self.__AndroidCommonPage)
        self.Tile_Delete = self._Tile_Delete_model(self.__AndroidCommonPage)
        self.Tile_SortBy = self._Tile_SortBy_model(self.__AndroidCommonPage)
        self.Tile_Rename = self._Tile_Rename_model(self.__AndroidCommonPage)

    def button_Back(self):
        return self.get(inspect.stack()[0][3])

    def button_DropDownOption(self):
        return self.get(inspect.stack()[0][3])

    def button_share(self):
        return self.get(inspect.stack()[0][3])

    def button_print(self):
        return self.get(inspect.stack()[0][3])

    def title_action_bar(self):
        return self.get(inspect.stack()[0][3])

    def button_MoreOptions(self):
        return self.get(inspect.stack()[0][3])

    '''moreOptions menu.'''
    class _Menu_DropDownOption_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'menu_DropDownOption'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def menuItem_All(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_JPEG(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_PDF(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_SuppliesInfo(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def select_SuppliesInfo(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''All menu.'''
    class _Page_menuItem_All_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'page_menuItem_All'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def checkBox_All_setIndex(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_jpg_1(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_jpg_2(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_pdf_1(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_pdf_2(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''PDF menu.'''
    class _Page_menuItem_PDF_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'page_menuItem_PDF'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def checkBox_pdf_setIndex(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_pdf_1(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_pdf_2(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''JPEG menu.'''
    class _Page_menuItem_JPEG_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'page_menuItem_JPEG'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def checkBox_pdf_setIndex(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_jpg_1(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def checkbox_jpg_2(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''share menu.'''
    class _Tile_share_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'tile_share'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def title_BlueTooth(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def title_Mail(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''Mail page.'''
    class _Page_Mail_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'page_Mail'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def title_MicrosoftExchangeActiveSync(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''print tile.'''
    class _Tile_print_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'tile_print'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def button_Cancel(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def button_Continue(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''MoreOptionsmenu.'''
    class _Menu_MoreOptions_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'menu_MoreOptions'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def menuItem_Delete(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_SortBy(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_Rename(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_PrintHelp(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''Delete tile.'''
    class _Tile_Delete_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'tile_Delete'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def button_Yes(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def button_No(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''SortBy tile.'''
    class _Tile_SortBy_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'tile_SortBy'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def button_Date(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def button_Name(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''Rename tile.'''
    class _Tile_Rename_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'tile_Rename'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def dialog_rename(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def button_ok(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def button_cancel(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)
