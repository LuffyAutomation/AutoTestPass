class CommonPage:
    def __init__(self):
        self._elementsMap = self.UI.getUiMap(self.page_name)
        return self

    def update_for_sub_page(self, child_page_name=None, elements_ui_map=None):
        if "\\" in self.page_name:  # avoid duplicate adding if continuously operated subpage.
            self.page_name = self.page_name.split("\\")[0]
        if elements_ui_map is None:  # 0 level page
            self.elementsMap = self._elementsMap
        else:
            self.elementsMap = elements_ui_map
            self.page_name += "\\" + child_page_name
