import inspect
from fwk.page.IosCommonPage import IosCommonPage


''''''
class Page_edit_model(IosCommonPage):
    page_name = 'page_edit'

    def __init__(self):
        self.__IosCommonPage = IosCommonPage.__init__(self)

    def text_edit(self):
        return self.get(inspect.stack()[0][3])

    def text_copies(self):
        return self.get(inspect.stack()[0][3])

    def copies1(self):
        return self.get(inspect.stack()[0][3])

    def copies2(self):
        return self.get(inspect.stack()[0][3])

    def copies3(self):
        return self.get(inspect.stack()[0][3])

    def copies4(self):
        return self.get(inspect.stack()[0][3])

    def copies5(self):
        return self.get(inspect.stack()[0][3])

    def text_colorAndQuality(self):
        return self.get(inspect.stack()[0][3])

    def quality(self):
        return self.get(inspect.stack()[0][3])

    def quality_draft(self):
        return self.get(inspect.stack()[0][3])

    def quality_normal(self):
        return self.get(inspect.stack()[0][3])

    def quality_best(self):
        return self.get(inspect.stack()[0][3])

    def colorOption(self):
        return self.get(inspect.stack()[0][3])

    def colorOption_color(self):
        return self.get(inspect.stack()[0][3])

    def colorOption_black(self):
        return self.get(inspect.stack()[0][3])

    def colorOption_grayscale(self):
        return self.get(inspect.stack()[0][3])

    def text_paper(self):
        return self.get(inspect.stack()[0][3])

    def size(self):
        return self.get(inspect.stack()[0][3])

    def A4(self):
        return self.get(inspect.stack()[0][3])

    def letter(self):
        return self.get(inspect.stack()[0][3])

    def usLegal(self):
        return self.get(inspect.stack()[0][3])

    def source(self):
        return self.get(inspect.stack()[0][3])

    def automatic(self):
        return self.get(inspect.stack()[0][3])

    def main_tray(self):
        return self.get(inspect.stack()[0][3])

    def type(self):
        return self.get(inspect.stack()[0][3])

    def photoPaper(self):
        return self.get(inspect.stack()[0][3])

    def plainPage(self):
        return self.get(inspect.stack()[0][3])

    def text_resizeAndMove(self):
        return self.get(inspect.stack()[0][3])

    def manual(self):
        return self.get(inspect.stack()[0][3])

    def original_size(self):
        return self.get(inspect.stack()[0][3])

    def fitToPage(self):
        return self.get(inspect.stack()[0][3])

    def fillPage(self):
        return self.get(inspect.stack()[0][3])

    def button_done(self):
        return self.get(inspect.stack()[0][3])

    def button_cancel(self):
        return self.get(inspect.stack()[0][3])
