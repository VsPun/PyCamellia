from Function import *
import Function
import unittest
from random import randint

class FunctionMulTests(unittest.TestCase):
  """Test + overloads"""
  def testMul(self):
    g = Function.Function_xn(4)+Function.Function_xn(3)+Function.Function_xn(2)+Function.Function_xn(1)
    for x in range (2,11):      
      r = randint(2,x)
      t = Function.Function_xn(randint(1,4))
      self.assertAlmostEquals(g.evaluate(r)*t.evaluate(r),(g*t).evaluate(r), delta=1e-12)
    for y in range (2,11):
      r = randint(2,x)
      t = randint(1,15)
      self.assertAlmostEquals(g.evaluate(r)*t,(g*t).evaluate(r), delta=1e-12)
    for i in range (2,11):
      r = randint(2,x)
      t = randint(1,15)
      self.assertAlmostEquals(t*g.evaluate(r),(t*g).evaluate(r), delta=1e-12)
    forwardTest = Function.Function_xn(2)
    sol = forwardTest * Function.DoubleVector(2,2.0)
    self.assertAlmostEqual(8 ,sol.x().evaluate(2), delta=1e-12)
    backwardTest = Function.Function_xn(2)
    sol = Function.DoubleVector(2,2.0) * backwardTest
    self.assertAlmostEqual(8 ,sol.x().evaluate(2), delta=1e-12)

if (__name__ == '__main__'):
  unittest.main()
