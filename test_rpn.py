#!/usr/bin/env python3
import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate( '1 1 +')
        self.assertEqual(result,2)
    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(result,1)
    def test_mul(self):
        result = rpn.calculate('4 3 *')
        self.assertEqual(result,12)
    def test_div(self):
        result = rpn.calculate('9 3 /')
        self.assertEqual(result,3)
    def test_chain(self):
        result = rpn.calculate('1 1 + 2 *')
        self.assertEqual(result,4)