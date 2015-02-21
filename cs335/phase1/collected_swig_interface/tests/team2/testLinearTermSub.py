from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import Mesh
import MeshFactory
import unittest

class testLinearTermSub(unittest.TestCase):
  """Test LinearTermSub methods"""
  def testLinearTermSub(self):

    # Sets up test variables
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")
    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")

    varFunctions = {test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2}


    # Sub overloads
    ltp = test3 - test4
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(4,1), 6.0)
    # Var - Var 2x - 2y
    ltp = - test3
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), -2.0)
    # - Var  -2x
    ltp2 = -ltp
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    # - LinearTerm  -(-2x)
    ltp = test3 + test4
    ltp2 = ltp - test3
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    # LinearTerm - Var   (2x + 2y) - 2x
    ltp2 = test4 - ltp
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), -2.0)
    #Var - LinearTerm    2y - (2x + 2y)
    ltp2 = test1 + test2
    ltp3 = ltp - ltp2
    eval = ltp3.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    #LinearTerm - LinearTerm  (2x + 2y)-(x+y)

