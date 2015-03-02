import SpatialFilter
import unittest

sf = SpatialFilter.SpatialFilter

class TestSpatialFilter(unittest.TestCase):


    # MatchesPoint Test
    def test_matchesPoint_(self):
        x = sf.matchingX(2.0)
        y = sf.matchingY(4.0)
        xy = x | y
        self.assertEqual(True, xy.matchesPoint(2.0, 4.0))

    # allSpace test
#    def test_allSpace_(self):
#        x = sf.matchingX(1.0)
#        y = sf.negatedFilter(x)
#        xy = x | y
#        self.assertEqual(xy, sf.allSpace())

    # unionFilter
    def test_unionFilter_(self):
        x = sf.matchingX(36.0)
        y = sf.matchingY(64.0)
        xy = sf.unionFilter(x, y)
        self.assertEqual(True, xy.matchesPoint(36.0, 64.0))
        
    # intersectionFilter
#    def test_intersectionFilter_(self):
#        x = sf.greaterThanX(1.0)
#        y = sf.allSpace()
#        xy = sf.intersectionFilter(x, y)
#        self.assertEqual(xy, x)
        
    # negatedFilter
#    def test_negatedFilter_(self):
#        x = sf.matchingX(1.0)
#        y = sf.negatedFilter(x)
#        xy = x & y
#        self.assertEqual(xy, sf.negatedFilter(sf.allSpace()))

    # matchingX
    def test_matchingX_(self):
        x = sf.matchingX(8.0)
        self.assertEqual(True, x.matchesPoint(8.0, 24.0))


     # matchingY
    def test_matchingY_(self):
        y = sf.matchingY(8.0)
        self.assertEqual(True, y.matchesPoint(24.0, 8.0))

    # lessThanX
    def test_lessThanX_(self):
        x = sf.lessThanX(8.0)
        self.assertEqual(False, x.matchesPoint(8.1, 24.0))
    
    # lessThanY
    def test_lessThanY_(self):
        x = sf.lessThanY(8.0)
        self.assertEqual(False, x.matchesPoint(24.0, 8.1))
    
    # greaterThanX
    def test_greaterThanX_(self):
        x = sf.greaterThanX(8.0)
        self.assertEqual(True, x.matchesPoint(8.1, 24.0))
    
    # greaterThanY
    def test_greaterThanY_(self):
        x = sf.greaterThanY(8.0)
        self.assertEqual(True, x.matchesPoint(24.0, 8.1))
    
