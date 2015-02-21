%module Mesh
%{
#include "Mesh.h"
%}

%include "Camellia.i"

using namespace std;

//typedef Teuchos::RCP<Solution> SolutionPtr;
//typedef unsigned GlobalIndexType;

%nodefaultctor Mesh;
class Mesh{
public:
  void saveToHDF5(string filename);
  int cellPolyOrder(GlobalIndexType cellID);
  set<GlobalIndexType> getActiveCellIDs();
  int getDimension();
  void hRefine(const set<GlobalIndexType> &cellIDs);
  GlobalIndexType numActiveElements();
  GlobalIndexType numFluxDofs();
  GlobalIndexType numFieldDofs();
  GlobalIndexType numGlobalDofs();
  GlobalIndexType numElements();
  void pRefine(const set<GlobalIndexType> &cellIDsForPRefinements);
  vector<unsigned> vertexIndicesForCell(GlobalIndexType cellID);
  vector< vector<double> > verticesForCell(GlobalIndexType cellID);
  void registerSolution(SolutionPtr solution);
  void unregisterSolution(SolutionPtr solution);
};

class MeshPtr {
public:
  Mesh* operator->();
};

