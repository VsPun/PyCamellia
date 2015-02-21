import PoissonFormulation
import Solution
import Mesh
import MeshFactory
import BF
import BC
import RHS
import IP
import Function
import Var
import VarFactory
import HDF5Exporter
import unittest

class TestSolution(unittest.TestCase):
    """Test Solution's methods"""

    def testSolnConstr(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        #create a new solution with mesh
        soln = Solution.Solution_solution(mesh)
        self.assertEquals(soln.mesh().numActiveElements(), 12, "Testing Solution Constructor")

    """def testDupSolnConstr(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        #create a new solution with mesh
        soln = Solution.Solution_solution(mesh)
        solnDup = Solution.Solution(soln)
        self.assertEquals(solnDup.mesh().numActiveElements(), 12, "Testing Solution Constructor")
        --------Apparently this constructor isn't defined in the Solution.i file anymore--------"""

    def testAddSolution2(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        x = Function.Function_xn(1)
        one = Function.Function_constant(1)
        zero = Function.Function_constant(0)
        phi = formulation.phi() # VarPtr for main, scalar-valued variable in Poisson problem
        psi = formulation.psi() # VarPtr for gradient of psi, vector-valued
        soln = Solution.Solution_solution(mesh)
        soln2 = Solution.Solution_solution(mesh)
        soln.projectOntoMesh({
                phi.ID() : x,
                psi.ID() : Function.Function_vectorize(one,zero)
          })
        soln.addSolution(soln,1.0,[phi.ID()])
        self.assertNotEqual(soln.L2NormOfSolution(0), soln2.L2NormOfSolution(0)) 

    def testClear(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        #create a new solution with mesh
        soln = Solution.Solution_solution(mesh)
        soln.clear()
        self.assertIsNotNone(soln)
        self.assertEquals(soln.L2NormOfSolution(0), 0)

    def testCubEnriDegr(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        soln = Solution.Solution_solution(mesh)
        soln.setCubatureEnrichmentDegree(8)
        self.assertEquals(soln.cubatureEnrichmentDegree(), 8)

    def tesSetCubatureEnrichmentDegree(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        soln = Solution.Solution_solution(mesh)
        soln.setCubatureEnrichmentDegree(9)
        self.assertEquals(soln.cubatureEnrichmentDegree(), 9)

    def testL2NormOfSolution(self):
        formulation = PoissonFormulation.PoissonFormulation(2, True)
        bf = formulation.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)
        #make a bf, add a field variable, then get its id, pass it to L2Norm
        soln = Solution.Solution_solution(mesh)
        vf = VarFactory.VarFactory()
        fv = vf.fieldVar("Hello")
        self.assertEquals(soln.L2NormOfSolution(fv.ID()), 0.0)
        
    def testProjOntoMesh(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
        psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued
        x = Function.Function_xn(1)
        y = Function.Function_yn(1)
        one = Function.Function_constant(1)
        zero = Function.Function_constant(0)
        soln = Solution.Solution_solution(mesh)
        self.assertEquals(0.0, soln.L2NormOfSolution(phi.ID()))
        soln.projectOntoMesh({ phi.ID() : x, psi.ID() : Function.Function_vectorize(one,zero) })
        self.assertNotEquals(0.0, soln.L2NormOfSolution(phi.ID()))

    def testMesh(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        soln = Solution.Solution_solution(mesh)
        self.assertEquals(soln.mesh().numActiveElements(), mesh.numActiveElements(), "Testing Solution's Mesh Method")

    def testBC(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        soln = Solution.Solution_solution(mesh)
        vf = VarFactory.VarFactory()
        fv = vf.fieldVar("Hello")
        testBC = BC.BC_bc()
        soln.setBC(testBC)
        self.assertEqual(testBC.bcsImposed(fv.ID()), soln.bc().bcsImposed(fv.ID()))

    def testIP(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        soln = Solution.Solution_solution(mesh)
        testIP = IP.IP_ip()
        soln.setIP(testIP)
        worked = soln.ip()
        self.assertIsNotNone(worked)

#Could not test the other methods successfully in solution so they are not included in this file

if (__name__ == '__main__'):
    unittest.main()
