%module Var
%{
#include "Var.h"
#include "LinearTerm.h"
%}

%include "std_string.i"

%nodefaultctor Var;  // Disable the default constructor for class Var


using namespace std;

// need if a type is Space
namespace Camellia {
  enum Space { HGRAD, HCURL, HDIV, HGRAD_DISC, HCURL_DISC, HDIV_DISC, HDIV_FREE, L2, CONSTANT_SCALAR, VECTOR_HGRAD, VECTOR_HGRAD_DISC, VECTOR_L2, UNKNOWN_FS }; // reference formally, ex Var.HGRAD

  // for op()
  enum EOperator { OP_VALUE = 0, OP_GRAD, OP_CURL, OP_DIV, OP_D1, OP_D2, OP_D3, OP_D4, OP_D5, OP_D6, OP_D7, OP_D8, OP_D9, OP_D10, OP_X, OP_Y, OP_Z, OP_DX, OP_DY, OP_DZ, OP_CROSS_NORMAL, OP_DOT_NORMAL, OP_TIMES_NORMAL, OP_TIMES_NORMAL_X, OP_TIMES_NORMAL_Y, OP_TIMES_NORMAL_Z, OP_TIMES_NORMAL_T, OP_VECTORIZE_VALUE };

enum VarType { TEST, FIELD, TRACE, FLUX, UNKNOWN_TYPE, MIXED_TYPE };

}

using namespace Camellia;

class Var {
 public:
  //Var();
  int ID();
  const string & name();
  string displayString();
  int rank();
  Space space();
  VarType varType();
  Camellia::EOperator op();
  LinearTermPtr termTraced();
  VarPtr grad();
  VarPtr div();
  VarPtr curl(int spaceDim);
  VarPtr dx();
  VarPtr dy();
  VarPtr x();
  VarPtr y();
};

class VarPtr {
public:
  Var* operator->();

  %extend {
    LinearTermPtr __mul__(double w) {
      return *self * w;
    }

    LinearTermPtr __rmul__(double w) {
      return *self * w;
    }

    LinearTermPtr __mul__(vector<double> w) {
      return *self * w;
    }

    LinearTermPtr __rmul__(vector<double> w) {
      return *self * w;
    }

    LinearTermPtr __add__(VarPtr v) {
      return *self + v;
    }

    LinearTermPtr __div__(double w) {
      return *self / w;
    }

    LinearTermPtr __div__(FunctionPtr f) {
      return *self / f;
    }

    LinearTermPtr __sub__(VarPtr v) {
      return *self - v;
    }

    LinearTermPtr __sub__() {
      return - *self;
    }
  }
};
