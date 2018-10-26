import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate( '1 1 +')
        self.assertEqual(result,2)
    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(result,1)