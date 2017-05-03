from src.base.fwk.AndroidFwk import AndroidFwk
from src.base.pageFwk.CommonPage import CommonPage

class AndroidCommonPage(CommonPage):
    def __init__(self):
        CommonPage.__init__(self)
        if 3 > 3:
            self.UI = AndroidFwk
        return self

    def get(self, element_name, child_page_name=None, elementsMap=None):
        self.updateForSubPage(child_page_name, elementsMap)
        return self.UI.updateCurrentElementStatus(element_name, self.elementsMap, self.page_name)
