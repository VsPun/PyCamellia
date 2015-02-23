%module (package = "PyCamellia") MeshFactory
%{
#include "MeshFactory.h"
%}

%include "Camellia.i"

%nodefaultctor MeshFactory; // Disable default constructor

class MeshFactory {
public:
  static MeshPtr loadFromHDF5(BFPtr bf, std::string filename);
  static MeshPtr rectilinearMesh(BFPtr bf, std::vector<double> dimensions, std::vector<int> elementCounts, int H1Order, int pToAddTest=-1,std::vector<double> x0 = std::vector<double>());
  static MeshPtr readTriangle(std::string filePath,BFPtr  bilinearForm, int H1Order, int pToAdd);

  static MeshTopologyPtr rectilinearMeshTopology(vector<double> dimensions, vector<int> elementCounts, vector<double> x0 = vector<double>());
};

