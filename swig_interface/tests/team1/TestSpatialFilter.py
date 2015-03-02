import SpatialFilter
import Function
import unittest


class TestSpatialFilter(unittest.TestCase):
    """Test matchespoint(), intersectionFilter(), negatedFilter(), untionFilter(), allSpace()"""
    def testmatchespoint(self):
        self.assertTrue(SpatialFilter.SpatialFilter_allSpace().matchesPoint(1,1))
        point=[2.0,1.0]
        self.assertTrue(SpatialFilter.SpatialFilter_allSpace().matchesPoint(point))
        self.assertTrue(SpatialFilter.SpatialFilter_intersectionFilter(SpatialFilter.SpatialFilter_allSpace(),SpatialFilter.SpatialFilter_allSpace()).matchesPoint(2,4))
        self.assertTrue(SpatialFilter.SpatialFilter_intersectionFilter(SpatialFilter.SpatialFilter_allSpace(),SpatialFilter.SpatialFilter_allSpace()).matchesPoint(2,4))
        self.assertFalse(SpatialFilter.SpatialFilter_negatedFilter(SpatialFilter.SpatialFilter_allSpace()).matchesPoint(5,8))
        self.assertTrue(SpatialFilter.SpatialFilter_unionFilter(SpatialFilter.SpatialFilter_allSpace(),SpatialFilter.SpatialFilter_allSpace()).matchesPoint(6,1))

    """Test matchingX()"""
    def testmatchingX(self):
        self.assertTrue(SpatialFilter.SpatialFilter_matchingX(3).matchesPoint(3,2))
        self.assertFalse(SpatialFilter.SpatialFilter_matchingX(4).matchesPoint(1,4))
    """Test matchingY()"""
    def testmatchingY(self):
        self.assertTrue(SpatialFilter.SpatialFilter_matchingY(2).matchesPoint(3,2))
        self.assertFalse(SpatialFilter.SpatialFilter_matchingY(4).matchesPoint(4,9))

    """Test lessThanX()"""
    def testlessThanX(self):
        self.assertTrue(SpatialFilter.SpatialFilter_lessThanX(7).matchesPoint(3,2))
        self.assertFalse(SpatialFilter.SpatialFilter_lessThanX(8).matchesPoint(10,9))
    """Test greaterThanX()"""
    def testgreaterThanX(self):
        self.assertTrue(SpatialFilter.SpatialFilter_greaterThanX(1).matchesPoint(3,2))
        self.assertFalse(SpatialFilter.SpatialFilter_greaterThanX(16).matchesPoint(10,9))
        
    """Test lessThanY()"""
    def testlessThanY(self):
        self.assertTrue(SpatialFilter.SpatialFilter_lessThanY(7).matchesPoint(31,2))
        self.assertFalse(SpatialFilter.SpatialFilter_lessThanY(8).matchesPoint(0,9))
    """Test greaterThanY()"""
    def testgreaterThanY(self):
        self.assertTrue(SpatialFilter.SpatialFilter_greaterThanY(1).matchesPoint(1,2))
        self.assertFalse(SpatialFilter.SpatialFilter_greaterThanY(16).matchesPoint(103,9))


# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
