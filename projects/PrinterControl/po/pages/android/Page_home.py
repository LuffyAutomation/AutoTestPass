import inspect
from projects.PrinterControl.po.models.android.Page_home_model import Page_home_model


'''main page.'''
class Page_home(Page_home_model):
    def __init__(self, UI):
        self.UI = UI
        Page_home_model.__init__(self)

    def __open_menuMoreOptions(self):
        self.button_MoreOptions().waitForShown().click()

    def flow_open_menuItemAbout(self):
        self.__open_menuMoreOptions()
        self.Menu_moreOptions.menuItem_about_().waitForShown().click()

    def flow_open_menuItemAppSettings(self):
        self.__open_menuMoreOptions()
        self.Menu_moreOptions.menuItem_appSettings_().waitForShown().click()

    def flow_open_menuItemDevInvestigations(self):
        self.__open_menuMoreOptions()
        self.Menu_moreOptions.menuItem_devInvestigations().waitForShown().click()

    def flow_open_menuItemGiveFeedback(self):
        self.__open_menuMoreOptions()
        self.Menu_moreOptions.menuItem_giveFeedback_().waitForShown().click()

    def flow_open_menuItemShowWelcomeScreen(self):
        self.__open_menuMoreOptions()
        self.Menu_moreOptions.menuItem_showWelcomeScreen_().waitForShown().click()
