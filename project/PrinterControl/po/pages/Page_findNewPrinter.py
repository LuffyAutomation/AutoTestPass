from project.PrinterControl.po.models.Page_findNewPrinter_model import Page_findNewPrinter_model


'''We find new printer.'''
class Page_findNewPrinter(Page_findNewPrinter_model):
    def __init__(self, Portal):
        self.Portal = Portal
        Page_findNewPrinter_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def flow_xxxxxx(self):
        pass       #self.button_xxxx().waitForShown().click()
