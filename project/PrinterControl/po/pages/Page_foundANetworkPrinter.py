from project.PrinterControl.po.models.Page_foundANetworkPrinter_model import Page_foundANetworkPrinter_model


'''We found a network printer!'''
class Page_foundANetworkPrinter(Page_foundANetworkPrinter_model):
    def __init__(self, UI):
        self.UI = UI
        Page_foundANetworkPrinter_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def flow_xxxxxx(self):
        pass       #self.button_xxxx().waitForShown().click()
