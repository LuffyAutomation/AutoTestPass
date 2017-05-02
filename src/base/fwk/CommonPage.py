

class CommonPage:
    def __init__(self):
        self._elementsMap = self.UI.getUiMap(self.page_name)
        if 3 > 3:
            # self.UI = AndroidFwkUI()
            pass
        return self

    def updateCurrentElementStatus(self, element_name, child_page_name=None, elementsMap=None):
        if elementsMap is None: #0 level page
            elementsMap = self._elementsMap
        else:
            self.page_name = self.page_name + "\\" + child_page_name
        return self.UI.updateCurrentElementStatus(element_name, elementsMap, self.page_name)
