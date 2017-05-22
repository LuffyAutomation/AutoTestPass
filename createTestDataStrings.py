import os
from fwk.base.InitFwk import InitFwk
from fwk.utils.testDataStringsCreator.TestDataStringsCreator import TestDataStringsCreator

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def create():
    # project is defined in env>main.conf>[DefaultProject].
    _InitFwk = InitFwk()
    _TestDataStringsCreator = TestDataStringsCreator(_InitFwk.path_file_xlsx_testData_android, _InitFwk.path_folder_xlsx_strings_android)
    _TestDataStringsCreator.create()
    _TestDataStringsCreator = TestDataStringsCreator(_InitFwk.path_file_xlsx_testData_ios, _InitFwk.path_folder_xlsx_strings_ios)
    _TestDataStringsCreator.create()
    _TestDataStringsCreator = TestDataStringsCreator(_InitFwk.path_file_xlsx_testData_web, _InitFwk.path_folder_xlsx_strings_web)
    _TestDataStringsCreator.create()

if __name__ == '__main__':
    create()

