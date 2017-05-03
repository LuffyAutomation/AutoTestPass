from fwk.utils.utilTime.UtilTime import UtilTime


class GlobalArgs:
    __GLOBAL_START_TIME = UtilTime.getCurrentTime()
    __global_testSuiteNum = 0
    __path_xml_result = ""
    __name_project = ""
    __path_project = ""
    @staticmethod
    def getGlobalStartTime():
        return GlobalArgs.__GLOBAL_START_TIME

    @staticmethod
    def getGlobalTestSuiteNum():
        GlobalArgs.__global_testSuiteNum += 1
        #return GlobalArgs.__global_testSuiteNum
        # testSuiteNum += 1
        return "%05d" % GlobalArgs.__global_testSuiteNum

    @staticmethod
    def setPathXmlResult(path):
        GlobalArgs.__path_xml_result = path

    @staticmethod
    def getPathXmlResult():
        return GlobalArgs.__path_xml_result

    @staticmethod
    def setProjectName(name_project):
        GlobalArgs.__name_project = name_project

    @staticmethod
    def setProjectPath(path_project):
        GlobalArgs.__path_project = path_project

    @staticmethod
    def getProjectName():
        return GlobalArgs.__name_project

    @staticmethod
    def getProjectPath():
        return GlobalArgs.__path_project

# __GLOBAL_START_TIME = UtilTime.getCurrentTime()
# global_testSuiteNum = 0
#
#
# def getTestSuiteNum():
#     global global_testSuiteNum
#     global_testSuiteNum += 1
#     return global_testSuiteNum
#     # testSuiteNum += 1
#     # return "_%05d" % testSuiteNum
#
# def getStartPyTime():
#     return __GLOBAL_START_TIME
