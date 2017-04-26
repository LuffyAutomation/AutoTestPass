from project.PrinterControl.po.models.Dialog_legalInformation_model import Dialog_legalInformation_model


'''dialog_legalInformation'''
class Dialog_legalInformation(Dialog_legalInformation_model):
    def __init__(self, Portal):
        self.Portal = Portal
        Dialog_legalInformation_model.__init__(self)

    # This is function template to write your Business wrapper here.
    def verify_TitleLegalInformation(self):
        self.text_title_legalInformation().verifyIsShown()
        self.area_content_legalInformation().verifyIsShown()

        # self.Portal.verifyIsShown("link_legalInformation")
        # self.Portal.clickOn("link_legalInformation")
        # self.Portal.verifyIsShown("text_title_legalInformation")
        # self.Portal.verifyIsShown("area_content_legalInformation")
        # self.Portal.clickOn("button_ok")
        # self.Portal.verifyIsShown("text_title_About")
