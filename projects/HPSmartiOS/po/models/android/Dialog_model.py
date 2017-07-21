import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''Allow/ok button'''
class Dialog_model(AndroidCommonPage):
    page_name = 'dialog'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def dialog_all(self):
        return self.get(inspect.stack()[0][3])

    def dialog_ok(self):
        return self.get(inspect.stack()[0][3])
