#!/usr/bin/env python3
import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        y = []
        result = rpn.calculate("1 1 +",y)
        self.assertEqual(2, result)
    def test_subtract(self):
        y = []
        result = rpn.calculate("5 3 -",y)
        self.assertEqual(2, result)
    def test_multiply(self):
        y = []
        result = rpn.calculate("5 3 *",y)
        self.assertEqual(15, result)
    def test_divide(self):
        y = []
        result = rpn.calculate("6 3 /",y)
        self.assertEqual(2, result)
    def test_exponent(self):
        y = []
        result = rpn.calculate("2 3 ^",y)
        self.assertEqual(8,result)
