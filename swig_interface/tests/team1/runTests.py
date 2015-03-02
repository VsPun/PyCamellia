from TestFunction import *
from TestSpatialFilter import *
from TestBC import *
import unittest

testSuite = unittest.makeSuite(TestFunction)
testSuite.addTest(unittest.makeSuite(TestSpatialFilter))
testSuite.addTest(unittest.makeSuite(TestBC))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
