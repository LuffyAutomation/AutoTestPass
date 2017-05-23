import os

from fwk.utils.utilIO.UtilFile import UtilFile
from fwk.utils.utilIO.UtilFolder import UtilFolder
from fwk.utils.utilString.UtilString import UtilString
from fwk.utils.exceller.Exceller import Exceller
from fwk.utils.utilXml.UtilXml import UtilXml


class TestDataStringsCreator(object):
    def __init__(self, path_folder_testData, path_folder_strings, isGeneratedInProject=True):
        self._UtilFolder = UtilFolder
        self._UtilFile = UtilFile
        self._UtilString = UtilString
        self._UtilXml = UtilXml
        self.scriptFolderName = path_folder_testData.split("data" + os.path.sep)[1].split(os.path.sep)[0]
        self. __isGeneratedInProject = isGeneratedInProject

        self._newLine = "\n"
        self._indent = "    "
        self._descriptionWrapper = "'''"

        self.__path_folder_testData = path_folder_testData
        self.__path_folder_strings = path_folder_strings

    def __getTestType(self):
        if self.scriptFolderName.lower() == "android":
            return "TestData_Android"
        elif self.scriptFolderName.lower() == "web":
            return "TestData_Web"
        elif self.scriptFolderName.lower() == "ios":
            return "TestData_ios"

    def create(self):
        try:
            self.DictTestDataOfAllSheets = Exceller(self.__path_folder_testData, None).getDictTestDataOfAllWorkSheets()
            if self.DictTestDataOfAllSheets is None:
                return
        except:
            return
        self._DictSheetName = self.DictTestDataOfAllSheets.keys()
        tmp = "# coding: utf-8" + self._newLine + self._newLine + self._newLine
        tmp += "class %s:" % self.__getTestType() + self._newLine
        for page_key in self.DictTestDataOfAllSheets:
            tmp += self._indent + "def __init__(self, UI):" + self._newLine
            for name_sheet in self._DictSheetName:
                tmp += self._indent + self._indent + "self.%s = self._%s(UI)" % (UtilString.toCodeNameCap(name_sheet), UtilString.toCodeNameCap(name_sheet)) + self._newLine
            tmp += self._indent + "# sheet name: [%s]" % (page_key) + self._newLine
            tmp += self._indent + "class _%s:" % UtilString.toCodeNameCap(page_key) + self._newLine
            tmp += self._indent + self._indent + "def __init__(self, UI):" + self._newLine
            tmp += self._indent + self._indent + self._indent + "self.UI = UI" + self._newLine
            for testData_string in self.DictTestDataOfAllSheets[page_key]:
                t = self.DictTestDataOfAllSheets[page_key][testData_string]
                tmp += self._newLine + self._indent + self._indent + "# ID: [%s] value:[%s]" % (UtilString.toCodeName(testData_string), t) + self._newLine
                tmp += self._indent + self._indent + "def %s(self):" % UtilString.toCodeName(testData_string) + self._newLine
                tmp += self._indent + self._indent + self._indent + ("return self.UI.getTestData('%s')" % testData_string) + self._newLine
            self._writeFileAndOverwrite(os.path.join(self.__path_folder_strings, self.__getTestType() + ".py"), tmp)

    def _writeFileAndOverwrite(self, path_file, txt=""):
            UtilFile.writeFile(path_file, txt, self._UtilFile.FileMode.W)
