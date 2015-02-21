%module Var
%{
#include "Var.h"
#include "LinearTerm.h"
%}

%include "std_string.i"
%include "Camellia.i"

using namespace std;
using namespace Camellia;

%nodefaultctor Var;  // Disable the default constructor for class Var
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

    LinearTermPtr __mul__(FunctionPtr f) {
      return f * *self;
    }

    LinearTermPtr __rmul__(FunctionPtr f) {
      return f * *self;
    }

    LinearTermPtr __add__(LinearTermPtr lt) {
      return *self + lt;
    }

    LinearTermPtr __radd__(LinearTermPtr lt) {
      return *self + lt;
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

    LinearTermPtr __neg__() {
      return -*self;
    }

    LinearTermPtr __sub__(VarPtr v) {
      return *self - v;
    }

    LinearTermPtr __sub__() {
      return - *self;
    }
  }
};
