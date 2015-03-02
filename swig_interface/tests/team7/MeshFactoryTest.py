import MeshFactory
import PoissonFormulation
import unittest
import Mesh
import VarFactory
import Var
import BF

varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("f")
testVar = varFac.testVar("t", Var.HGRAD)
bf = BF.BF_bf(varFac)
vecd = [1.5,1.5]
veci = [1,1]

class MeshFactoryTest(unittest.TestCase):
  """Test something"""
  def testrectilinearMesh(self):
    #Tests to see if we can even make a mesh
    mesh = MeshFactory.MeshFactory_rectilinearMesh(bf,vecd,veci,2)
    self.assertEqual(2,mesh.getDimension())
    #print ("Number of Dimensions in Mesh: %i" % mesh.getDimension())
    #print ("Number of Elements in Mesh: %i" % mesh.numElements())
    #print ("Number of GlobalDofs in Mesh : %i" % mesh.numGlobalDofs())

  def testloadFromHDF5(self):
    #Tests to see if loadFromHDF5 works (assuming the saveToHDF5 works) 
    mesh = MeshFactory.MeshFactory_rectilinearMesh(bf,vecd,veci,2)
    numGlobalDofsBefore = mesh.numGlobalDofs();
    numElementsBefore = mesh.numElements();

    mesh.saveToHDF5("Mesh.HDF5")
    meshLoad = MeshFactory.MeshFactory_loadFromHDF5(bf,"Mesh.HDF5")


    numGlobalDofsAfter = meshLoad.numGlobalDofs();
    numElementsAfter = meshLoad.numElements();

    self.assertEqual(numGlobalDofsBefore,numGlobalDofsAfter)
    self.assertEqual(numElementsBefore,numElementsAfter)

  def testReadTriangle(self):
    #Tests to see if we can read a triangle mesh
    #Dr. Roberts' code
    spaceDim = 2
    useConformingTraces  = True
    poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
    poissonBF = poissonForm.bf()

    triangleMesh = MeshFactory.MeshFactory_readTriangle("./tests/team7/box.2",poissonBF,2,2)

    #triangleMesh = MeshFactory.MeshFactory_readTriangle("box.2.ele",bf,2,2)

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


