%module (package = "PyCamellia") Cell
%{
#include "Cell.h"
%}

%include "Camellia.i"

%nodefaultctor Cell; // Disable default constructor

class Cell {
public:
  IndexType cellIndex();
  const vector< CellPtr > &children();
  vector<IndexType> getChildIndices();
  int numChildren();
  
  CellPtr getParent();
  bool isParent();
  
  RefinementPatternPtr refinementPattern();
  void setRefinementPattern(RefinementPatternPtr refPattern);

  CellTopoPtr topology();
  
  CellPtr getNeighbor(unsigned sideOrdinal);
  
  const vector< unsigned > &vertices();
};

class CellPtr {
public:
  Cell* operator->();
};
