from project.PrinterControl.po.models.Page_setup_model import Page_setup_model


'''set up printer.'''
class Page_setup(Page_setup_model):
    def __init__(self, UI):
        self.UI = UI
        Page_setup_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def flow_xxxxxx(self):
        pass       #self.button_xxxx().waitForShown().click()
