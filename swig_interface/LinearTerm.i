%module (package = "PyCamellia") LinearTerm
%{
#include "LinearTerm.h"
%}

%include "Camellia.i"

using namespace std;

%nodefaultctor LinearTerm;  // Disable the default constructor for class LinearTerm        


class LinearTerm {
public:                                                                                                                                                       
  const set<int> & varIDs();

  VarType termType();

  int rank();

  string displayString();
  
%extend {
  FunctionPtr evaluate(const map<int, FunctionPtr> &varFunctions) {
    map<int, FunctionPtr> varFunctionsCopy = varFunctions; 
    return self->evaluate(varFunctionsCopy); 
  }
}

};
//FunctionPtr operator*(double weight, FunctionPtr f);                                                                                                                               

class LinearTermPtr {
public:
  LinearTerm* operator->();

  %extend {
    LinearTermPtr __add__(LinearTermPtr t2) {
      return *self + t2;
    }
    LinearTermPtr __add__(VarPtr v) {
      return *self + v;
    }
    LinearTermPtr __radd__(VarPtr v) {
      return *self + v;
    }
    LinearTermPtr __mul__(FunctionPtr f){
       return f * *self; 
    }
    LinearTermPtr __rmul__(FunctionPtr f){
       return f * *self; 
    }
    LinearTermPtr __neg__() {
      return - *self;
    }
    LinearTermPtr __sub__(VarPtr v){
      return *self - v;
    }
    LinearTermPtr __rsub__(VarPtr v){
      return v - *self;
    }
    LinearTermPtr __sub__(LinearTermPtr a2){
      return *self - a2;
    }
  }
};
