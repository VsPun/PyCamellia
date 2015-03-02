from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import Mesh
import MeshFactory
import unittest

class testLinearTermAdd(unittest.TestCase):
  """Test LinearTerm ADD methods"""
  def testLinearTermAdd(self):

    # Sets up test variables
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")
    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")

    varFunctions = {test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2}

    #add overloads
    ltp = test1 + test2
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    #var + var (x+y)
    ltp2 = ltp + test3
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 4.0)
    #LinearTerm + Var (x + y + 2x)
    ltp2 = test3 + test4
    ltp3 = ltp + ltp2
    eval = ltp3.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 6.0)
    #LinearTerm + LinearTerm (x + y + 2x + 2y)
    ltp = test3 + ltp2
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 6.0)
    #Var + LinearTerm (2x + 2x + 2y)




