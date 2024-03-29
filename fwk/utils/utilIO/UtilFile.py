# coding: utf-8
import os
import shutil


class UtilFile:
    # "r"   以读方式打开，只能读文件 ， 如果文件不存在，会发生异常
    # "w" 以写方式打开，只能写文件， 如果文件不存在，创建该文件如果文件已存在，先清空，再打开文件
    # "rb"   以二进制读方式打开，只能读文件 ， 如果文件不存在，会发生异常
    # "wb" 以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件如果文件已存在，先清空，再打开文件
    # "rt"   以文本读方式打开，只能读文件 ， 如果文件不存在，会发生异常
    # "wt" 以文本写方式打开，只能写文件， 如果文件不存在，创建该文件如果文件已存在，先清空，再打开文件
    # "rb+"   以二进制读方式打开，可以读、写文件 ， 如果文件不存在，会发生异常
    # "wb+" 以二进制写方式打开，可以读、写文件， 如果文件不存在，创建该文件如果文件已存在，先清空，再打开文件
    # a 以追加模式打开(从EOF 开始, 必要时创建新文件)

    class FileMode:
        R = "r"
        W = "w"
        RB = "rb"
        WB = "wb"
        RT = "rt"
        WT = "wt"
        RB_PLUS = "rb+"
        WB_PLUS = "wb+"
        A = "a"

    def __init__(self, *args):
        pass

    @staticmethod
    def delete_file(path_file):
        os.remove(path_file)

    @staticmethod
    def write_file(path_file, txt="", file_mode=FileMode.W):
        with open(path_file, file_mode) as f:
            f.write(txt)

    @staticmethod
    def write_file_if_not_exists(path_file, txt="", file_mode=FileMode.W):
        if UtilFile.is_path_existing(path_file):
            return
        with open(path_file, file_mode) as f:
            f.write(txt)

    @staticmethod
    def is_path_existing(p):
           return os.path.exists(p)

    @staticmethod
    def copy_file(o_file, dst):
        if os.path.isfile(o_file):
            shutil.copyfile(o_file, dst)

    @staticmethod
    def rename(o_file, dst):
        if os.path.isfile(o_file):
            os.rename(o_file, dst)

    @staticmethod
    def get_base_name(o_file):
        return os.path.basename(o_file)

    @staticmethod
    def replace_file_content_by_line(path_file, old_text, new_text):
        if os.path.isfile(path_file):
            lines = open(path_file, UtilFile.FileMode.R).readlines()
            with open(path_file, UtilFile.FileMode.W) as f:
                _len = len(lines) - 1
                for i in range(_len):
                    if old_text in lines[i]:
                        lines[i] = lines[i].replace(old_text, new_text)
                f.writelines(lines)

    @staticmethod
    def get_lines_from_file(path_file):
        lines = []
        if os.path.isfile(path_file):
            lines = open(path_file, UtilFile.FileMode.R).readlines()
        return lines

    @staticmethod
    def read_file(path):
        size = 1024
        with open(path, 'r') as f:
            while True:
                block = f.read(size)
                if block:
                    yield block
                else:
                    return
