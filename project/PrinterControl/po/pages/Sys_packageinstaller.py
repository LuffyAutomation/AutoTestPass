from project.PrinterControl.po.models.Sys_packageinstaller_model import Sys_packageinstaller_model


'''for android 6.0 'Allow xxxx to access device's location'.'''
class Sys_packageinstaller(Sys_packageinstaller_model):
    def __init__(self, UI):
        self.UI = UI
        Sys_packageinstaller_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def flow_xxxxxx(self):
        pass       #self.button_xxxx().waitForShown().click()
