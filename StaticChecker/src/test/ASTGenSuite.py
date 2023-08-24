import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test301(self):
        input = """
        struct test
        {
            int a, b;
            test()
            {
                this->a = 0;
                this->b = 0;
            }
        };
        struct test1
        {
            float a, b;
            test1()
            {
                this->a = 0;
                this->b = 0;
            }
        };
        void main()
        {
            struct test a = new test();
            printInteger(a.c);
            printString("Hello World!");
        }"""
        output = ""
        self.assertTrue(TestAST.test(input, output, 301))