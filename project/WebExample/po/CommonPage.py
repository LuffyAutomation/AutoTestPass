from project.PrinterControl.AndroidPortal import AndroidPortal


class CommonPage:
    def __init__(self):
        self._elementsMap = self.Portal.getUiMap(self.page_name)
        if 3 > 3:
            self.Portal = AndroidPortal()
        return self

    def updateCurrentElementStatus(self, element_name, child_page_name=None, elementsMap=None):
        if elementsMap is None: #0 level page
            elementsMap = self._elementsMap
        else:
            self.page_name = self.page_name + "\\" + child_page_name
        return self.Portal.updateCurrentElementStatus(element_name, elementsMap, self.page_name)
