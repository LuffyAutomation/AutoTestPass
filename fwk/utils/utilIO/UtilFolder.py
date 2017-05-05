# coding: utf-8
import os
import shutil
import time


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
    def isPathExists(p):
           return os.path.exists(p)

    class FolderMode:
        LIST_SUB_FOLDER_NAMES = "LIST_SUB_FOLDER_NAMES"
        LIST_SUB_FILE_NAMES = "LIST_SUB_FOLDER_NAMES"

    @staticmethod
    def walkFolder(p, folderMode=FolderMode.LIST_SUB_FOLDER_NAMES):
        for parent, list_subFolderName, list_subfileName in os.walk(p):
            if folderMode == UtilFolder.FolderMode.LIST_SUB_FOLDER_NAMES:
                return list_subFolderName
            elif folderMode == UtilFolder.FolderMode.LIST_SUB_FILE_NAMES:
                return list_subfileName
            for dirname in list_subFolderName:
                pass
                for filename in list_subfileName:
                    os.path.join(parent, filename)
                    pass
