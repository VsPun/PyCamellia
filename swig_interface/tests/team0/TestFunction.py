import Function
import VarFactory
import Var
import BF
import MeshFactory
import unittest
import Solution

f = Function.Function
 
class TestFunction(unittest.TestCase):
  def test_x_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertAlmostEqual(16.0, f.evaluate(v.x(), 4, 1), delta=1e-12)
   
  def test_y_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertAlmostEqual(81.0, f.evaluate(v.y(), 1, 3), delta=1e-12)
  
  def test_dx_(self):
   x3 = f.xn(3)
   self.assertAlmostEqual(12.0, f.evaluate(x3.dx(), 2, 1), delta=1e-12)
   
  def test_dy_(self):
   y3 = f.yn(3)
   self.assertAlmostEqual(48.0, f.evaluate(y3.dy(), 1, 4), delta=1e-12)
  
  def test_div_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertAlmostEqual(40.0, f.evaluate(v.div(), 4, 2), delta=1e-12)
   
  def test_grad_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual("(2 \\cdot x,0)", v.grad().x().displayString())
   self.assertEqual("(0,4 \\cdot y^3)", v.grad().y().displayString())
   
  def test_rank_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual(0, x2.rank())
   self.assertEqual(1, v.rank())
   
  def test_l2norm_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   g = f.vectorize(x2, y4)
   vf = VarFactory.VarFactory()
   p = vf.fieldVar("p")
   v = vf.testVar("v", Var.HGRAD)
   b = BF.BF_bf(vf)
   mp = MeshFactory.MeshFactory_rectilinearMesh(b, [1.0, 1.0], [1, 1], 2)
   self.assertAlmostEqual(0.44721359549995804, x2.l2norm(mp, 0), delta=1e-12)
   self.assertAlmostEqual(0.3293301281895316, y4.l2norm(mp, 0), delta=1e-12)
   self.assertAlmostEqual(0.5553902531853916, g.l2norm(mp, 0), delta=1e-12)
   
  def test_displayString_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual("x^2", x2.displayString())
   self.assertEqual("y^4", y4.displayString())
   self.assertEqual("(x^2,y^4)", v.displayString())
   
  def test_evaluate_(self):
   x2 = f.xn(2)
   y3 = f.yn(3)
   self.assertAlmostEqual(31.0, f.evaluate(x2+y3, 2, 3), delta=1e-12)
   
  def test_composedFunction_(self):
   h = 3*f.xn(2) + 5*f.yn(1)
   g = f.vectorize(3*f.yn(1), 2*f.xn(1) + 3)
   self.assertAlmostEqual(153.0, f.evaluate(f.composedFunction(h, g), 3, 2), delta=1e-12)
   
  def test_constant_(self):
   self.assertEqual("7", f.constant(7).displayString())
   
  def test_vectorize_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual("x^2", v.x().displayString())
   self.assertEqual("y^4", v.y().displayString())
   
  #Told NOT to test!!
  #def test_normal_(self):
   
  def test_solution(self):
   vf = VarFactory.VarFactory()
   p = vf.fieldVar("p")
   v = vf.testVar("v", Var.HGRAD)
   b = BF.BF_bf(vf)
   mp = MeshFactory.MeshFactory_rectilinearMesh(b, [1.0, 1.0], [1, 1], 3)
   soln = Solution.Solution_solution(mp)
   soln.projectOntoMesh({p.ID() : f.xn(2)})
   g = f.solution(p, soln)
   self.assertAlmostEqual(0.0, f.xn(2).l2norm(mp, 2) - g.l2norm(mp, 2), delta=1e-12)
   
  
  def test_xn_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(9.0, f.evaluate(x2, 3, 1), delta=1e-12)
  
  def test_yn_(self):
   y2 = f.yn(2)
   self.assertAlmostEqual(25.0, f.evaluate(y2, 1, 5), delta=1e-12)
   
  def test_multFF_(self):
   x2 = f.xn(2)
   y2 = f.yn(2)
   self.assertAlmostEqual(36.0, f.evaluate(x2*y2, 2, 3), delta=1e-12)
   
  def test_divideFF_(self):
   x2 = f.xn(2)
   y2 = f.yn(2)
   self.assertAlmostEqual(4.0, f.evaluate(x2/y2, 4, 2), delta=1e-12)
   
  def test_divideFD_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(8.0, f.evaluate(x2/2, 4, 1), delta=1e-12)
   
  def test_divideDF_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(2.0, f.evaluate(18/x2, 3, 1), delta=1e-12)
   
  def test_multDF_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(36.0, f.evaluate(4*x2, 3, 1), delta=1e-12)
   
  def test_multFD_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(50.0, f.evaluate(x2*2, 5, 1), delta=1e-12)
   
  def test_multVF_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   h = [3.0, 2.0]
   g = f.vectorize(x2, y4)
   self.assertAlmostEqual(59.0, f.evaluate(h * g, 3, 2), delta=1e-12)
   
  def test_multFV_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   h = [3.0, 2.0]
   g = f.vectorize(x2, y4)
   self.assertAlmostEqual(174.0, f.evaluate(g * h, 2, 3), delta=1e-12)
   
  def test_addFF_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   self.assertAlmostEqual(32.0, f.evaluate(x2+y4, 4, 2), delta=1e-12)
   
  def test_addFD_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(19.0, f.evaluate(x2+3, 4, 2), delta=1e-12)
   
  def test_addDF_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(27.0, f.evaluate(2+x2, 5, 2), delta=1e-12)
   
  def test_minFF_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   self.assertAlmostEqual(0.0, f.evaluate(x2-y4, 4, 2), delta=1e-12)
   
  def test_minFD_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(47.0, f.evaluate(x2-2, 7, 2), delta=1e-12)
   
  def test_minDF_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(25.0, f.evaluate(50-x2, 5, 2), delta=1e-12)
   
  def test_neg_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(-25.0, f.evaluate(-x2, 5, 2), delta=1e-12)
  
   
