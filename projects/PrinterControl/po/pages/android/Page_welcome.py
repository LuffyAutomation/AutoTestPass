import inspect
from projects.PrinterControl.po.models.android.Page_welcome_model import Page_welcome_model


'''Welcome page'''
class Page_welcome(Page_welcome_model):
    def __init__(self, UI):
        self.UI = UI
        if 1 > 1:
            from fwk.object.AndroidFwk import AndroidFwk
            self.UI = AndroidFwk(None)
        Page_welcome_model.__init__(self)

    def flow_welcome(self):
        self.button_start().waitForShown().click()

    def flow_welcome_setupLater(self):
        self.link_setupLater().waitForShown().click()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
