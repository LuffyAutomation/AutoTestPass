import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''moreOptions then app settings page.'''
class Page_appSettings_model(AndroidCommonPage):
    page_name = 'page_appSettings'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def checkBox_All_noIndex(self):
        return self.get(inspect.stack()[0][3])

    def checkBox_All_setIndex(self):
        return self.get(inspect.stack()[0][3])

    def checkBox_usageTracking(self):
        return self.get(inspect.stack()[0][3])

    def checkBox_hpSuppliesShopping(self):
        return self.get(inspect.stack()[0][3])

    def checkBox_wirelessNetwork(self):
        return self.get(inspect.stack()[0][3])
