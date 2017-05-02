import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ProjectPortal():
    @classmethod
    def getProjectName(cls):
        # return PATH("").split("\\")[-1]
        # in DP > '/apktest/86b3fded428245ec977cb63f8a752f9d/python-work-4df1517a21454fb7/src/project/PrinterControl' will fail
        return PATH("").split(os.path.sep)[-1]

    @classmethod
    def getProjectPath(cls):
        return PATH("")