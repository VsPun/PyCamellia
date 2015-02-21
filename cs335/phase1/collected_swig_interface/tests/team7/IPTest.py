from Function import *
import Function
import LinearTerm
import IP
import VarFactory
import Var
import unittest
import Solution
import MeshFactory
import Mesh
import BF
import PoissonFormulation
import StokesVGPFormulation


varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("fieldVar")
tv = varFac.fieldVar("tv")
testVar = varFac.testVar("testVar",3)
testLT = 0.0 * fieldVar
testFlux = varFac.fluxVar("testFlux")


spaceDim = 2
useConformingTraces  = True
poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
stokesForm = StokesVGPFormulation.StokesVGPFormulation(spaceDim, useConformingTraces)

class IPTest(unittest.TestCase):
  """Basic Test case"""
  def testConstructorOK(self):
    testIP = IP.IP_ip()
    self.assertIsNotNone(testIP)
    #print "Constructor succeeded"

  def testAddVarTermOK(self):
    testIP = IP.IP_ip()
    testIP.addTerm(testVar)
    self.assertIsNotNone(testIP)
    #print "Add testVar term succeeded"

  def testAddLinTermOK(self):
    testIP = IP.IP_ip()
    test1 = varFac.fieldVar("x")
    test2 = varFac.fieldVar("y")
    ltp = test1 + test2
    testIP.addTerm(ltp)
    self.assertIsNotNone(testIP)
    #print "Add Linear term succeeded"
  
  def testEvaluateOK(self):
    testIP = IP.IP_ip()
    testIP.addTerm(tv)
    # dictionary objects
    testmap1 = {tv.ID(): Function.Function_xn(2)}
    testmap2 = {tv.ID(): Function.Function_xn(2)}
    # create linear term
    lntrm = testIP.evaluate(testmap1)
    # get a function from the linearterm
    res = lntrm.evaluate(testmap2)
    # test case taken from group 02
    self.assertAlmostEquals(Function.Function_xn(4).evaluate(2), res.evaluate(2), delta=1e-12)
    #also possible to use l2norm?

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


