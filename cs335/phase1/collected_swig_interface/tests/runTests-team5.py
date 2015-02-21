from TestVar import * 
from TestVarFactory import *
from TestSolution import *
import unittest

testSuite = unittest.makeSuite(TestVar)
testSuite.addTest(unittest.makeSuite(TestVarFactory))
testSuite.addTest(unittest.makeSuite(TestSolution))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
