import Function
import PoissonFormulation
import VarFactory
import Var
import Solution
import BF
import Mesh
import MeshFactory
import unittest

x1 = Function.Function_xn(2)
y1 = Function.Function_yn(1)
z = Function.Function_constant(0)
poissonForm = PoissonFormulation.PoissonFormulation(2, True)
poissonBF = poissonForm.bf()
mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 1)

class TestFunction(unittest.TestCase):

    """Test x(), y(), vectorize(), evaluate() """
    def testComponent(self):
        self.assertAlmostEqual(4,Function.Function_vectorize(x1, y1).x().evaluate(2,3),delta =1e-12)
        self.assertAlmostEqual(3,Function.Function_vectorize(x1, y1).y().evaluate(2,3),delta =1e-12)
        

    """ Test dx(), dy(), div(), grad()"""
    def testCalc(self):
        self.assertAlmostEqual(0,Function.Function_constant(2).dx().evaluate(1,2),delta=1e-12)
        self.assertAlmostEqual(0,Function.Function_constant(2).dy().evaluate(1,2),delta=1e-12)
        v = Function.Function_vectorize(z , z)
        self.assertAlmostEqual(0.0, v.div().evaluate(1,2), delta = 1e-12)
        self.assertAlmostEqual(2.0, x1.grad().x().evaluate(1,2), delta = 1e-12)

    """ Test rank() """
    def testRank(self):
        self.assertEqual(0, Function.Function_constant(2).rank())
        self.assertEqual(1, Function.Function_vectorize(x1,y1).rank())

    """ Test 12norm() """
    def testNorm(self):
        self.assertAlmostEqual(z.l2norm(mesh), 0.0 ,delta = 1e-12) 
        

    """ Test displayString()"""
    def testDisplayString(self):
        self.assertEqual("y",Function.Function_vectorize(y1, z).x().displayString())
        self.assertEqual("(y,0)",Function.Function_vectorize(y1, z).displayString())

    """ Test composedFunction(), constant(), xn(), yn() """
    def testEval(self):
        self.assertAlmostEqual(3, Function.Function_xn(1).evaluate(3, 2), delta=1e-12)
        self.assertAlmostEqual(2, Function.Function_yn(1).evaluate(3, 2), delta=1e-12)
        self.assertAlmostEqual(12, Function.Function_constant(12).evaluate(2, 2), delta = 1e-12)
        x3 = Function.Function_vectorize(z ,z)
        self.assertAlmostEqual(0.0, Function.Function_composedFunction(x1, x3).evaluate(2, 0),delta=1e-12)

    """Test solution()"""
    def testSolution(self):
        vf = VarFactory.VarFactory()
        p = vf.fieldVar("p")
        v = vf.testVar("v", Var.HGRAD)
        b = BF.BF_bf(vf)
        msh = MeshFactory.MeshFactory_rectilinearMesh(b , [1.0,1.0], [1,1], 2)
        s = Solution.Solution_solution(msh)
        s.projectOntoMesh({ p.ID() : Function.Function_xn(45)})
        r = Function.Function_solution(p, s)
	self.assertAlmostEqual(Function.Function_xn(45).l2norm(msh, 0) - r.l2norm(msh,0),0.00028653041840038087 , delta =1e-12)
    
    """Test operator*"""
    def testoperatormul(self):
       f = Function.Function_constant(2) * Function.Function_constant(3)
       self.assertAlmostEqual(6, f.evaluate(5,-2), delta=1e-12)
       f = 10 * Function.Function_constant(3)
       self.assertAlmostEqual(30, f.evaluate(1,200), delta=1e-12)
       f = Function.Function_constant(4) * 3
       self.assertAlmostEqual(12, f.evaluate(-7,20), delta=1e-12)
       vec = [3,4]
       f = vec * Function.Function_xn(1)
       self.assertAlmostEqual(6, f.x().evaluate(2,1), delta=1e-12)
       vec = [3,1]
       f = Function.Function_yn(1) * vec
       self.assertAlmostEqual(6, f.x().evaluate(-1,2), delta=1e-12)

    """Test operator/"""
    def testoperatordiv(self):
       f = Function.Function_constant(-50)/Function.Function_constant(10)
       self.assertAlmostEqual(-5, f.evaluate(4,-123), delta=1e-12)
       f = Function.Function_constant(6)/3.0
       self.assertAlmostEqual(2, f.evaluate(10,-6), delta=1e-12)
       f = 12 / Function.Function_constant(4)
       self.assertAlmostEqual(3, f.evaluate(0,0), delta=1e-12) 

    """Test operator+"""
    def testoperatorplus(self):
       f = Function.Function_constant(22) + Function.Function_constant(18)
       self.assertAlmostEqual(40, f.evaluate(8,-7), delta=1e-12)
       f = Function.Function_constant(16) + 16
       self.assertAlmostEqual(32, f.evaluate(5,4), delta=1e-12)
       f = 12 + Function.Function_constant(14)
       self.assertAlmostEqual(f.evaluate(1,2), 26, delta=1e-12)
     
    """Test operator-"""
    def testoperatorminus(self):
       f = Function.Function_constant(22) - Function.Function_constant(18)
       self.assertAlmostEqual(4, f.evaluate(2,469), delta=1e-12)
       f = Function.Function_constant(0) - -10
       self.assertAlmostEqual(10, f.evaluate(12,46), delta=1e-12)
       f = -5 - Function.Function_constant(-4)
       self.assertAlmostEqual(-1, f.evaluate(8,46), delta=1e-12)
       f = -Function.Function_constant(9)
       self.assertAlmostEqual(-9, f.evaluate(-43,12), delta=1e-12)    
