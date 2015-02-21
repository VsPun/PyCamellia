from Function import *
import BF
import unittest
import Var
import VarFactory
import LinearTerm
import PoissonFormulation
import StokesVGPFormulation
import Function
import Solution
import Mesh
import MeshFactory

varFac = VarFactory.VarFactory()

fieldVar = varFac.fieldVar("fieldVar")
testVar1 = varFac.testVar("testVar",Var.HGRAD)
testVar2 = varFac.testVar("testVar2",Var.HGRAD)

lttestVars = 1.0 * testVar1 
lttrial = 1.0 * fieldVar 

testFlux = varFac.fluxVar("testFlux")
testFluxID = testFlux.ID()

bf = BF.BF_bf(varFac)

vecd = [1.0,1.0]
veci = [1,1]
mesh = MeshFactory.MeshFactory_rectilinearMesh(bf,vecd,veci,2)
soln = Solution.Solution_solution(mesh)

spaceDim = 2
function1 = Function.Function_xn()

useConformingTraces  = True
poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
stokesForm = StokesVGPFormulation.StokesVGPFormulation(spaceDim, useConformingTraces)
stokesBF = stokesForm.bf()
poissonBF = poissonForm.bf()

u1 = stokesForm.u(1) # VarPtr for x component of velocity
p = stokesForm.p()   # VarPtr for pressure

phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued



class BFTest(unittest.TestCase):
  """Test something"""
  def testBFCtor(self):
    testBF = BF.BF_bf(varFac)
    
  def testIsFluxOrTrace(self):
    self.assertTrue(bf.isFluxOrTrace(testFluxID))

  def testAddTerm(self):
    bf.addTerm(fieldVar,testVar1) 
    bf.addTerm(fieldVar,1.0*testVar1)
    bf.addTerm(1.0*fieldVar,testVar1)
    soln.projectOntoMesh({fieldVar.ID() : function1})
    ltsoln = bf.testFunctional(soln)
    function2  = ltsoln.evaluate({testVar1.ID() : function1})
    val = function1.evaluate(1.0,1.0)
    self.assertAlmostEqual(function2.evaluate(1.0,1.0),3*val*val,delta=1e-12)
 # def testGraphNorm(self):
   # IPPtr = bf.graphNorm()
    
# Run the tests:
if (__name__ == '__main__'):
  unittest.main()

