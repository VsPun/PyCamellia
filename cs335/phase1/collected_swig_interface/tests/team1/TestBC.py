import BC
import Var
import VarFactory
import SpatialFilter
import Function
import unittest

boundary = BC.BC_bc()
vf = VarFactory.VarFactory();
vtest = vf.fieldVar("test", 1);
vflux = vf.fluxVar("test");

class TestBC(unittest.TestCase):
    """ test BC()"""
    def testBoundCond(self):
        self.assertFalse(boundary.bcsImposed(1))
        
    def testSinglePoint(self):
        boundary.addSinglePointBC(17, 0.0)    
        self.assertTrue(boundary.singlePointBC(17))
        self.assertFalse(boundary.bcsImposed(17)) 
        self.assertAlmostEqual(boundary.valueForSinglePointBC(17), 0.0, delta = 1e-12)

        vertex = boundary.vertexForSinglePointBC(17)
        self.assertEqual(vertex,4294967295)
        
    def testZeroMean(self):
        boundary.addZeroMeanConstraint(vtest)    
        self.assertTrue(boundary.imposeZeroMeanConstraint(vtest.ID()))
        boundary.removeZeroMeanConstraint(vtest.ID())
        self.assertFalse(boundary.imposeZeroMeanConstraint(vtest.ID()))
    
    """addDirichlet, getDirichletBC, getSpatiallyFilteredFunctionForDirichletBC"""    
    def testDirichlet(self): 
        f = Function.Function_xn(1)
        boundary.addDirichlet(vflux, SpatialFilter.SpatialFilter_allSpace(), f)
        self.assertAlmostEqual(boundary.getSpatiallyFilteredFunctionForDirichletBC(vflux.ID()).evaluate(1,0), 1, delta = 1e-12)
        dirichlet = boundary.getDirichletBC(vflux.ID())
        self.assertTrue(dirichlet[0].matchesPoint(1.0,1.0))
        self.assertAlmostEqual(dirichlet[1].evaluate(1.0,3.0), 1, delta = 1e-12)
        
