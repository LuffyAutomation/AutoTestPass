import inspect
from projects.PrinterControl.po.models.android.Dialog_legalInformation_model import Dialog_legalInformation_model


'''dialog_legalInformation'''
class Dialog_legalInformation(Dialog_legalInformation_model):
    def __init__(self, UI):
        self.UI = UI
        if 1 > 1:
            from fwk.object.AndroidFwk import AndroidFwk
            self.UI = AndroidFwk(None)
        Dialog_legalInformation_model.__init__(self)

    def verify_TitleLegalInformation(self):
        self.text_title_legalInformation().verifyIsShown()
        self.area_content_legalInformation().verifyIsShown()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass



