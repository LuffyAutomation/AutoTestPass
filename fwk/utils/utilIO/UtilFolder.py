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
    def delete_file_folder(src):
        # os.removedirs（r"c:\python"）
        if os.path.isfile(src):
            os.remove(src)
        elif os.path.isdir(src):
            for item in os.listdir(src):
                item_src = os.path.join(src, item)
                UtilFolder.delete_file_folder(item_src)
                os.rmdir(src)

    @staticmethod
    def copy_folder(o_folder, dst):
        shutil.copytree(o_folder, dst)

    @staticmethod
    def create_folder(p_folder):
        if not os.path.isdir(p_folder):
            os.makedirs(p_folder)
            time.sleep(0.5)

    @staticmethod
    def get_path_from_url(p):
        return os.path.dirname(p)

    @staticmethod
    def get_name_from_url(p):
        return os.path.basename(p)

    @staticmethod
    def get_url_tuple(p):
        return os.path.splitext(p)

    @staticmethod
    def is_path_existing(p):
        return os.path.exists(p)

    class DoMode:
        LIST_SUB_FOLDER_NAMES = "LIST_SUB_FOLDER_NAMES"
        LIST_SUB_FILE_NAMES = "LIST_SUB_FILE_NAMES"
        DEL_SPECIFIED = "DEL_SPECIFIED"

    @staticmethod
    def walk_folder(p, folder_access_mode=DoMode.LIST_SUB_FOLDER_NAMES, list_names=[]):
        for folder_path, list_sub_folder_name, list_sub_file_name in os.walk(p):
            if folder_access_mode == UtilFolder.DoMode.LIST_SUB_FOLDER_NAMES:
                return list_sub_folder_name
            elif folder_access_mode == UtilFolder.DoMode.DEL_SPECIFIED:
                for subFolderName in list_sub_folder_name:
                    UtilFolder.remove_specified_file_or_folder(os.path.join(folder_path, subFolderName), list_names)
                for sub_file_name in list_sub_file_name:
                    UtilFolder.remove_specified_file_or_folder(os.path.join(folder_path, sub_file_name), list_names)
            elif folder_access_mode == UtilFolder.DoMode.LIST_SUB_FILE_NAMES:
                return list_sub_file_name
            # for dirname in list_subFolderName:
            #     pass
            #     for filename in list_subfileName:
            #         os.path.join(folderPath, filename)
            #         pass

    @staticmethod
    def remove_specified_file_or_folder(found_file_or_folder, list_names):
        for i in range(len(list_names)):
            if os.path.isfile(found_file_or_folder) and UtilString.isWildCardMatched(os.path.basename(found_file_or_folder), list_names[i]):
                try:
                    # UtilConsole.printCmdLn(found_file_or_folder)
                    os.remove(found_file_or_folder)
                except Exception as e:
                    UtilConsole.printCmdLn(e.__init__())
            elif os.path.isdir(found_file_or_folder) and UtilString.isWildCardMatched(os.path.basename(found_file_or_folder), list_names[i]):
                try:
                    # UtilConsole.printCmdLn(found_file_or_folder)
                    os.removedirs(found_file_or_folder)
                except Exception as e:
                    UtilConsole.printCmdLn(e.__init__())

  # for idx in range(len(description)):