from Function import *
import Function
from VarFactory import *
from Var import *
import VarFactory
import Var
import LinearTerm
import unittest
import RHS

class RHSTest(unittest.TestCase):
  """Test RHS"""
  def testRHS(self):
    VarFac = VarFactory.VarFactory()
    u = VarFac.testVar("q", HGRAD)  
    rhs = RHS.RHS_rhs()
    rhs.addTerm(u)
    insert = {u.ID(): Function.Function_xn(2)}
    lt = rhs.linearTermCopy()
    sol = lt.evaluate(insert)
    self.assertAlmostEquals(Function.Function_xn(2).evaluate(2), sol.evaluate(2), delta=1e-12)
    
    


if (__name__ == '__main__'):
  unittest.main()
