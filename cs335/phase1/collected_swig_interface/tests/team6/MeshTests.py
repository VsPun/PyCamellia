"""import swig files & whatever"""
import unittest
import MeshFactory
import Mesh
import Solution
import BF
import VarFactory
import PoissonFormulation

class TestMesh(unittest.TestCase):
    
    def testMeshNormal(self):

        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        h1Order = 2
        cellsX = 2
        cellsY = 3
        numElements = cellsX * cellsY
        activeCellIDs = tuple([])
        for i in range(0, numElements):
            activeCellIDs += tuple([i])
        testMesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF, [1.2, 1.4], [cellsX,cellsY], h1Order) 
        

        self.assertTrue(testMesh.cellPolyOrder(0) == h1Order, "h1Order Broken")
        self.assertTrue(testMesh.numFluxDofs() + testMesh.numFieldDofs() == testMesh.numGlobalDofs())
        self.assertTrue(numElements == testMesh.numElements())
        self.assertTrue(numElements == testMesh.numActiveElements())
        self.assertTrue(activeCellIDs == testMesh.getActiveCellIDs())
        self.assertTrue(testMesh.getDimension() == 2)
        polyOrder = testMesh.cellPolyOrder(0)

        testMesh.pRefine(tuple([0]))
        testMesh.hRefine(tuple([0]))
        numElements += 4
        numActiveElements = numElements - 1
        polyOrder += 1


        self.assertTrue(polyOrder == testMesh.cellPolyOrder(0))
        self.assertTrue(numElements == testMesh.numElements())
        self.assertTrue(numActiveElements == testMesh.numActiveElements())


#Could not figure out how to get registersolution, unregistersolution to work

        solution = Solution.Solution_solution(testMesh)
        testMesh.registerSolution(solution)
        testMesh.unregisterSolution(solution)

        filename = "./tests/team6/B.1.HDF5"
        testMesh.saveToHDF5(filename)
        
 #Could not figure out how to get loadfromHDF5 (& maybe save) to work
        # Load saved Mesh from HDF5
#        testMesh2 = MeshFactory.MeshFactory_loadFromHDF5(poissonBF,filename)

        # Load triangle from HDF5
        testMesh3 = MeshFactory.MeshFactory_readTriangle("./tests/team6/A.1", poissonBF, 2, 3)

    def testMeshVertices(self):
        
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        testMesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF, [1.2, 1.4], [1,1], 2)

        self.assertTrue((0, 2, 3, 1) == testMesh.vertexIndicesForCell(0))
        self.assertTrue(((0.0, 0.0), (1.2, 0.0), (1.2, 1.4), (0.0, 1.4)) == testMesh.verticesForCell(0))
        

if (__name__ == '__main__'):
    unittest.main()
