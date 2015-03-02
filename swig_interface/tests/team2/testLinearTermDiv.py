from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import Mesh
import MeshFactory
import unittest

class testLinearTermDiv(unittest.TestCase):
  """Test LinearTermDiv methods"""
  def testLinearTermDiv(self):

    # Sets up test variables
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")
    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")

    varFunctions = {test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2}

    funPtr = Function.Function_xn(2)

    #Div overloads
    ltp = test3 / 2.0
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,0), 1.0)
    # Var / Double  2x/2
    ltp = test3 / funPtr
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,0), 2.0)
    # Var / function  2x/(x^2)
