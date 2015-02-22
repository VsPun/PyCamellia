%module (package = "PyCamellia") CellTopology
%{
#include "CellTopology.h"
%}

%include "Camellia.i"

using namespace Camellia;

%nodefaultctor CellTopology; // Disable default constructor

class CellTopology {
public:
  unsigned getSideCount() const;

  static CellTopoPtr point();
  static CellTopoPtr line();
  static CellTopoPtr quad();
  static CellTopoPtr hexahedron();
    
  static CellTopoPtr triangle();
  static CellTopoPtr tetrahedron();
};

class CellTopoPtr {
public:
  CellTopology* operator->();
};
