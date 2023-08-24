import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):
    def test401(self):
        input = """
        const int a = 8;
        void main()
        {
            int b = a++;
        }"""
        output = ""
        self.assertTrue(TestChecker.test(input, output, 401))