import re
from fwk.utils.utilTime.UtilTime import UtilTime

class UtilString:
    def __init__(self, *args):
        pass

    @staticmethod
    def capitalizeFirstLetter(f, separator=None, reserveSep=False):
        tmp = ""
        if separator is None:
            return f[0].upper() + f[1:]
        tmpList = f.split(separator)
        for idx in range(len(tmpList)):
            tmp += (tmpList[idx][0].upper() + tmpList[idx][1:])
            if reserveSep is True and idx != len(tmpList):
                tmp += separator
        return tmp

    @staticmethod
    def toCodeName(str):
        str = str.replace(".", "_").strip()
        str = re.sub('[^a-zA-Z_]', '', str)
        if str == "":
            str = "Null" + UtilTime.getCodeTime()
        return re.sub('[^a-zA-Z_]', '', str)

    @staticmethod
    def toCodeNameCap(str):
        return str[0].upper() + str[1:]

    # s = filter(lambda ch: ch in '0123456789', s)
    # print ''.join([x for x in oldS if x.isalpha()])