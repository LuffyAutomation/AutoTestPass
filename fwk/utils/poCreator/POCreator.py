import os

from fwk.utils.utilIO.UtilFile import UtilFile
from fwk.utils.utilIO.UtilFolder import UtilFolder

from fwk.utils.poCreator.POCreatorBase import POCreatorBase


class POCreator(POCreatorBase):
    def __init__(self, path_folder_uiMaps, path_folder_po, isGeneratedInProject=True):
        if not UtilFile.is_path_existing(path_folder_uiMaps):
            return
        if not UtilFile.is_path_existing(path_folder_po):
            UtilFolder.create_folder(path_folder_po)
        POCreatorBase.__init__(self, path_folder_uiMaps, path_folder_po, isGeneratedInProject)

    def findFile(self, rootdir):
        for parent, dirnames, filenames in os.walk(rootdir):
            for dirname in dirnames:
                pass

    def __getWhichPage(self):
        if self.scriptFolderName.lower() == "android":
            return "AndroidCommonPage"
        elif self.scriptFolderName.lower() == "web":
            return "WebCommonPage"
        elif self.scriptFolderName.lower() == "ios":
            return "IosCommonPage"

    def __getWhichFwk(self):
        if self.scriptFolderName.lower() == "android":
            return "AndroidFwk"
        elif self.scriptFolderName.lower() == "web":
            return "WebFwk"
        elif self.scriptFolderName.lower() == "ios":
            return "IosFwk"

    def _getPOModelHead(self, page_name, child_page_name=None, page_description="NA", level=0):
        if page_description is None:
            page_description = "NA"
        tmp = ""
        if level == 0:
            # tmp = self._getPOModelClassImportString(self._COMMONPAGE)
            tmp = "import inspect" + self._newLine
            tmp += "from fwk.page.%s import %s" % (self.__getWhichPage(), self.__getWhichPage())
            tmp += self._newLine + self._newLine \
                + self._newLine + self._getIndent(level) + self._descriptionWrapper + page_description + self._descriptionWrapper \
                + self._newLine + self._getIndent(level) + "class %s(%s):" % (self._getPOModelClassName(page_name), self.__getWhichPage()) \
                + self._newLine + self._getIndent(level) + self._indent + "page_name = '%s'" % page_name \
                + self._newLine + self._newLine + self._getIndent(level) + self._indent + "def __init__(self):" \
                + self._newLine + self._getIndent(level) + self._indent + self._indent + "self.__%s = %s.__init__(self)" % (self.__getWhichPage(), self.__getWhichPage()) \
                + self._newLine
        else:
            tmp += self._newLine + self._getIndent(level) + self._descriptionWrapper + page_description + self._descriptionWrapper \
                + self._newLine + self._getIndent(level) + "class _%s:" % self._getPOModelClassName(child_page_name) \
                + self._newLine + self._getIndent(level) + self._indent + "def __init__(self, outer=%s):" % self.__getWhichPage() \
                + self._newLine + self._getIndent(level) + self._indent + self._indent + "self.page_name = '%s'" % child_page_name \
                + self._newLine + self._getIndent(level) + self._indent + self._indent + "self.__outer = outer" \
                + self._newLine + self._getIndent(level) + self._indent + self._indent + "self._elementsMap = self.__outer.UI.get_uimap_of_subpage(self.__outer.page_name, self.page_name)" \
                + self._newLine
        return tmp

    def _getPOModelHeadSubClass(self, list_headSubClass, level=1):
        tmp = ""
        for headSubClass in list_headSubClass:
            tmp += self._getIndent(level) + self._indent + "self.%s = self._%s(self.__%s)" % (self._getPOClassName(headSubClass), self._getPOModelClassName(headSubClass), self.__getWhichPage()) \
                   + self._newLine
        return tmp
        # self.SubPagePlaceholder = self._SubPagePlaceholder_Model(self.__CommonPage)

    def _getPOModelBody(self, element_name, level=0):
        # tmp = "return self.get('%s')" % name
        tmp = "return self.get(%s)" % "inspect.stack()[0][3]"
        if level != 0:
            # tmp = "return self.__outer.get('%s', self._elementsMap)" % name
            tmp = "return self.__outer.get(%s, self.page_name, self._elementsMap)" % "inspect.stack()[0][3]"
        return self._newLine + self._getIndent(level) + self._indent + "def %s(self):" % element_name \
               + self._newLine + self._getIndent(level) + self._indent + self._indent + tmp \
               + self._newLine

    def _getPOHead(self, po_name, page_description, level=0):
        tmp = ""
        if level == 0:
            tmp = self._getPOModelClassImportString(po_name) + self._newLine + self._newLine
        tmp += self._newLine + self._getIndent(level) + self._descriptionWrapper + page_description + self._descriptionWrapper \
            + self._newLine + self._getIndent(level) + "class %s(%s):" % (self._getPOClassName(po_name), self._getPOModelClassName(po_name)) \
            + self._newLine + self._getIndent(level) + self._indent + "def __init__(self, UI):" \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + "self.UI = UI" \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + "if False:" \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + self._indent + "from fwk.object.%s import %s" % (self.__getWhichFwk(), self.__getWhichFwk()) \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + self._indent + "self.UI = %s(None)" % self.__getWhichFwk() \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + "%s.__init__(self)" % self._getPOModelClassName(po_name) \
            + self._newLine \
            + self._newLine + self._getIndent(level) + self._indent + "# This is function template of how to write your Business Logic." \
            + self._newLine + self._getIndent(level) + self._indent \
            + \
        '''def example(self):
        pass
        # self.checkbox_accept().waitForShown().click()
        # self.Pages.Page_endUserLicenseAgreement.text_always().clickIfPresent().wait(1)
        # self.button_continue().click()
        # self.button_search().waitForShown(60).click().wait(1)
        # self.Edit_search().setValueBySendKeys("10.10.63.128")
        
        # if VALUE_PLACEHOLDER was defined in uimap.xml like:
        # <element name="text_printerIp" page="page_home"><xpath>//android.widget.TextView[contains(@text,'VALUE_PLACEHOLDER')]</xpath></element>
        # you can find the element by  xxx.replace_placeholder("10").click
        # self.text_printerIp().replace_placeholder("10.10.63.128").click()
        
        # self.image_appIcon().verifyIsShown()
        # A few elements' properties may be changed after a while. It should be searched again by using refresh_element()
        # self.image_appIcon().waitForShown().refresh_element().click()
        # self.text_version().verifyEqual(self.text_version().getValue(), "4.3.19")''' \
            + self._newLine + self._newLine + self._getIndent(level) + self._indent \
            + \
        '''def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass''' \
            + self._newLine
        return tmp

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
