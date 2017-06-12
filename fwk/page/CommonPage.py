class CommonPage:
    def __init__(self):
        self._elementsMap = self.UI.getUiMap(self.page_name)
        return self

    def updateForSubPage(self, child_page_name=None, elementsMap=None):
        if elementsMap is None:  # 0 level page
            self.elementsMap = self._elementsMap
        else:
            self.elementsMap = elementsMap
            if not self.page_name.endswith("\\" + child_page_name):  #  avoid duplicate add if continuously operate subpage.
                self.page_name += "\\" + child_page_name
