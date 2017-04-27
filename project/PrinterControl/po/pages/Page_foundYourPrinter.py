from project.PrinterControl.po.models.Page_foundYourPrinter_model import Page_foundYourPrinter_model


'''We found your printer.'''
class Page_foundYourPrinter(Page_foundYourPrinter_model):
    def __init__(self, UI):
        self.UI = UI
        Page_foundYourPrinter_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def flow_xxxxxx(self):
        pass       #self.button_xxxx().waitForShown().click()
