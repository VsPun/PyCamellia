from BFTests import *
import unittest
from TestSolution import *
from TestHDF5Exporter import *


testSuite = unittest.makeSuite(BFTests)
testSuite.addTest(unittest.makeSuite(TestSolution))
testSuite.addTest(unittest.makeSuite(TestHDF5Exporter))


testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)

