from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import Mesh
import MeshFactory
import unittest

class testLinearTermBasic(unittest.TestCase):
  """Test LinearTerm Basic methods"""
  def testLinearTermBasic(self):

    # Sets up test variables
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")
    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")

    varFunctions = {test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2}

    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")

    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")
    ltp = test1 + test2
    #tests displayString()
    str = ' x +  y'
    self.assertEqual(str, ltp.displayString())
    #tests rank()
    #another rank test is in testLinearTermMul.py
    self.assertEqual(ltp.rank(),0) 
    #tests termType()
    bool = (ltp.termType() == Var.FIELD) 
    self.assertTrue(bool)

    varFunctions = {test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2}

    # tests varIDs()
    varID = (test1.ID(), test2.ID())
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    self.assertEqual(ltp.varIDs(), varID) 

