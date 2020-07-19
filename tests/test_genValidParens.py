import unittest
from src.genValidParens import generateParens

class GenValidParensTestSuite(unittest.TestCase):
    def test1(self):
        self.assertEqual(generateParens(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])