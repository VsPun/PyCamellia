%module Camellia
%{
#include "BC.h"
#include "IP.h"
#include "Function.h"
#include "LinearTerm.h"
#include "SpatialFilter.h"
#include "Solution.h"
#include "Var.h"
#include "VarFactory.h"
%}

%include "std_string.i"
%include "std_map.i"
%include "std_pair.i"
%include "std_set.i"
%include "std_vector.i"

namespace std {
  %template(DoubleVector) vector<double>;
  %template(DoubleVectorVector) vector< std::vector<double> >;
  %template(FunctionVector) vector<FunctionPtr>;
  %template(IntFunctionMap) map<int, FunctionPtr>;
  %template(IntSet) set<int>;
  %template(IntVector) vector<int>;
  %template(SpatialFilterFunctionPair) pair<SpatialFilterPtr,FunctionPtr>;
  %template(StringVector) vector<string>;
  %template(UnsignedSet) set<unsigned>;
  %template(UnsignedVector) vector<unsigned>;
  %template(VarVector) vector<VarPtr>;
}

#include "IndexType.h"

typedef Teuchos::RCP<Solution> SolutionPtr;
typedef unsigned GlobalIndexType;

using namespace std;

// need if a type is Space
namespace Camellia {
  enum Space { HGRAD, HCURL, HDIV, HGRAD_DISC, HCURL_DISC, HDIV_DISC, HDIV_FREE, L2, CONSTANT_SCALAR, VECTOR_HGRAD, VECTOR_HGRAD_DISC, VECTOR_L2, UNKNOWN_FS }; // reference formally, ex Var.HGRAD

  // for op()
  enum EOperator { OP_VALUE = 0, OP_GRAD, OP_CURL, OP_DIV, OP_D1, OP_D2, OP_D3, OP_D4, OP_D5, OP_D6, OP_D7, OP_D8, OP_D9, OP_D10, OP_X, OP_Y, OP_Z, OP_DX, OP_DY, OP_DZ, OP_CROSS_NORMAL, OP_DOT_NORMAL, OP_TIMES_NORMAL, OP_TIMES_NORMAL_X, OP_TIMES_NORMAL_Y, OP_TIMES_NORMAL_Z, OP_TIMES_NORMAL_T, OP_VECTORIZE_VALUE };

enum VarType { TEST, FIELD, TRACE, FLUX, UNKNOWN_TYPE, MIXED_TYPE };

}

using namespace Camellia;
