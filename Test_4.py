from fun_for_Test4 import mul, div
import unittest


class Checkclass(unittest.TestCase):
    def testmul(self):
        self.assertEquals(mul(5, 6), 30)

    def testdiv(self):
        self.assertEquals(div(15, 3), 14)


if __name__ == "__main__":
    unittest.main()
