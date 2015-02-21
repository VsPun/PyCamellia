from Function import *
import Function
import unittest
import math

class FunctionTestInstance(unittest.TestCase):
  def testInstance(self):
    x3 = Function.Function_xn(3)
    #test xn rank
    self.assertEqual(x3.rank(),0,"x3 rank is not 0")
    y4 = Function.Function_yn(4)
    #test yn rank
    self.assertEqual(y4.rank(),0,"y4 rank is not 0")
    c4 = Function.Function_constant(4.0)
    #test const rank
    self.assertEqual(y4.rank(),0,"y4 rank is not 0")
    #test evaluate on xn yn and const
    for i in range (0,10):
        self.assertAlmostEquals(c4.evaluate((10+i),i),4.0,delta=1e-12)
        self.assertAlmostEquals(x3.evaluate((10+i),i),math.pow(10+i,3),delta=1e-12)
        self.assertAlmostEquals(y4.evaluate((10+i),i),math.pow(i,4),delta=1e-12)
    
    dxx3 = x3.dx()
    dyx3 = x3.dy()
    dxy4 = y4.dx()
    dyy4 = y4.dy()
    dxc4 = c4.dx()
    dyc4 = c4.dy()
    #test evaluate on dy and dx
    for i in range (0,10):
        self.assertAlmostEquals(dxx3.evaluate(i,i),3*math.pow(i,2),delta=1e-12)
        self.assertAlmostEquals(dyx3.evaluate(i,i),0,delta=1e-12)
        self.assertAlmostEquals(dxy4.evaluate(i,i),0,delta=1e-12)
        self.assertAlmostEquals(dyy4.evaluate(i,i),4*math.pow(i,3),delta=1e-12)
        self.assertAlmostEquals(dxc4.evaluate(i,i),0,delta=1e-12)
        self.assertAlmostEquals(dyc4.evaluate(i,i),0,delta=1e-12)
    sum = x3+y4
    #test rank after summation
    self.assertEqual(sum.rank(),0,"sum rank is not 0")
    vector = Function.Function_vectorize(dxx3,dyy4)
    gradient = sum.grad()
    #test rank of vectorize and gradient
    self.assertEqual(vector.rank(),1,"vector rank is not 1")
    self.assertEqual(gradient.rank(),1,"gradient rank is not 1")

    #test evaluate of x and y components of vectors
    for i in range (0,10):
        self.assertAlmostEquals(vector.x().evaluate(i,i),dxx3.evaluate(i,i),delta = 1e-12)
        self.assertAlmostEquals(gradient.x().evaluate(i,i),dxx3.evaluate(i,i),delta = 1e-12)
        self.assertAlmostEquals(vector.y().evaluate(i,i),dyy4.evaluate(i,i),delta = 1e-12)
        self.assertAlmostEquals(gradient.y().evaluate(i,i),dyy4.evaluate(i,i),delta = 1e-12)

    #test composition of functions
    composed = Function.Function_composedFunction(sum,gradient)
    for i in range (0,10):
        self.assertAlmostEquals(composed.evaluate(i,i),sum.evaluate((3*math.pow(i,2)),(4*math.pow(i,3))),delta = 1e-12)

    #test divergence
    diverg = gradient.div()
    for i in range(0,10):
      self.assertAlmostEquals(diverg.evaluate(i+1,i),dxx3.dx().evaluate(i+1,i)+dyy4.dy().evaluate(i+1,i),delta = 1e-12)
    
    


if (__name__ == '__main__'):
  unittest.main()
