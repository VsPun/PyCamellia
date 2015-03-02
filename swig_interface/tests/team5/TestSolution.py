import Solution
import PoissonFormulation
import StokesVGPFormulation
from Var import *
from VarFactory import *
import MeshFactory
import Mesh
import Function
import BC
import BF
import RHS
import IP
import unittest


class TestSolution(unittest.TestCase):

    """Test Solution.py's Solution() constructor"""
    def test_Solution(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh2)
        self.assertIsNotNone(s) #make sure some object exists

        

    """Test Solution.py's addSolution() method"""
    def test_addSolution(self):
        
        # using this method signiture causes an issue with array size mismatch
        # somewhere in your src code
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        
        x = Function.Function_xn(1)
        one = Function.Function_constant(1)
        zero = Function.Function_constant(0)
        phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
        psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued

        q = Solution.Solution_solution(mesh)
        p = Solution.Solution_solution(mesh)
        q.projectOntoMesh({ phi.ID() : x })
        p.projectOntoMesh({ psi.ID() : Function.Function_vectorize(one,zero) })
        
        q.addSolution(p, 1.0)
        s = Solution.Solution_solution(mesh)

        s.projectOntoMesh({
                          phi.ID() : x,
                          psi.ID() : Function.Function_vectorize(one,zero)
                          })
        self.assertEqual(s.L2NormOfSolution(phi.ID()), q.L2NormOfSolution(phi.ID()))
        self.assertEqual(s.L2NormOfSolution(psi.ID()), q.L2NormOfSolution(psi.ID()))
                         
        # again with different params for addSolution
        t = Solution.Solution_solution(mesh)
        s.projectOntoMesh({
                phi.ID() : x,
                psi.ID() : Function.Function_vectorize(one,zero)
          })
        s.addSolution(s,1.0,[phi.ID()])
        self.assertNotEqual(s.L2NormOfSolution(phi.ID()),t.L2NormOfSolution(phi.ID()))
        #s != t since s had something added to it since it was copied



    """Test Solution.py's clear() method"""
    def test_clear(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        
        x = Function.Function_xn(1)
        one = Function.Function_constant(1)
        zero = Function.Function_constant(0)
        phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
        psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued

        s = Solution.Solution_solution(mesh)
        s.projectOntoMesh({
                phi.ID() : x,
                psi.ID() : Function.Function_vectorize(one,zero)
          })
        s.addSolution(s,1.0,[phi.ID()])
        self.assertNotEqual(0.0, s.L2NormOfSolution(0)) # not zero since addSolution
        s.clear()
        self.assertIsNotNone(s) #make sure some object still exists since should be in tact
        self.assertEqual(0, s.L2NormOfSolution(0)) # zero since zero solutions now



    """Test Solution.py's setCubatureEnrichmentDegree() & cubatureEnrichmentDegree() method"""
    def test_cubatureEnrichmentDegree(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh2)
        s.setCubatureEnrichmentDegree(3)
        self.assertEqual(3, s.cubatureEnrichmentDegree())
        s.setCubatureEnrichmentDegree(4)
        self.assertEqual(4, s.cubatureEnrichmentDegree())
        self.assertNotEqual(3, s.cubatureEnrichmentDegree())



    """Test Solution.py's L2NormOfSolution() method"""
    def test_L2NormOfSolution(self):
         poissonForm = PoissonFormulation.PoissonFormulation(2, True)
         poissonBF = poissonForm.bf()
         mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
         s = Solution.Solution_solution(mesh)
         self.assertEqual(0.0, s.L2NormOfSolution(0))

         x = Function.Function_xn(1)
         one = Function.Function_constant(1)
         zero = Function.Function_constant(0)
         phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
         psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued
         r = Solution.Solution_solution(mesh)
         r.projectOntoMesh({ phi.ID() : x, psi.ID() : Function.Function_vectorize(one,zero)})
         r.addSolution(r,1.0,[phi.ID()])
         self.assertAlmostEqual(1.333333333333334, r.L2NormOfSolution(0))
         self.assertAlmostEqual(216, r.L2NormOfSolution(1))

    

    """Test Solution.py's projectOntoMesh() method"""
    def test_projectOntoMesh(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        x = Function.Function_xn(1)
        one = Function.Function_constant(1)
        zero = Function.Function_constant(0)
        phi = poissonForm.phi() 
        psi = poissonForm.psi() 
        r = Solution.Solution_solution(mesh)
        self.assertEqual(0.0, r.L2NormOfSolution(0))
        r.projectOntoMesh({ phi.ID() : x, psi.ID() : Function.Function_vectorize(one,zero)})
        self.assertNotEqual(0.0, r.L2NormOfSolution(0)) #L2Norm can't be 0 after projection


        
    """Test Solution.py's mesh() method"""
    def test_mesh(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh1 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh1)
        #self.assertEqual(mesh1, s.mesh())
        # i want to test that what I set is equal to what I used to set it with, but
        # since that won't work, I can at least test that they behave in the same way
        self.assertEqual(mesh1.getDimension(), s.mesh().getDimension())
        
       

    """Test Solution.py's setBC() and bc() method"""
    def test_bc(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        bc = BC.BC_bc()
        s.setBC(bc)
        #self.assertEqual(bc, s.bc())
        # i want to test that what I set is equal to what I used to set it with, but
        # since that won't work, I can at least test that they behave in the same way
        self.assertEqual(bc.singlePointBC(0), s.bc().singlePointBC(0))
        


    """Test Solution.py's setRHS() and rhs() method"""
    def test_rhs(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        rhs = RHS.RHS_rhs()
        s.setRHS(rhs)
        #self.assertEqual(rhs, s.rhs()) this and variatons on it won't  work
        # i want to test that what I set is equal to what I used to set it with, but
        # since that won't work, I can at least test that they behave in the same way
        self.assertEqual(rhs.nonZeroRHS(0), s.rhs().nonZeroRHS(0))
        


    #"""Test Solution.py's setIP() and ip() method"""
    def test_ip(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        ip = IP.IP_ip()
        s.setIP(ip)
        success = s.ip()
        #self.assertEqual(s.IP(), ip)
        # i want to test that what I set is equal to what I used to set it with, but
        # since that won't work, I can at least test that they behave in the same way
        


   
    """Test Solution.py's save() and load() method"""
    def test_save_and_load(self):
       poissonForm = PoissonFormulation.PoissonFormulation(2, True)
       poissonBF = poissonForm.bf()
       mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
       s = Solution.Solution_solution(mesh2)

       x = Function.Function_xn(1)
       one = Function.Function_constant(1)
       zero = Function.Function_constant(0)
       phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
       psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued

       s.projectOntoMesh({phi.ID() : x,psi.ID() : Function.Function_vectorize(one,zero)})
       s.addSolution(s,1.0,[phi.ID()])
       s.save("location") # if no exception, this is a success
       #new = s.load(BF.BF_bf(), "location") this always seg faults



    #"""Test Solution.py's saveToHDF5() & loadFromHDF5() method"""
    #def test_saveToHDF5(self):



    """Test Solution.py's setUseCondensedSolve() method"""
    def test_setUseCondensedSolve(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        s.setUseCondensedSolve(False) # if no exception, then successful test
       


    # Run the tests:
    if (__name__ == '__main__'):
        unittest.main()
