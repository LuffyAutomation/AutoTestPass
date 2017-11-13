from fwk.object.AndroidFwk import AndroidFwk

from fwk.page.CommonPage import CommonPage


class AndroidCommonPage(CommonPage):
    def __init__(self):
        CommonPage.__init__(self)
        if 3 > 3:
            self.UI = AndroidFwk
        return self

    def get(self, element_name, child_page_name=None, elements_ui_map=None):
        self.update_for_sub_page(child_page_name, elements_ui_map)
        return self.UI.updateCurrentElementStatus(element_name, self.elements_ui_map, self.page_name)
