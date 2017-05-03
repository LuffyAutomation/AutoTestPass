import inspect

class UtilClass:
    @staticmethod
    def getCurrentFunctionName():
        return inspect.stack()[0][3]
        # return sys._getframe().f_code.co_name


