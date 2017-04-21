import locale
import platform
import os


class UtilOS:

    class OSLauguages:
        ENU = "en_US"

    def __init__(self, *args):
        pass

    @staticmethod
    def getOSLocale():  # not work in DP
        return locale.getdefaultlocale()[0]

    @staticmethod
    def getOSName():  # "Linux, Windows, Darwin"
        s = platform.system()
        if s == "Windows":
            return "Win"
        elif s == "Darwin":
            return "Mac"
        return s

    @staticmethod
    def getOSVersion():  # not work in DP
        return platform.version() # '6.1.7601'

    @staticmethod
    def getOSRelease():
        return platform.release() # 7

    @staticmethod
    def getOSBit():
        if UtilOS.getOSName() == "Windows":  # 32bit Python always return 32bit no matter 32bit or 64bit os.
            if 'PROGRAMFILES(X86)' in os.environ:
                return "64bit"
            return "32bit"
        else:
            return platform.architecture()[0]

    @staticmethod
    def getOSNameVersion():
        return platform.platform() # 'Windows-7-6.1.7601-SP1

    # {(6, 0): 'Vista', (6, 2): '8', (5, 1): 'XP', (10, None): 'post10', (5, None): 'post2003', (6, 1): '7',
    #  (6, 3): '8.1', (5, 0): '2000', (10, 0): '10', (6, None): 'post8.1', (5, 2): '2003Server'}

    @staticmethod
    def getCPU(): # 'x86_64' 'AMD64'
        return platform.machine()