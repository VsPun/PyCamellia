from Function import *
import Function
import PoissonFormulation
import Solution
import MeshFactory
import Mesh
import BF
import unittest
import math

class FunctionTestL2Norm(unittest.TestCase):
  def testL2Norm(self):
      poissonForm = PoissonFormulation.PoissonFormulation(2,True)
      poissonBF = poissonForm.bf()
      mesh1 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[1,1],2)
      mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[4.0,4.0],[1,1],2)
      mesh3 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,4.0],[1,1],2)

      c1 = Function.Function_constant(1.0)

      a1 = c1.l2norm(mesh1)
      a2 = c1.l2norm(mesh2)
      a3 = c1.l2norm(mesh3)


      self.assertAlmostEquals(a1,1.0,delta=1e-12)
      self.assertAlmostEquals(a2,4.0,delta=1e-12)
      self.assertAlmostEquals(a3,2.0,delta=1e-12)

if (__name__ == '__main__'):
  unittest.main()
