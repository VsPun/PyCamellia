from Var import *
from VarFactory import *
from LinearTerm import *
import unittest

class TestVar(unittest.TestCase):

    """Test Var.py's ID() method"""
    def test_ID(self):
        factory = VarFactory()
        self.assertEqual(0, factory.fieldVar("").ID()) #IDs start at 0 and increase by 1 each time

    """Test Var.py's name() method"""
    def test_name(self):
        factory = VarFactory()
        self.assertEqual("name", factory.fieldVar("name").name())

    """Test Var.py's displayString() method"""
    def test_displayString(self):
       factory = VarFactory()
       self.assertEqual("name", factory.fieldVar("name").displayString())

    """Test Var.py's rank() method"""
    def test_rank(self):
       factory = VarFactory()
       self.assertEqual(0, factory.fieldVar("").rank())
       self.assertEqual(1, factory.testVar("", HDIV).rank())

    """Test Var.py's space() method"""
    def test_space(self):
        factory = VarFactory()
        self.assertEqual(L2, factory.fieldVar("").space())
        self.assertEqual(HGRAD, factory.testVar("", HGRAD).space())

    """Test Var.py's varType() method"""
    def test_varType(self):
        factory = VarFactory()
        self.assertEqual(0, factory.testVar("", HGRAD).varType())
        self.assertEqual(1, factory.fieldVar("").varType())
        trace = factory.fieldVar("").termTraced()
        flux = factory.fluxVar("", trace)
        self.assertEqual(1, flux.varType())
        self.assertEqual(1, factory.fluxVar("").varType())
        self.assertEqual(1, factory.traceVar("").varType())

 
    """Test Var.py's op() method"""
    def test_op(self):
        factory = VarFactory()
        self.assertEqual(OP_VALUE, factory.fieldVar("").op())
        self.assertEqual(OP_VALUE, factory.testVar("", HGRAD).op())

    #"""Test Var.py's termTraced() method"""
    #def test_termTraced(self):
        #factory = VarFactory()
        #u = factory.fieldVar("u")
        #fluxA = factory.fluxVar("x", u)
        #t = fluxA.termTraced()
        #s = t.varIDs()        ##### THIS DOESN"T WORK
        #self.assertEqual(1, s.amount())
        #self.assertEqual(u.ID(), s[0]) 

    """Test Var.py's grad() method"""
    def test_grad(self):
        factory = VarFactory()
        self.assertEqual(OP_GRAD, factory.fluxVar("").grad().op())

    """Test Var.py's div() method"""
    def test_div(self):
        factory = VarFactory()
        x = factory.testVar("", HDIV)
        self.assertEqual(OP_DIV, x.div().op())

    """Test Var.py's curl(int spaceDim) method"""
    def test_curl(self):
        factory = VarFactory()
        x = factory.testVar("", HCURL)
        self.assertEqual(OP_CURL, x.curl(HGRAD).op())

    """Test Var.py's dx() method"""
    def test_dx(self):
        factory = VarFactory() 
        self.assertEqual(OP_DX, factory.fluxVar("").dx().op())

    """Test Var.py's dy() method"""
    def test_dy(self):
        factory = VarFactory()
        self.assertEqual(OP_DY, factory.fluxVar("").dy().op())
        

    """Test Var.py's x() method"""
    def test_x(self):
        factory = VarFactory()
        x = factory.testVar("", HDIV)
        self.assertEqual(OP_X, x.x().op())
      
    """Test Var.py's y() method"""
    def test_y(self):
        factory = VarFactory()
        x = factory.testVar("", HDIV)
        self.assertEqual(OP_Y, x.y().op())


    # Run the tests:
    if (__name__ == '__main__'):
        unittest.main()
