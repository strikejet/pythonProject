# test suite is collection of test cases

import unittest

# you must use use setUp for declaring variables to test within the class


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.num1 = 10
        self.num2 = 20

    def testadd(self):
        result = self.num1 + self.num2
        self.assertTrue(result == 30)

    def testsub(self):
        result = self.num1 - self.num2
        self.assertTrue(result == -10)


def suite():
    test_suite = unittest.TestSuite()   # naming of test suite
    test_suite.addTest(unittest.makeSuite(ConfigTestCase))   # creating of test suite
    return test_suite


myCreatedSuit = suite()
runner = unittest.TextTestRunner()
runner.run(myCreatedSuit)

