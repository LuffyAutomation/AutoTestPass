import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''How To Print page.'''
class Page_HowToPrint_model(AndroidCommonPage):
    page_name = 'page_HowToPrint'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def button_Cancel(self):
        return self.get(inspect.stack()[0][3])

    def button_Continue(self):
        return self.get(inspect.stack()[0][3])

    def title_HowToPrint_(self):
        return self.get(inspect.stack()[0][3])
