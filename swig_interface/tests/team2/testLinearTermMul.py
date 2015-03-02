from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import Mesh
import MeshFactory
import unittest

class testLinearTermMul(unittest.TestCase):
  """Test LinearTermMul methods"""
  def testLinearTermMul(self):

    # Sets up test variables
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")
    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")

    varFunctions = {test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2}


    #Mul overloads
    funPtr = Function.Function_xn(2)
    ltp = funPtr * test3
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(3,1), 54.0)
    #Function * Var 2x*x^2
    ltp = test3 * funPtr
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(2,1), 16.0)
    #Var * Function 2x*x^2
    ltp = test3 * 2.0
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 4.0)
    #Var * Double   2x * 2
    ltp = 2.0 * test3
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 4.0)
    # Double * Var   2x * 2

    doubV = [1.0, 1.0]
    ltp = test1 * doubV
    #tests rank()
    self.assertEqual(ltp.rank(),1)
    eval = ltp.evaluate(varFunctions) #gives vector-valued function
    x = eval.x()
    y = eval.y()
    self.assertEqual(x.evaluate(2,1), 2.0)
    self.assertEqual(x.evaluate(5,3), 5.0)
    ltp = doubV * test1
    eval = ltp.evaluate(varFunctions)
    x = eval.x()
    y = eval.y()
    self.assertEqual(x.evaluate(2,1), 2.0)
    self.assertEqual(x.evaluate(4,3), 4.0)

    ltp = test3 + test4
    ltp2 = funPtr * ltp
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(2,4), 48.0)
    # Function * LinearTerm  x^2 * (2x + 2y)

