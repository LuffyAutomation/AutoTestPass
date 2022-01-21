import locale
import platform
import os


class UtilOS:

    class OSLauguages:
        ENU = "en_US"

    def __init__(self, *args):
        pass

    @staticmethod
    def get_os():  # not work in DP
        return UtilOS.get_os_name() + UtilOS.get_os_release() + UtilOS.get_os_bit()

    @staticmethod
    def get_os_locale():  # not work in DP
        return locale.getdefaultlocale()[0]

    @staticmethod
    def get_os_name():  # "Linux, Windows, Darwin"
        s = platform.system()
        if s == "Windows":
            return "Win"
        elif s == "Darwin":
            return "Mac"
        elif s == "Linux":
            return "Linux"
        return s

    @staticmethod
    def get_os_version():  # not work in DP
        return platform.version()  # '6.1.7601'

    @staticmethod
    def get_os_release():
        return platform.release()  # 7

    @staticmethod
    def get_os_bit():
        if UtilOS.get_os_name() == "Windows" or UtilOS.get_os_name() == "Win":  # 32bit Python always return 32bit no matter 32bit or 64bit os.
            if 'PROGRAMFILES(X86)' in os.environ:
                return "x64"
            return "x86"
        else:
		            return platform.architecture()[0]
    @staticmethod
    def get_os_name_version():
        return platform.platform()  # 'Windows-7-6.1.7601-SP1

    # {(6, 0): 'Vista', (6, 2): '8', (5, 1): 'XP', (10, None): 'post10', (5, None): 'post2003', (6, 1): '7',
    #  (6, 3): '8.1', (5, 0): '2000', (10, 0): '10', (6, None): 'post8.1', (5, 2): '2003Server'}

    @staticmethod
    def get_cpu_architecture():  # 'x86_64' 'AMD64'
        return platform.machine()
