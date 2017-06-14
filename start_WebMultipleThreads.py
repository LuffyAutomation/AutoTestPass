# coding: utf-8
from projects.WebMultipleThreads.cases.WebMultipleThreads import WebMultipleThreads

import unittest
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(WebMultipleThreads("test_flow"))
    suite.addTest(WebMultipleThreads("test_your_other_flow"))

    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

