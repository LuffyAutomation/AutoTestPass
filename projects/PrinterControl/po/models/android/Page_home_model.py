import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''main page.'''
class Page_home_model(AndroidCommonPage):
    page_name = 'page_home'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)
        self.Menu_moreOptions = self._Menu_moreOptions_model(self.__AndroidCommonPage)

    def link_selectAPrinter(self):
        return self.get(inspect.stack()[0][3])

    def button_scan(self):
        return self.get(inspect.stack()[0][3])

    def button_capture(self):
        return self.get(inspect.stack()[0][3])

    def button_file(self):
        return self.get(inspect.stack()[0][3])

    def button_photos(self):
        return self.get(inspect.stack()[0][3])

    def button_printerInfo(self):
        return self.get(inspect.stack()[0][3])

    def tile_printPhotos(self):
        return self.get(inspect.stack()[0][3])

    def tile_Personalize(self):
        return self.get(inspect.stack()[0][3])

    def tile_PrintFacebookPhotos(self):
        return self.get(inspect.stack()[0][3])

    def button_MoreOptions(self):
        return self.get(inspect.stack()[0][3])

    '''NA'''
    class _Menu_moreOptions_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'menu_moreOptions'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.get_uimap_of_subpage(self.__outer.page_name, self.page_name)

        def menuItem_appSettings_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_giveFeedback_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_about_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_showWelcomeScreen_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def menuItem_devInvestigations_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)
