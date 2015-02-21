from Function import *
import Function
import VarFactory
import Var
import LinearTerm
import unittest
import IP

class IPTest(unittest.TestCase):
  """Test IP"""
  def testIP(self):
    VarFac = VarFactory.VarFactory()
    u = VarFac.fieldVar("test")
    ip = IP.IP_ip()
    ip.addTerm(u)
    insert = {u.ID(): Function.Function_xn(2)}
    insert2 = {u.ID(): Function.Function_xn(2)}
    lt = ip.evaluate(insert)
    sol = lt.evaluate(insert2)
    self.assertAlmostEquals(Function.Function_xn(4).evaluate(2), sol.evaluate(2), delta=1e-12)
    
    


if (__name__ == '__main__'):
  unittest.main()
