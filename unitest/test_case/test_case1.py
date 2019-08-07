# coding = utf-8
import unittest


class mytest(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_case1(self):
        print('test_case1')

    def test_case2(self):
        print('test_case2')

    def test_case3(self):
        print('test_case3')


def suitcase():
    suittest = unittest.TestSuite()
    suittest.addTest(mytest('test_case1'))
    suittest.addTest(mytest('test_case2'))
    return suittest


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suitcase())
