# coding: utf-8
import os
import shutil
import time
from fwk.utils.utilConsole.UtilConsole import UtilConsole
from fwk.utils.utilString.UtilString import UtilString


class UtilFolder:
    def __init__(self, *args):
        pass

    @staticmethod
    def deleteFileFolder(src):
     #os.removedirs（r"c:\python"）
     if os.path.isfile(src):
         os.remove(src)
     elif os.path.isdir(src):
        for item in os.listdir(src):
            itemSrc = os.path.join(src, item)
            UtilFolder.delete_file_folder(itemSrc)
            os.rmdir(src)

    @staticmethod
    def copyFolder(o_folder, dst):
        shutil.copytree(o_folder, dst)

    @staticmethod
    def createFolder(p_folder):
       if not os.path.isdir(p_folder):
           os.makedirs(p_folder)
           time.sleep(0.5)

    @staticmethod
    def getPathFromURL(p):
           return os.path.dirname(p)

    @staticmethod
    def getNameFromURL(p):
           return os.path.basename(p)

    @staticmethod
    def getUrlTuple(p):
           return os.path.splitext(p)

    @staticmethod
    def isPathExisting(p):
           return os.path.exists(p)

    class DoMode:
        LIST_SUB_FOLDER_NAMES = "LIST_SUB_FOLDER_NAMES"
        LIST_SUB_FILE_NAMES = "LIST_SUB_FILE_NAMES"
        DEL_SPECIFIED = "DEL_SPECIFIED"

    @staticmethod
    def walkFolder(p, folderMode=DoMode.LIST_SUB_FOLDER_NAMES, list_names=[]):
        for folderPath, list_subFolderName, list_subfileName in os.walk(p):
            if folderMode == UtilFolder.DoMode.LIST_SUB_FOLDER_NAMES:
                return list_subFolderName
            elif folderMode == UtilFolder.DoMode.DEL_SPECIFIED:
                for subFolderName in list_subFolderName:
                    UtilFolder.removeSpecified(os.path.join(folderPath, subFolderName), list_names)
                for subfileName in list_subfileName:
                    UtilFolder.removeSpecified(os.path.join(folderPath, subfileName), list_names)
            elif folderMode == UtilFolder.DoMode.LIST_SUB_FILE_NAMES:
                return list_subfileName
            # for dirname in list_subFolderName:
            #     pass
            #     for filename in list_subfileName:
            #         os.path.join(folderPath, filename)
            #         pass

    @staticmethod
    def removeSpecified(foundFileOrFolder, list_names):
        for i in range(len(list_names)):
            if os.path.isfile(foundFileOrFolder) and UtilString.isWildCardMatched(os.path.basename(foundFileOrFolder), list_names[i]):
                try:
                    # UtilConsole.printCmdLn(foundFileOrFolder)
                    os.remove(foundFileOrFolder)
                except Exception as e:
                    UtilConsole.printCmdLn(e.__init__())
            elif os.path.isdir(foundFileOrFolder) and UtilString.isWildCardMatched(os.path.basename(foundFileOrFolder), list_names[i]):
                try:
                    # UtilConsole.printCmdLn(foundFileOrFolder)
                    os.removedirs(foundFileOrFolder)
                except Exception as e:
                    UtilConsole.printCmdLn(e.__init__())
        pass


  # for idx in range(len(description)):