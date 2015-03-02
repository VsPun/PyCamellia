from FunctionXNYNTest import *
from FunctionTestInstance import *
from FunctionDivTests import *
from FunctionAddTests import *
from FunctionSubTests import *
from FunctionMulTests import *
from FunctionTestL2Norm import *
from FunctionTestEvaluate import *
from FunctionTestRank import *
from IPTest import *
from testLinearTermBasic import *
from testLinearTermAdd import *
from testLinearTermMul import *
from testLinearTermDiv import *
from testLinearTermSub import *


from RHSTest import *

import unittest

testSuite = unittest.makeSuite(FunctionXNYNTest)
#testSuite.addTest(unittest.makeSuite(FunctionTestInstance))
testSuite.addTest(unittest.makeSuite(FunctionTestRank))
testSuite.addTest(unittest.makeSuite(FunctionTestEvaluate))
testSuite.addTest(unittest.makeSuite(FunctionDivTests))
testSuite.addTest(unittest.makeSuite(FunctionAddTests))
testSuite.addTest(unittest.makeSuite(FunctionSubTests))
testSuite.addTest(unittest.makeSuite(FunctionMulTests))
testSuite.addTest(unittest.makeSuite(IPTest))
testSuite.addTest(unittest.makeSuite(testLinearTermBasic))
testSuite.addTest(unittest.makeSuite(testLinearTermAdd))
testSuite.addTest(unittest.makeSuite(testLinearTermMul))
testSuite.addTest(unittest.makeSuite(testLinearTermDiv))
testSuite.addTest(unittest.makeSuite(testLinearTermSub))
testSuite.addTest(unittest.makeSuite(RHSTest))
testSuite.addTest(unittest.makeSuite(FunctionTestL2Norm))



testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
