import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Describe your page here.'''
class Page_first_model(IosCommonPage):
    page_name = 'page_first'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)
        self.Page_agreements = self._Page_agreements_model(self.__IosCommonPage)
        self.Page_welcome = self._Page_welcome_model(self.__IosCommonPage)

    '''Default first page.'''
    class _Page_agreements_model:
        def __init__(self, outer=IosCommonPage):
            self.page_name = 'page_agreements'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def checkbox_accept(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

        def button_continue(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)

    '''Welcome page'''
    class _Page_welcome_model:
        def __init__(self, outer=IosCommonPage):
            self.page_name = 'page_welcome'
            self.__outer = outer
            self._elementsMap = self.__outer.UI.getUiMapOfSubPage(self.__outer.page_name, self.page_name)

        def button_start(self):
            return self.__outer.get(inspect.stack()[0][3], self.page_name, self._elementsMap)
