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
    class FileMode:
        R = "r"
        W = "w"
        RB = "rb"
        WB = "wb"
        RT = "rt"
        WT = "wt"
        RB_PLUS = "rb+"
        WB_PLUS = "wb+"

    def __init__(self, *args):
        pass

    @staticmethod
    def deleteFile(path_file):
        os.remove(path_file)

    @staticmethod
    def writeFile(path_file, txt, file_mode=FileMode.W):
        with open(path_file, file_mode) as f:
            f.write(txt)

    @staticmethod
    def isPathExists(p):
           return os.path.exists(p)

    @staticmethod
    def copyFile(o_file, dst):
        if os.path.isfile(o_file):
            shutil.copyfile(o_file, dst)
