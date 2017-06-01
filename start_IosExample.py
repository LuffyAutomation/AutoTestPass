# coding: utf-8
from projects.IosExample.cases.IosExample import IosExample

import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(IosExample("test_flow"))
    suite.addTest(IosExample("test_your_other_flow"))

    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

