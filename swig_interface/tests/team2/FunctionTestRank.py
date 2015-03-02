from Function import *
import Function
import unittest
import math

class FunctionTestRank(unittest.TestCase):
  def testRank(self):
    #Create Functions
    x3 = Function.Function_xn(3)
    y4 = Function.Function_yn(4)
    c4 = Function.Function_constant(4.0)
    #Take Derivatives
    dxx3 = x3.dx()
    dyx3 = x3.dy()
    dxy4 = y4.dx()
    dyy4 = y4.dy()
    dxc4 = c4.dx()
    dyc4 = c4.dy()
    #Utilize Functions
    sum = x3+y4
    vector = Function.Function_vectorize(dxx3,dyy4)
    gradient = sum.grad()
    composed = Function.Function_composedFunction(sum,gradient)
    diverg = gradient.div()

    #Check Ranks
    self.assertEqual(x3.rank(),0,"x3 rank is not 0")
    self.assertEqual(y4.rank(),0,"y4 rank is not 0")   
    self.assertEqual(c4.rank(),0,"c4 rank is not 0")   
    self.assertEqual(sum.rank(),0,"sum rank is not 0")
    self.assertEqual(vector.rank(),1,"vector rank is not 1")
    self.assertEqual(gradient.rank(),1,"gradient rank is not 1")
    self.assertEqual(diverg.rank(),0,"diverg rank is not 1")

if (__name__ == '__main__'):
  unittest.main()
