import Function
import VarFactory
import Var
import BF
import MeshFactory
import unittest
import LinearTerm
 
myFactory = VarFactory.VarFactory()
var1 = myFactory.fieldVar("x")
var2 = myFactory.fieldVar("y")
var3 = myFactory.fieldVar("x^2")
var4 = myFactory.fieldVar("y^3")
ltMain = var1 + var2
varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

class TestLinearTerm(unittest.TestCase):

  #BEGIN TESTS
  
  def test_varIDs_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   varID = (var1.ID(),var2.ID())
   self.assertEqual(varID, ltMain.varIDs())
    
  def test_displayString_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   lt = var1 + var2
   self.assertEqual(lt.displayString(), ' x +  y')
    
   
  def test_Rank_(self):
   myFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})
   var1 = myFactory.fieldVar("Test")
   x2 = Function.Function.xn(2)
   y4 = Function.Function.yn(4)
   v = Function.Function.vectorize(x2, y4)
   lt1 = x2*var1
   lt2 = v*var1
   self.assertEqual(0, lt1.rank())
   self.assertEqual(1, lt2.rank())
   
  def test_termType_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   var1 = myFactory.testVar("Test", Var.HGRAD)
   f1 = Function.Function.xn(2)
   myLT = f1*var1
   bool = (myLT.termType() == Var.TEST)
   self.assertTrue(bool)
    
    
    #TESTING OVERLOADS
    
    #Add overloads
    
  def test_addLTLT_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTemp = var3 + var4
   ltTest = ltTemp + ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 80.0)
   
  def test_addLTV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = ltMain + var3
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 16.0)
    
  def test_addVLT_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var3 + ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 16.0)
      
  def test_addVV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var3 + var4
   eval = ltTest.evaluate(varFunctions)
   x0 = 3.0; y0 = 4.0
   expectedValue = x0 * x0 + y0 * y0 * y0;
   self.assertAlmostEqual(eval.evaluate(x0, y0), expectedValue, 1e-10)
      
      #Mul overloads
      
  def test_mulFV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = Function.Function_xn(2) * var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 27.0)
      
  def test_mulVF_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest =  var1 * Function.Function_xn(2) 
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 27.0)
  
  def test_mulDV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = 2.0 * var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 6.0)
      
  def test_mulVD_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var1 * 2.0
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 6.0)
    
  def test_mulVecV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   vec = [1.0, 1.0]
   ltTest = vec * var1
   eval = ltTest.evaluate(varFunctions)
   xComp = eval.x() # should equal x
   yComp = eval.y() # should equal x
   x0 = 3.0; y0 = 4.0
   expectedValue = x0
   self.assertEqual(xComp.evaluate(x0, y0), expectedValue)
   self.assertEqual(yComp.evaluate(x0, y0), expectedValue)
    
  def test_mulVVec_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   vec = [1.0, 1.0]
   ltTest = var1 * vec
   eval = ltTest.evaluate(varFunctions)
   xComp = eval.x() # should equal x
   yComp = eval.y() # should equal x
   x0 = 3.0; y0 = 4.0
   expectedValue = x0
   self.assertEqual(xComp.evaluate(x0, y0), expectedValue)
   self.assertEqual(yComp.evaluate(x0, y0), expectedValue)
      
  def test_mulLTF_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = ltMain * Function.Function_xn(2)
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 63.0)
      
     
    
    #Div overloads
    
  def test_divVW_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var1 / 3.0
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 1.0)
      
  def test_divVF_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var1 / Function.Function_xn(1)
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 1.0)
      
    
    #Neg and sub overloads
    
  def test_subVV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var1 - var2
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(4,3), 1.0)
      
  def test_negV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = - var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), -3.0)
      
  def test_negLT_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = - ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), -7.0)
    
  def test_subLTV_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = ltMain - var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 4.0)
    
  def test_subVLT_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTest = var1 - ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), -4.0)
    
  def test_subLTLT_(self):
   yFactory = VarFactory.VarFactory()
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   var3 = myFactory.fieldVar("x^2")
   var4 = myFactory.fieldVar("y^3")
   ltMain = var1 + var2
   varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

   ltTemp = var3 + var4
   ltTest = ltTemp - ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(4,3), 36.0)
    
    
    
    
    
    
    
  
