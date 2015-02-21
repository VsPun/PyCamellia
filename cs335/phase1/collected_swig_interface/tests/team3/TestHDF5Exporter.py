import PoissonFormulation
import Solution
import Mesh
import MeshFactory
import Function
import Var
import BF
import VarFactory
import HDF5Exporter
import unittest

class TestHDF5Exporter(unittest.TestCase):
    def testHDF5Constructor(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        hdf5Exp = HDF5Exporter.HDF5Exporter(mesh)
        self.assertIsNotNone(hdf5Exp)

    def testExportFunction1(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        hdf5Exp = HDF5Exporter.HDF5Exporter(mesh)
        x = Function.Function_xn(3)
        hdf5Exp.exportFunction(x, "TestFunction")

    def testExportFunction2(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        hdf5Exp = HDF5Exporter.HDF5Exporter(mesh)
        x = Function.Function_xn(3)
        y = Function.Function_yn(4)
        vec = [x, y]
        nameVec = ["x", "y"]
        hdf5Exp.exportFunction(vec, nameVec)

    def testExportSolution(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 4)
        hdf5Exp = HDF5Exporter.HDF5Exporter(mesh)
        soln = Solution.Solution_solution(mesh)
        hdf5Exp.exportSolution(soln)
        
if (__name__ == '__main__'):
    unittest.main()
