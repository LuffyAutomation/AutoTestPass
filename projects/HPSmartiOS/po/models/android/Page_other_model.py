import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''main page.'''
class Page_other_model(AndroidCommonPage):
    page_name = 'page_other'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)
        self.Menu_moreOptions = self._Menu_moreOptions_model(self.__AndroidCommonPage)

    def button_scan(self):
        return self.get(inspect.stack()[0][3])

    '''You can add one level of subpage here.'''
    class _Menu_moreOptions_model:
        def __init__(self, outer=AndroidCommonPage):
            self.page_name = 'menu_moreOptions'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def menuItem_about_(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)
