import unittest
from test_case1 import mytest
import os
import datetime

#now_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(now)
report_dir = 'F:\\unitest\\report'


def suitcase():
    suittest = unittest.TestSuite()
    suittest.addTest(unittest.makeSuite(mytest))

    return suittest


if __name__ == '__main__':

    from BeautifulReport import BeautifulReport as bf

    runner = bf(suitcase())
    runner.report(filename=filename, description="测试报告", report_dir=report_dir)
