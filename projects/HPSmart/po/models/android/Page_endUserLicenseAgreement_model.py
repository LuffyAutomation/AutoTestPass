import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''page_endUserLicenseAgreement'''
class Page_endUserLicenseAgreement_model(AndroidCommonPage):
    page_name = 'page_endUserLicenseAgreement'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def text_404PageNotFound(self):
        return self.get(inspect.stack()[0][3])

    def image_logo(self):
        return self.get(inspect.stack()[0][3])
