import inspect
from fwk.page.WebCommonPage import WebCommonPage


'''main page.'''
class Page_home2_model(WebCommonPage):
    page_name = 'page_home2'

    def __init__(self):
        self.__WebCommonPage = WebCommonPage.__init__(self)
        self.Page_home3 = self._Page_home3_model(self.__WebCommonPage)

    def link_selectAPrinter(self):
        return self.get(inspect.stack()[0][3])

    '''NA'''
    class _Page_home3_model:
        def __init__(self, outer=WebCommonPage):
            self.page_name = 'page_home3'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.get_uimap_of_subpage(self.__outer.page_name, self.page_name)

        def menuItem_about_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)
