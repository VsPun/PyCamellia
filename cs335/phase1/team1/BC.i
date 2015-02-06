%module BC
%{
#include "BC.h"
  %}


class BC {
 public:

  BC(legacySubclass = false);
  bool bcsImposed(int varID);
  bool singlePointBC(int varID);
  double valueForSinglePointBC(int varID);
  GlobalIndexType vertexForSinglePointBC(int varID);
  bool imposeZeroMeanConstraint(int varID);
  void addDirichlet(VarPtr traceOrFlux, SpatialFilterPtr spatialPoints, FunctionPtr valueFunction);
  void addSinglePointBC( int fieldID, double value,GlobalIndexType meshVertexNumber = -1 );
  void addZeroMeanConstraint( VarPtr field );
  void removeZeroMeanConstraint( int fieldID );
  pair<SpatialFilterPtr, FunctionPtr> getDirichletBC(int varID);
  FunctionPtr getSpatiallyFilteredFunctionForDirichletBC(int varID);

}
