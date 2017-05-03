from fwk.object.WebFwk import WebFwk

from fwk.page.CommonPage import CommonPage


class WebCommonPage(CommonPage):
    def __init__(self):
        CommonPage.__init__(self)
        if 3 > 3:
            self.UI = WebFwk
        return self

    def get(self, element_name, child_page_name=None, elementsMap=None):
        self.updateForSubPage(child_page_name, elementsMap)
        return self.UI.updateCurrentElementStatus(element_name, self.elementsMap, self.page_name)
