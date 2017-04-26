import os
from src.base.fwk.AndroidFramework import Android

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidPortal(Android):

    def __init__(self):
        Android.__init__(self)

    def getProjectName(self):
        # return PATH("").split("\\")[-1]
        # in DP > '/apktest/86b3fded428245ec977cb63f8a752f9d/python-work-4df1517a21454fb7/src/project/PrinterControl' will fail
        return PATH("").split(os.path.sep)[-1]

    def getProjectPath(self):
        return PATH("")
