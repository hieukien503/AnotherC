import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test301(self):
        input = """struct test
        {
            
        };
        void foo(struct test x)
        {
            
        }
        void main()
        {
            
        }
        """
        output = """"""
        self.assertTrue(TestAST.test(input, output, 301))