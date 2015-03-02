from Function import *
import Function
import PoissonFormulation
import Solution
import MeshFactory
import Mesh
import Var
import VarFactory
import BF
import unittest
import math

class FunctionTestSolution(unittest.TestCase):
  def testSolution(self):
      poissonForm = PoissonFormulation.PoissonFormulation(2,True)
      poissonBF = poissonForm.bf()
      mesh1 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[1,1],2)
      mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[4.0,4.0],[1,1],2)
      mesh3 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,4.0],[1,1],2)

      varFact = VarFactory.VarFactory()
      fVar = varFact.fieldVar("f")

      sol1 = Solution.Solution_solution(mesh1)
      sol2 = Solution.Solution_solution(mesh2)
      sol3 = Solution.Solution_solution(mesh3)

      sol1.projectOntoMesh({fVar.ID() : Function.Function_xn(1000)})
      sol2.projectOntoMesh({fVar.ID() : Function.Function_xn(1)})
      sol3.projectOntoMesh({fVar.ID() : Function.Function_xn(400)})

      fn1 = Function.Function_solution(fVar,sol1)
      fn2 = Function.Function_solution(fVar,sol2)
      fn3 = Function.Function_solution(fVar,sol3)

      a1 = Function.Function_xn(1000).l2norm(mesh1)
      a2 = Function.Function_xn(1).l2norm(mesh2)
      a3 = Function.Function_xn(400).l2norm(mesh3)

      b1 = fn1.l2norm(mesh1)
      b2 = fn2.l2norm(mesh2)
      b3 = fn3.l2norm(mesh3)

      self.assertAlmostEqual(0.0,a1 - b1, delta=1e-12)
      self.assertAlmostEqual(0.0,a2 - b2, delta=1e-12)
      self.assertAlmostEqual(0.0,a3 - b3, delta=1e-12)
      

if (__name__ == '__main__'):
  unittest.main()
