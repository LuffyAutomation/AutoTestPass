from project.PrinterControl.po.models.Page_printerList_model import Page_printerList_model


'''Printer list.'''
class Page_printerList(Page_printerList_model):
    def __init__(self, Portal):
        self.Portal = Portal
        Page_printerList_model.__init__(self)

    def flow_selectPrinter(self):
        self.button_search().waitForShown().click().wait(1)
        self.Edit_search().setValue("10.10.63.128")
        self.text_printerIp().relocateByText("10.10.63.128").click()
