from MeshTest import *
from MeshFactoryTest import *
from BFTest import *
from IPTest import *
import unittest

testSuite = unittest.makeSuite(MeshTest)
testSuite.addTest(unittest.makeSuite(BFTest))
testSuite.addTest(unittest.makeSuite(IPTest))
testSuite.addTest(unittest.makeSuite(MeshFactoryTest))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
