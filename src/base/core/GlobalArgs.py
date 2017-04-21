from src.utils.utilTime.UtilTime import UtilTime


class GlobalArgs:
    __GLOBAL_START_TIME = UtilTime.getCurrentTime()
    __global_testSuiteNum = 0
    __path_xml_result = ""

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
