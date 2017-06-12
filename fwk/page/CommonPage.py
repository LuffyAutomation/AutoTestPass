class CommonPage:
    def __init__(self):
        self._elementsMap = self.UI.getUiMap(self.page_name)
        return self

    def updateForSubPage(self, child_page_name=None, elementsMap=None):
        if "\\" in self.page_name:  # avoid duplicate adding if continuously operated subpage.
            self.page_name = self.page_name.split("\\")[0]
        if elementsMap is None:  # 0 level page
            self.elementsMap = self._elementsMap
        else:
            self.elementsMap = elementsMap
            self.page_name += "\\" + child_page_name
