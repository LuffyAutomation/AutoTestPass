from fwk.object.IosFwk import IosFwk

from fwk.page.CommonPage import CommonPage


class IosCommonPage(CommonPage):
    def __init__(self):
        CommonPage.__init__(self)
        if 3 > 3:
            self.UI = IosFwk
        return self

    def get(self, element_name, child_page_name=None, elementsMap=None):
        self.updateForSubPage(child_page_name, elementsMap)
        return self.UI.updateCurrentElementStatus(element_name, self.elementsMap, self.page_name)
