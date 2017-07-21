import inspect
from fwk.page.IosCommonPage import IosCommonPage


'''Touch button_settings go to APP Settings'''
class Page_appsettings_model(IosCommonPage):
    page_name = 'page_appsettings'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def notifications_settings(self):
        return self.get(inspect.stack()[0][3])

    def privacy_settings(self):
        return self.get(inspect.stack()[0][3])

    def heplp_center(self):
        return self.get(inspect.stack()[0][3])

    def contactHPOnFacebookMessenger(self):
        return self.get(inspect.stack()[0][3])

    def tweetUsforSupport(self):
        return self.get(inspect.stack()[0][3])

    def send_feedback(self):
        return self.get(inspect.stack()[0][3])

    def more_about(self):
        return self.get(inspect.stack()[0][3])
