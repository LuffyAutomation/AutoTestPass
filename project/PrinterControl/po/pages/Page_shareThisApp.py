from project.PrinterControl.po.models.Page_shareThisApp_model import Page_shareThisApp_model


'''page_shareThisApp'''
class Page_shareThisApp(Page_shareThisApp_model):
    def __init__(self, UI):
        self.UI = UI
        Page_shareThisApp_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def flow_xxxxxx(self):
        pass       #self.button_xxxx().waitForShown().click()
