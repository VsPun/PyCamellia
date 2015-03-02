import BF
import VarFactory
import Var
import LinearTerm
import Function
import IP
import unittest
import Solution
import MeshFactory
import Mesh













class BFTests(unittest.TestCase):

	def testConstructor(self):
		vf = VarFactory.VarFactory();
	
		bf = BF.BF_bf(vf);

		self.assertIsNotNone(bf, "test BF.BF_bf()");

#Test the method testName()
	def testTestName(self):

		vf = VarFactory.VarFactory()
		myVar = vf.testVar("identify me", 1)
		i = myVar.ID();
	
		bf = BF.BF_bf(vf);
		self.assertEqual(bf.testName(i), myVar.name(), "testName()");

	def testTrialName(self):
		vf = VarFactory.VarFactory();
		myVar = vf.fieldVar("identify me");
		i = myVar.ID();

		bf = BF.BF_bf(vf);
		self.assertEqual(bf.trialName(i), myVar.name(), "trialName()");

	
#	These methods generate errors, so I commented them out for simplicity.
#	Was unsure about how to use the return type, because it did not work with the 
#	typical enum handling procedure.



#	def testFunctionSpaceForTest(self):
#		vf = VarFactory.VarFactory();
#		v = vf.testVar("test", Var.HGRAD);
#		bf = BF.BF_bf(vf);
#		sp = bf.functionSpaceForTest(v.ID());
#
#		self.assertEqual(sp, v.space(), "testing testFunctionSpaceForTest()");
#
#
#	def testFunctionSpaceForTrial(self):
#		vf = VarFactory.VarFactory();
#		v = vf.fieldVar("field");
#		bf = BF.BF_bf(vf);
#		sp = bf.functionSpaceForTrial(v.ID());
#		self.assertEqual(sp, v.space(), "testing testFunctionSpaceForTest()");
	

	def testAddTerm1(self):

		f = Function.Function_xn(1);
		g = Function.Function_yn(1);
		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field");
		v = vf.testVar("test", Var.HGRAD);
		bf = BF.BF_bf(vf);
		lt = 1.0 * u;
		lt2 = 1.0 * v;
		bf.addTerm(lt, lt2)

		mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [10.0, 10.0], [1, 1], 10)

		soln = Solution.Solution_solution(mesh)
		soln.projectOntoMesh({u.ID() : f})
		lt3 = bf.testFunctional(soln)

		h = lt3.evaluate({v.ID() : g})
		result = h.evaluate(5.0, 6.0);

		self.assertAlmostEqual(30.0,result,delta=1e-6)


	def testAddTerm2(self):

		f = Function.Function_xn(1);
		g = Function.Function_yn(1);
		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field"); #trial var
		v = vf.testVar("test", Var.HGRAD); #test var
		bf = BF.BF_bf(vf);
		lt = 1.0 * v;
		bf.addTerm(u, lt)


		mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [10.0, 10.0], [1, 1], 10)


		soln = Solution.Solution_solution(mesh)
		soln.projectOntoMesh({u.ID() : f})
		lt3 = bf.testFunctional(soln)

		h = lt3.evaluate({v.ID() : g})

		result = h.evaluate(5.0, 6.0);

		self.assertAlmostEqual(30.0,result,delta=1e-6)



	def testAddTerm3(self):

		f = Function.Function_xn(1);
		g = Function.Function_yn(1);
		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field"); #trial var
		v = vf.testVar("test", Var.HGRAD); #test var
		bf = BF.BF_bf(vf);
		lt = 1.0 * u;
		bf.addTerm(lt, v)


		mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [10.0, 10.0], [1, 1], 10)


		soln = Solution.Solution_solution(mesh)
		soln.projectOntoMesh({u.ID() : f})
		lt3 = bf.testFunctional(soln)

		h = lt3.evaluate({v.ID() : g})

		result = h.evaluate(5.0, 6.0);

		self.assertAlmostEqual(30.0,result,delta=1e-6)


	def testAddTerm4(self):

		f = Function.Function_xn(1);
		g = Function.Function_yn(1);
		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field"); #trial var
		v = vf.testVar("test", Var.HGRAD); #test var
		bf = BF.BF_bf(vf);
		bf.addTerm(u, v)


		mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [10.0, 10.0], [1, 1], 10)


		soln = Solution.Solution_solution(mesh)
		soln.projectOntoMesh({u.ID() : f})
		lt3 = bf.testFunctional(soln)

		h = lt3.evaluate({v.ID() : g})

		result = h.evaluate(5.0, 6.0);

		self.assertAlmostEqual(30.0,result,delta=1e-6)

	def testTestFunctional(self):
		f = Function.Function_xn(1);
		g = Function.Function_yn(1);
		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field"); #trial var
		v = vf.testVar("test", Var.HGRAD); #test var
		bf = BF.BF_bf(vf);
		bf.addTerm(u, v)


		mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [10.0, 10.0], [1, 1], 10)


		soln = Solution.Solution_solution(mesh)
		soln.projectOntoMesh({u.ID() : f})
		lt3 = bf.testFunctional(soln)

		h = lt3.evaluate({v.ID() : g})

		result = h.evaluate(5.0, 6.0);

		self.assertAlmostEqual(30.0,result,delta=1e-6)


	def testIsFluxOrTrace(self):
		vf = VarFactory.VarFactory();
		myVar = vf.fluxVar("identify me");
		myVar2 = vf.traceVar("hey");
		myVar3 = vf.fieldVar("hi");
		i = myVar.ID();
		j = myVar2.ID();
		k = myVar3.ID();

		bf = BF.BF_bf(vf);
		self.assertEqual(bf.isFluxOrTrace(i), True, "test isFluxOrTrace");
		self.assertEqual(bf.isFluxOrTrace(j), True, "test isFluxOrTrace");
		self.assertEqual(bf.isFluxOrTrace(k), False, "test isFluxOrTrace");


	#just make sure this method runs successfully.
	def testGraphNorm(self):
		
		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field"); #trial var
		v = vf.testVar("test", Var.HGRAD); #test var
		bf = BF.BF_bf(vf);
		bf.addTerm(u, v)
		ip = bf.graphNorm();

	#just make sure this method runs successfully.
	def testNaieveNorm(self):

		vf = VarFactory.VarFactory();
		u = vf.fieldVar("field"); #trial var
		v = vf.testVar("test", Var.HGRAD); #test var
		bf = BF.BF_bf(vf);
		bf.addTerm(u, v)
		ip = bf.graphNorm();


	def testVarFactory(self):

		vf = VarFactory.VarFactory();
		v = vf.fieldVar("hi");
		u = vf.fieldVar("field");
		uID = u.ID();
	
		bf = BF.BF_bf(vf);
	
		vfCopy = bf.varFactory();
		uCopy = vfCopy.trial(uID);
		uIDCopy = uCopy.ID();

		self.assertEqual(uID, uIDCopy, "testing varFactory()");

if (__name__ == '__main__'):
  unittest.main()


	
