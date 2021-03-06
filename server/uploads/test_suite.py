# -*- coding: utf-8 -*-

import unittest
from test import TestCount
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.makeSuite(TestCount, 'test')

    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # suite.addTests(tests)

    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Count Test Report',
                                description='generated by Lancelot.',
                                verbosity=2
                                )
        runner.run(suite)
