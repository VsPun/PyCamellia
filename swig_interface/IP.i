%module (package = "PyCamellia") IP
%{
#include "IP.h"
%}

%include "Camellia.i"

%nodefaultctor IP;

class IP {
public:
void addTerm(LinearTermPtr a);
void addTerm(VarPtr v);
LinearTermPtr evaluate(map< int, FunctionPtr> &varFunctions);

static IPPtr ip();

%extend {
  LinearTermPtr evaluate(const map<int, FunctionPtr> &varFunctions) {
    map<int, FunctionPtr> varFunctionsCopy = varFunctions;
    return self->evaluate(varFunctionsCopy);
  }
}
};

class IPPtr {
public:
  IP* operator->();
};
