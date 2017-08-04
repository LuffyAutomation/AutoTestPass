import inspect

class UtilCode:
         # decode                 encode
    # str - --------> unicode - -------->str
    class CodeType:
        UTF8 = 'utf-8'
    @staticmethod
    def encode(value):
        try:
            if type(value).__name__ == "unicode":
                return value.encode(UtilCode.CodeType.UTF8)
        except:
            return value


