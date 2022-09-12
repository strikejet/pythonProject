# we need module "unittestingpython" for testing the program
# UNIT TEST
# this will carry out all tests in program and it will not terminate if one test is failed

import unittest


def add(num1, num2):
    return num1 + num2


def sub(num1,num2):
    return num1 - num2

# STEP1 -- create a class :cannot be done without class
# step2 -- logic -- method __ method should be created in class for testing
# step3 -- inherit Unittest class for the testing class
# step4 -- assertionEquals(what doo you need to check, answer you want )
# ***note -- we cannot create object from a class which is inherited from UNittest class
# step5 -- calling -- should be done from main class -- unittest.main()
# step6 -- Test method name must start with prefix "test" word


class CheckAddfunction(unittest.TestCase):
    def testcheckadd(self):                     #this naem should start with test
        self.assertEquals(add(10, 20), 30)

    def testchecksub(self):
        self.assertEquals(sub(40, 30), 10)

# obj = CheckAddfunction()  # can not be done


if __name__ == "__main__":
    unittest.main()
    