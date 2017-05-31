import os
from abc import abstractmethod

from fwk.utils.utilIO.UtilFile import UtilFile
from fwk.utils.utilIO.UtilFolder import UtilFolder
from fwk.utils.utilString.UtilString import UtilString

from fwk.utils.utilXml.UtilXml import UtilXml


class POCreatorBase(object):
    class uiMapMarks:
        NAME = "name"
        PAGE = "page"
        DESCRIPION = "description"

    def __init__(self, path_folder_uiMaps, path_folder_po, isGeneratedInProject=True):
        self._UtilFolder = UtilFolder
        self._UtilFile = UtilFile
        self._UtilString = UtilString
        self._UtilXml = UtilXml
        self.scriptFolderName = path_folder_uiMaps.split("data" + os.path.sep)[1].split(os.path.sep + "uiMaps")[0]
        # self.__IMPORT_STRING_BEGIN_WITH = "src"
        self.__IMPORT_STRING_BEGIN_WITH = "projects"
        self. __isGeneratedInProject = isGeneratedInProject
        self._COMMONPAGE = "CommonPage"
        self._PAGES_TEMPLATE = "Pages_%s_template" % self._UtilString.capitalizeFirstLetter(self.scriptFolderName)
        self._PO_SUFFIX = "_model"
        self._PO_MODELS = "models"
        self._PO_PAGES = "pages"
        self._PO_WRAPPER = "wrapper"
        self._newLine = "\n"
        self._indent = "    "
        self._descriptionWrapper = "'''"

        self.__path_folder_po = path_folder_po
        self.__path_folder_pages = os.path.join(path_folder_po, self._PO_PAGES, self.scriptFolderName)
        self._UtilFolder.createFolder(self.__path_folder_pages)
        self._writeFile(os.path.join(self.__path_folder_pages, "__init__.py"))
        self.__path_folder_models = os.path.join(path_folder_po, self._PO_MODELS, self.scriptFolderName)
        self._UtilFolder.createFolder(self.__path_folder_models)
        self._writeFile(os.path.join(self.__path_folder_models, "__init__.py"))
        self.__path_folder_wrapper = os.path.join(path_folder_po, self._PO_WRAPPER)
        self._UtilFolder.createFolder(self.__path_folder_wrapper)
        self._writeFile(os.path.join(self.__path_folder_wrapper, "__init__.py"))
        self._writeFile(os.path.join(self.__path_folder_wrapper, "Pages_Android.py"))
        self._writeFile(os.path.join(self.__path_folder_wrapper, "Pages_Web.py"), "class Pages_Web: pass")
        self._writeFile(os.path.join(self.__path_folder_wrapper, "Pages_Ios.py"), "class Pages_Ios: pass")
        self.__path_folder_po = path_folder_po
        self.__path_folder_uiMaps = path_folder_uiMaps

        self.__xmlTree = self._UtilXml.getTree(self.__path_folder_uiMaps)
        self._root = self._UtilXml.getRootElement(self.__xmlTree)

        self.__classImportStringHead = self.__getClassImportStringHead()

    def create(self):
        try:
            list = self._UtilXml.getElements(self._root, ".//pages/")
        except:
            return
        list_pagesTemplateHead = []
        pagesTemplateHead = ""
        list_pagesTemplateBodyBody = []
        pagesTemplateBodyBody = ""
        for index in range(len(list)):
            attributes = self._UtilXml.getAttribute(list[index])
            children = self._UtilXml.getChildren(list[index])
            name = attributes.get(self.uiMapMarks.NAME)
            pagesTemplateHead += self._getPagesClassImportString(name)
            list_pagesTemplateHead.append(self._getPagesClassImportString(name))
            pagesTemplateBodyBody += self._getPagesBodyBody(name)
            list_pagesTemplateBodyBody.append(self._getPagesBodyBody(name))
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
            self._writeFileAndOverwrite(os.path.join(self.__path_folder_models, self._getPOModelFileName(name)), tmpStr)
        self._writePagesFile(os.path.join(self.__path_folder_wrapper, "Pages_%s.py" % (self._UtilString.capitalizeFirstLetter(self.scriptFolderName))), list_pagesTemplateHead, self._getPagesBodyHead(), list_pagesTemplateBodyBody)

    def __getClassImportStringHead(self):
        if self.__isGeneratedInProject == True:
            # tmpPath = self.__IMPORT_STRING_BEGIN_WITH + self.__path_folder_po.split(self.__IMPORT_STRING_BEGIN_WITH)[1]
            tmpPath = self.__IMPORT_STRING_BEGIN_WITH + self.__path_folder_po.split(self.__IMPORT_STRING_BEGIN_WITH)[1]
            self.__classImportStringHead = "from " + tmpPath.replace("/", ".").replace("\\", ".")
            return self.__classImportStringHead

    def _getPOModelClassImportString(self, po_name):
        po_name = self._getPOClassName(po_name)
        classImportString = self.__classImportStringHead
        pOModelClassName = self._getPOModelClassName(po_name)
        if self._COMMONPAGE not in pOModelClassName:
            classImportString += "." + self._PO_MODELS
            classImportString += "." + self.scriptFolderName
        tmp = "# coding: utf-8" + self._newLine
        # tmp = "import inspect" + self._newLine
        return tmp + "%s.%s import %s" % (classImportString, pOModelClassName, pOModelClassName)

    def _getPagesClassImportString(self, po_name):
        po_name = self._getPOClassName(po_name)
        classImportString = self.__classImportStringHead
        # pOModelClassName = self._getPOModelClassName(po_name)
        classImportString += "." + self._PO_PAGES + "." + self.scriptFolderName
        return "%s.%s import %s" % (classImportString, po_name, po_name) + self._newLine

    def _getIndent(self, level=0):
        tmp = ""
        for i in range(level):
            tmp += self._indent
        return tmp

    def _getPagesBodyHead(self, level=0):
        return self._getIndent(level) + "class Pages_%s:" % (self._UtilString.capitalizeFirstLetter(self.scriptFolderName)) \
            + self._newLine + self._getIndent(level) + self._indent + "def __init__(self, UI):" \
            + self._newLine + self._getIndent(level) + self._indent + self._indent + "self._UI = UI" \
            + self._newLine
            # + self._newLine + self._getIndent(level) + self._indent + self._indent + "self._UI.getDriver()" \
            # + self._newLine

    def _getPagesBodyBody(self, po_name, level=0):
        tmp = self._getIndent(level) + self._indent + self._indent + "self.%s = %s(self._UI)" % (self._getPOClassName(po_name), self._getPOClassName(po_name)) \
            + self._newLine
        return tmp

    def _getPOModelClassName(self, po_name):
        if self._COMMONPAGE not in po_name:
            return self._getPOClassName(po_name) + self._PO_SUFFIX
        return self._getPOClassName(po_name)

    def _getPOClassName(self, po_name):
        return self._UtilString.capitalizeFirstLetter(po_name)

    def _getPOModelFileName(self, po_name):
        return self._getPOModelClassName(po_name) + ".py"

    def _getPOFileName(self, po_name):
        return self._getPOClassName(po_name) + ".py"

    def _writeFile(self, path_file, txt=""):
        if not self._UtilFile.isPathExists(path_file):
            self._UtilFile.writeFile(path_file, txt, self._UtilFile.FileMode.W)

    def _writeFileAndOverwrite(self, path_file, txt=""):
        self._UtilFile.writeFile(path_file, txt, self._UtilFile.FileMode.W)

    def _writePagesFile(self, path_file, list_pagesTemplateHead, txt_PagesBodyHead, list_pagesTemplateBodyBody):
        global lines, list_existed_pagesTemplateHead, list_existed_pagesTemplateBodyBody, part
        lines = []
        list_existed_pagesTemplateHead = []
        list_existed_pagesTemplateBodyBody = []
        part = 1
        try:
            lines = self._UtilFile.getLinesFromFile(path_file)
            for line in lines:
                if part == 3:
                    list_existed_pagesTemplateBodyBody.append(line)
                if "class Pages_" in line:
                    part = 2
                elif "self._UI = UI" in line:
                    part = 3
                if part == 1:
                    list_existed_pagesTemplateHead.append(line)

            for line in list_pagesTemplateHead:
                if line not in list_existed_pagesTemplateHead:
                    list_existed_pagesTemplateHead.insert(0, line)

            for line in list_pagesTemplateBodyBody:
                if line not in list_existed_pagesTemplateBodyBody:
                    list_existed_pagesTemplateBodyBody.insert(0, line)

            txt_pagesTemplateHead = "".join(list_existed_pagesTemplateHead)
            txt_existed_pagesTemplateBodyBody = "".join(list_existed_pagesTemplateBodyBody)
            if not txt_pagesTemplateHead.endswith(self._newLine + self._newLine):
                # txt_PagesBodyHead = txt_PagesBodyHead.replace(self._newLine, "", 1)
                txt_pagesTemplateHead = txt_pagesTemplateHead + self._newLine + self._newLine
            self._writeFileAndOverwrite(os.path.join(self.__path_folder_wrapper, "Pages_%s.py" % (self._UtilString.capitalizeFirstLetter(self.scriptFolderName))), txt_pagesTemplateHead + txt_PagesBodyHead + txt_existed_pagesTemplateBodyBody)
        except:
            return

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