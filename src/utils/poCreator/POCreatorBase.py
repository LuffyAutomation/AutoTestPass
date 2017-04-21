import os
from abc import abstractmethod

from src.utils.utilString.UtilString import UtilString
from src.utils.utilIO.UtilFile import UtilFile
from src.utils.utilXml.UtilXml import UtilXml


class POCreatorBase:
    class uiMapMarks:
        NAME = "name"
        PAGE = "page"
        DESCRIPION = "description"

    def __init__(self, path_folder_uiMaps, path_folder_po, isGenerateInProject=True):
        self.__IMPORT_STRING_BEGIN_WITH = "src"
        self. __isGenerateInProject = isGenerateInProject
        self._COMMONPAGE = "CommonPage"
        self._PAGES_TEMPLATE = "Pages_template"
        self._PO_SUFFIX = "_model"
        self._PO_MODELS = "models"
        self._PO_PAGES = "pages"
        self._PO_WRAPPER = "wrapper"
        self._newLine = "\n"
        self._indent = "    "
        self._descriptionWrapper = "'''"

        self.__path_folder_po = path_folder_po
        self.__path_folder_pages = os.path.join(path_folder_po, self._PO_PAGES)
        self.__path_folder_models = os.path.join(path_folder_po, self._PO_MODELS)
        self.__path_folder_wrapper = os.path.join(path_folder_po, self._PO_WRAPPER)
        self.__path_folder_po = path_folder_po
        self.__path_folder_uiMaps = path_folder_uiMaps

        self._UtilFile = UtilFile
        self._UtilString = UtilString
        self._UtilXml = UtilXml
        self.__xmlTree = self._UtilXml.getTree(self.__path_folder_uiMaps)
        self._root = self._UtilXml.getRootElement(self.__xmlTree)

        self.__classImportStringHead = self.__getClassImportStringHead()

    def create(self):
        list = self._UtilXml.getElements(self._root, ".//pages/")
        pagesTemplateHead = ""
        pagesTemplateBodyBody = ""
        for index in range(len(list)):
            attributes = self._UtilXml.getAttribute(list[index])
            children = self._UtilXml.getChildren(list[index])
            name = attributes.get(self.uiMapMarks.NAME)
            pagesTemplateHead += self._getPagesClassImportString(name)
            pagesTemplateBodyBody += self._getPagesBodyBody(name)
            description = attributes.get(self.uiMapMarks.DESCRIPION)
            self._writeFile(os.path.join(self.__path_folder_pages, self._getPOFileName(name)), self._getPOHead(name, description))
            _pOModelHead = self._getPOModelHead(name, None, description)
            _pOModelHeadSubClass = ""
            list_subClass = []
            _pOModelModelBody = ""
            _pOModelSubModelBody = ""
            for idx in range(len(children)):
                level = 0
                children_name = self._UtilXml.getAttribute(children[idx]).get(self.uiMapMarks.NAME)
                if self._UtilXml.getTagName(children[idx]) == self.uiMapMarks.PAGE:
                    level += 1
                    list_subClass.append(children_name)
                    children_description = self._UtilXml.getAttribute(children[idx]).get(self.uiMapMarks.DESCRIPION)
                    children_children = self._UtilXml.getChildren(children[idx])
                    _pOModelHeadSubClass += self._getPOModelHead(name, children_name, children_description, level)
                    for c_idx in range(len(children_children)):
                        children_children_name = self._UtilXml.getAttribute(children_children[c_idx]).get(self.uiMapMarks.NAME)
                        _pOModelSubModelBody += self._getPOModelBody(children_children_name, level)
                    _pOModelHeadSubClass += _pOModelSubModelBody
                    _pOModelSubModelBody = ""
                else:
                    _pOModelModelBody += self._getPOModelBody(children_name, 0)
            _pOModelHead += self._getPOModelHeadSubClass(list_subClass, level)
            tmpStr = _pOModelHead + _pOModelModelBody + _pOModelHeadSubClass + _pOModelSubModelBody
            self._writeFile(os.path.join(self.__path_folder_models, self._getPOModelFileName(name)), tmpStr)
        self._writeFile(os.path.join(self.__path_folder_wrapper, self._getPOFileName(self._PAGES_TEMPLATE)), pagesTemplateHead + self._getPagesBodyHead() + pagesTemplateBodyBody)

    def __getClassImportStringHead(self):
        if self.__isGenerateInProject == True:
            tmpPath = self.__IMPORT_STRING_BEGIN_WITH + self.__path_folder_po.split(self.__IMPORT_STRING_BEGIN_WITH)[1]
            self.__classImportStringHead = "from " + tmpPath.replace("/", ".").replace("\\", ".")
            return self.__classImportStringHead

    def _getPOModelClassImportString(self, po_name):
        po_name = self._getPOClassName(po_name)
        classImportString = self.__classImportStringHead
        pOModelClassName = self._getPOModelClassName(po_name)
        if self._COMMONPAGE not in pOModelClassName:
            classImportString += "." + self._PO_MODELS
        tmp = "import inspect" + self._newLine
        return tmp + "%s.%s import %s" % (classImportString, pOModelClassName, pOModelClassName)

    def _getPagesClassImportString(self, po_name):
        po_name = self._getPOClassName(po_name)
        classImportString = self.__classImportStringHead
        # pOModelClassName = self._getPOModelClassName(po_name)
        classImportString += "." + self._PO_PAGES
        return "%s.%s import %s" % (classImportString, po_name, po_name) + self._newLine

    def _getIndent(self, level=0):
        tmp = ""
        for i in range(level):
            tmp += self._indent
        return tmp

    def _getPagesBodyHead(self, level=0):
        return self._newLine + self._getIndent(level) + "class Pages:" \
            + self._newLine + self._getIndent(level) + self._indent + "def __init__(self, Portal):" \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + "self._Portal = Portal" \
            + self._newLine

    def _getPagesBodyBody(self, po_name, level=0):
        tmp = self._getIndent(level) + self._indent + self._indent + "self.%s = %s(self._Portal)" % (self._getPOClassName(po_name), self._getPOClassName(po_name)) \
            + self._newLine
        return tmp

    def _getPOModelClassName(self, po_name):
        if po_name != self._COMMONPAGE:
            return self._getPOClassName(po_name) + self._PO_SUFFIX
        return self._getPOClassName(po_name)

    def _getPOClassName(self, po_name):
        return self._UtilString.capitalizeFirstLetter(po_name)

    def _getPOModelFileName(self, po_name):
        return self._getPOModelClassName(po_name) + ".py"

    def _getPOFileName(self, po_name):
        return self._getPOClassName(po_name) + ".py"

    def _writeFile(self, path_file, txt):
        if not UtilFile.isPathExists(path_file):
            UtilFile.writeFile(path_file, txt, self._UtilFile.FileMode.W)

    @abstractmethod
    def _getPOModelHead(self, page_name, child_page_name, level):
        pass
    @abstractmethod
    def _getPOModelHeadSubClass(self, list_subClass, level):
        pass
    @abstractmethod
    def _getPOModelBody(self, element_name, level):
        pass
    @abstractmethod
    def _getPOHead(self, po_name, level):
        pass
    @abstractmethod
    def _getPagesTemplateHead(self, po_name, importPath):
        pass

#sys._getframe().f_code.co_name