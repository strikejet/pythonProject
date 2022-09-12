# when we want to skip test for some functions in program

import unittest


def add(num1, num2):
    return num1 + num2


def sub(num1,num2):
    return num1 - num2


class SkipIt(unittest.TestCase):
    def testcheckadd(self):
        self.assertEquals(add(10, 20), 30)

    @unittest.skip("skipping the sub method")    # moderator to skip
    def testchecksub(self):                       # this method is ignored
        self.assertEquals(sub(40, 30), 10)


if __name__ == "__main__":
    unittest.main()