import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''OnlineSupport page.'''
class Page_link_OnlineSupport_model(AndroidCommonPage):
    page_name = 'page_link_OnlineSupport'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def url_OnlineSupport(self):
        return self.get(inspect.stack()[0][3])

    def title_selectCountryHeader(self):
        return self.get(inspect.stack()[0][3])
