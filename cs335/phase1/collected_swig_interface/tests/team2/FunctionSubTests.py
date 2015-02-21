from Function import *
import Function
import unittest
from random import randint

class FunctionSubTests(unittest.TestCase):
  """Test + overloads"""
  def testSub(self):
    g = Function.Function_xn(4)+Function.Function_xn(3)+Function.Function_xn(2)+Function.Function_xn(1)
    for x in range (2,11):      
      r = randint(2,x)
      t = Function.Function_xn(randint(1,4))
      self.assertAlmostEquals(g.evaluate(r)-t.evaluate(r),(g-t).evaluate(r), delta=1e-12)
    for y in range (2,11):
      r = randint(2,x)
      t = randint(1,15)
      self.assertAlmostEquals(g.evaluate(r)-t,(g-t).evaluate(r), delta=1e-12)
    for i in range (2,11):
      r = randint(2,x)
      t = randint(1,15)
      self.assertAlmostEquals(t-g.evaluate(r),(t-g).evaluate(r), delta=1e-12)

if (__name__ == '__main__'):
  unittest.main()
