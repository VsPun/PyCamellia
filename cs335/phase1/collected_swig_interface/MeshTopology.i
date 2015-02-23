%module (package = "PyCamellia") MeshTopology
%{
#include "MeshTopology.h"
%}

%include "Camellia.i"

%nodefaultctor MeshTopology; // disable default constructor

class MeshTopology {
public:
  CellPtr addCell(CellTopoPtr cellTopo, const vector< vector<double> > &cellVertices);
%extend {
  static MeshTopologyPtr meshTopology(unsigned spaceDim) {
    return Teuchos::rcp( new MeshTopology(spaceDim) );
  }
}
};

class MeshTopologyPtr {
public:
  MeshTopology* operator->();
};
