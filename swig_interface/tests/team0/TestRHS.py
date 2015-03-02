import RHS
import unittest
import LinearTerm

rhs = RHS.RHS

class TestRHS(unittest.TestCase):
    
    # constructors
    def test_RHS_(self):
        self.assertEqual(rhs.rhs(), rhs.rhs())
        
    # --- not sure how RHS works, need more info to write tests for nonZeroRHS and addTerm
        def test_nonZeroRHS_(self):
            r = rhs.rhs()
            l = LinearTerm.LinearTerm_LinearTerm()
            
    
    def test_linearTerm_(self):
        r = rhs.rhs()
        lt = r.linearTerm()
        # --- need LinearTerm to be working so I know how to test it. will want to change the linearTerm and compare it to the RHS
        self.assertEqual(r, lt)
    
    def test_linearTermCopy(self):
        r = rhs.rhs()
        lt = r.linearTermCopy()
        # --- need LinearTerm to be working so I know how to test it. will want to change the linearTerm and compare it to the RHS
        self.assertNotEqual(r, lt)
    
