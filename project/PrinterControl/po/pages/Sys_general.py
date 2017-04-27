from project.PrinterControl.po.models.Sys_general_model import Sys_general_model


'''for android 6.0 'Allow xxxx to access device's location'.'''
class Sys_general(Sys_general_model):
    def __init__(self, UI):
        self.UI = UI
        Sys_general_model.__init__(self)

    # This is function template of how to write your Buissness Logic.
    
