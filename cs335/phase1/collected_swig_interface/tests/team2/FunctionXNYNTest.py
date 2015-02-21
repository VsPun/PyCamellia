from Function import *
import Function
import unittest

class FunctionXNYNTest(unittest.TestCase):
  """Test xn  and yn"""
  def testXNYN(self):
    x3 = Function.Function_xn(3)
    self.assertAlmostEquals(27, x3.evaluate(3,2), delta=1e-12)
    y2 = Function.Function_yn(2)
    self.assertAlmostEquals(4, y2.evaluate(3,2), delta=1e-12)
    g2 = x3 + y2
    self.assertAlmostEquals(31, g2.evaluate(3,2), delta=1e-12)


if (__name__ == '__main__'):
  unittest.main()
