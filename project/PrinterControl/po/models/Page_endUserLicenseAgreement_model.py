import inspect

from project.PrinterControl.po.CommonPage import CommonPage

'''page_endUserLicenseAgreement'''
class Page_endUserLicenseAgreement_model(CommonPage):
    page_name = 'page_endUserLicenseAgreement'

    def __init__(self):
        self.__CommonPage = CommonPage.__init__(self)

    def text_404PageNotFound(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])

    def image_logo(self):
        return self.updateCurrentElementStatus(inspect.stack()[0][3])
