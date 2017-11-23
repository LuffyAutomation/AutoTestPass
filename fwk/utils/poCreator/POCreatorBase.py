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
        self._UtilFolder.create_folder(self.__path_folder_pages)
        self._writeFile(os.path.join(self.__path_folder_pages, "__init__.py"))
        self.__path_folder_models = os.path.join(path_folder_po, self._PO_MODELS, self.scriptFolderName)
        self._UtilFolder.create_folder(self.__path_folder_models)
        self._writeFile(os.path.join(self.__path_folder_models, "__init__.py"))
        self.__path_folder_wrapper = os.path.join(path_folder_po, self._PO_WRAPPER)
        self._UtilFolder.create_folder(self.__path_folder_wrapper)
        self._writeFile(os.path.join(self.__path_folder_wrapper, "__init__.py"))
        self._writeFile(os.path.join(self.__path_folder_wrapper, "Pages_Android.py"))
        self._writeFile(os.path.join(self.__path_folder_wrapper, "Pages_Web.py"), "class Pages_Web: pass")
        self._writeFile(os.path.join(self.__path_folder_wrapper, "Pages_Ios.py"), "class Pages_Ios: pass")
        self.__path_folder_po = path_folder_po
        self.__path_folder_uiMaps = path_folder_uiMaps

        self.__xmlTree = self._UtilXml.get_tree(self.__path_folder_uiMaps)
        self._root = self._UtilXml.get_root_element(self.__xmlTree)

        self.__class_import_string_head = self.__getClassImportStringHead()

    def create(self):
        try:
            list_element = self._UtilXml.get_elements(self._root, ".//pages/")
        except:
            return
        list_pages_template_head = []
        pages_template_head = ""
        list_pages_template_body_body = []
        pages_template_body_body = ""
        for index in range(len(list_element)):
            attributes = self._UtilXml.get_attributes_list(list_element[index])
            children = self._UtilXml.get_children(list_element[index])
            name = attributes.get(self.uiMapMarks.NAME)
            pages_template_head += self._getPagesClassImportString(name)
            list_pages_template_head.append(self._getPagesClassImportString(name))
            pages_template_body_body += self._getPagesBodyBody(name)
            list_pages_template_body_body.append(self._getPagesBodyBody(name))
            description = attributes.get(self.uiMapMarks.DESCRIPION)
            self._writeFile(os.path.join(self.__path_folder_pages, self._getPOFileName(name)), self._getPOHead(name, description))
            _pOModelHead = self._getPOModelHead(name, None, description)
            _pOModelHeadSubClass = ""
            list_subClass = []
            _po_model_model_body = ""
            _po_model_sub_model_body = ""
            for idx in range(len(children)):
                level = 0
                children_name = self._UtilXml.get_attributes_list(children[idx]).get(self.uiMapMarks.NAME)
                if self._UtilXml.get_tag_name(children[idx]) == self.uiMapMarks.PAGE:
                    level += 1
                    list_subClass.append(children_name)
                    children_description = self._UtilXml.get_attributes_list(children[idx]).get(self.uiMapMarks.DESCRIPION)
                    children_children = self._UtilXml.get_children(children[idx])
                    _pOModelHeadSubClass += self._getPOModelHead(name, children_name, children_description, level)
                    for c_idx in range(len(children_children)):
                        children_children_name = self._UtilXml.get_attributes_list(children_children[c_idx]).get(self.uiMapMarks.NAME)
                        _po_model_sub_model_body += self._getPOModelBody(children_children_name, level)
                    _pOModelHeadSubClass += _po_model_sub_model_body
                    _po_model_sub_model_body = ""
                else:
                    _po_model_model_body += self._getPOModelBody(children_name, 0)
            _pOModelHead += self._getPOModelHeadSubClass(list_subClass, level)
            tmpStr = _pOModelHead + _po_model_model_body + _pOModelHeadSubClass + _po_model_sub_model_body
            self._writeFileAndOverwrite(os.path.join(self.__path_folder_models, self._getPOModelFileName(name)), tmpStr)
        self._writePagesFile(os.path.join(self.__path_folder_wrapper, "Pages_%s.py" % (self._UtilString.capitalizeFirstLetter(self.scriptFolderName))), list_pages_template_head, self._getPagesBodyHead(), list_pages_template_body_body)

    def __getClassImportStringHead(self):
        if self.__isGeneratedInProject == True:
            # tmp_path = self.__IMPORT_STRING_BEGIN_WITH + self.__path_folder_po.split(self.__IMPORT_STRING_BEGIN_WITH)[1]
            tmp_path = self.__IMPORT_STRING_BEGIN_WITH + self.__path_folder_po.split(self.__IMPORT_STRING_BEGIN_WITH)[1]
            self.__class_import_string_head = "from " + tmp_path.replace("/", ".").replace("\\", ".")
            return self.__class_import_string_head

    def _getPOModelClassImportString(self, po_name):
        po_name = self._getPOClassName(po_name)
        class_import_string = self.__class_import_string_head
        po_model_class_name = self._getPOModelClassName(po_name)
        if self._COMMONPAGE not in po_model_class_name:
            class_import_string += "." + self._PO_MODELS
            class_import_string += "." + self.scriptFolderName
        tmp = "# coding: utf-8" + self._newLine
        # tmp = "import inspect" + self._newLine
        return tmp + "%s.%s import %s" % (class_import_string, po_model_class_name, po_model_class_name)

    def _getPagesClassImportString(self, po_name):
        po_name = self._getPOClassName(po_name)
        class_import_string = self.__class_import_string_head
        # pOModelClassName = self._getPOModelClassName(po_name)
        class_import_string += "." + self._PO_PAGES + "." + self.scriptFolderName
        return "%s.%s import %s" % (class_import_string, po_name, po_name) + self._newLine

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
        if not self._UtilFile.is_path_existing(path_file):
            self._UtilFile.write_file(path_file, txt, self._UtilFile.FileMode.W)

    def _writeFileAndOverwrite(self, path_file, txt=""):
        self._UtilFile.write_file(path_file, txt, self._UtilFile.FileMode.W)

    def _writePagesFile(self, path_file, list_pagesTemplateHead, txt_PagesBodyHead, list_pages_template_body_body):
        # global lines, list_existed_pages_template_head, list_existed_pages_template_body_body, part
        lines = []
        list_existed_pages_template_head = []
        list_existed_pages_template_body_body = []
        part = 1
        try:
            lines = self._UtilFile.get_lines_from_file(path_file)
            for line in lines:
                if part == 3:
                    list_existed_pages_template_body_body.append(line)
                if "class Pages_" in line:
                    part = 2
                elif "self._UI = UI" in line:
                    part = 3
                if part == 1:
                    list_existed_pages_template_head.append(line)

            for line in list_pagesTemplateHead:
                if line not in list_existed_pages_template_head:
                    list_existed_pages_template_head.insert(list_existed_pages_template_head.__len__() - 2, line)  # make it befort /n /n
            # make a new one below the old one avoid duplicate name
            # from projects.WebMultipleThreads.po.pages.web.Page_home import Page_home
            # from projects.WebSingle.po.pages.web.Page_home import Page_home

            for line in list_pages_template_body_body:
                if line not in list_existed_pages_template_body_body:
                    list_existed_pages_template_body_body.insert(0, line)

            txt_pages_template_head = "".join(list_existed_pages_template_head)
            txt_existed_pages_template_body_body = "".join(list_existed_pages_template_body_body)
            if not txt_pages_template_head.endswith(self._newLine + self._newLine):
                # txt_PagesBodyHead = txt_PagesBodyHead.replace(self._newLine, "", 1)
                txt_pages_template_head = txt_pages_template_head + self._newLine + self._newLine
            self._writeFileAndOverwrite(os.path.join(self.__path_folder_wrapper, "Pages_%s.py" % (self._UtilString.capitalizeFirstLetter(self.scriptFolderName))), txt_pages_template_head + txt_PagesBodyHead + txt_existed_pages_template_body_body)
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