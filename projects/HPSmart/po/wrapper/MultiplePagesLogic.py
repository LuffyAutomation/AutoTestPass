

# Page Choose. Don't know what page will display.
class MultiplePagesLogic:
    def __init__(self, pages, Portal):
        self.Pages = pages
        self._Portal = Portal
    def _event_handleMultipleFindPrinterPages(self):
        right_flow = False
        if not self.Pages.Page_foundYourPrinter.button_later().isVisible() and self.Pages.Page_foundYourPrinter.button_continue().isVisible():
            self.Pages.Page_foundYourPrinter.button_continue().click().wait(3)
            self.Pages.Page_setup.button_ExitSetup().clickIfVisible()
            right_flow = True
        elif self.Pages.Page_foundYourPrinter.link_changePrinter().isVisible():
            self.Pages.Page_foundYourPrinter.link_changePrinter().click().wait(3)
            right_flow = True
        self.Pages.Sys_packageinstaller.link_AllowAccessLocation().clickIfVisible()
        if right_flow:
            return right_flow

    def _event_doNotSelectPrinter(self):
        right_flow = False
        if not self.Pages.Page_foundYourPrinter.button_later().isVisible() and self.Pages.Page_foundYourPrinter.button_continue().isVisible():
            self.Pages.Page_foundYourPrinter.button_continue().click().wait(3)
            self.Pages.Page_setup.button_ExitSetup().clickIfVisible()
            right_flow = True
        elif self.Pages.Page_foundYourPrinter.link_changePrinter().isVisible():
            self.Pages.Page_foundYourPrinter.link_changePrinter().click().wait(3)
            right_flow = True
        self.Pages.Sys_packageinstaller.link_AllowAccessLocation().clickIfVisible()
        if right_flow:
            return right_flow

    def flow_foundYourPrinter_multiplePages(self):
        self._Portal.wait_until(
            lambda: self._event_handleMultipleFindPrinterPages(), "Cannot find found/find printer screen."
        )


        # def sum(x, y=10): return x + y
        # sum2 = lambda x, y=10: x + y
        # print
        # sum2(1)  # 11
        # print
        # sum2(1, 100)  # 101
