from project.WebExample.po.models import Page_home_model


'''Default home page.'''
class Page_home(Page_home_model):
    def __init__(self, Portal):
        self.Portal = Portal
        Page_home_model.__init__(self)

    def open_main_page(self):
        self.Portal.openUrl("http://www.baidu.com")

    # This is function template of how to write your Buissness Logic.
    def flow_example(self):
        pass
        # self.checkbox_accept().waitForShown().click()
        # self.Pages.Page_endUserLicenseAgreement.text_always().clickIfPresent().wait(1)
        # self.button_continue().click()
        # self.button_search().waitForShown().click().wait(1)
        # self.Edit_search().setValue("10.10.63.128")
        # self.text_printerIp().relocateByText("10.10.63.128").click()
        # self.image_appIcon().verifyIsShown()
        # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")