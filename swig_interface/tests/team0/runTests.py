import TestFunction
import TestLinearTerm
import TestSpatialFilter
import TestRHS
import unittest

testSuite = unittest.makeSuite(TestFunction.TestFunction)
testSuite.addTest(unittest.makeSuite(TestLinearTerm.TestLinearTerm))
testSuite.addTest(unittest.makeSuite(TestSpatialFilter.TestSpatialFilter))

#NVR: TestRHS does not contain meaningful tests
#testSuite.addTest(unittest.makeSuite(TestRHS))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
