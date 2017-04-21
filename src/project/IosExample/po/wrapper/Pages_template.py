from src.project.WebExample.po.pages.Page_home import Page_home

class Pages:
    def __init__(self, Portal):
        self._Portal = Portal
        self.Page_home = Page_home(self._Portal)
