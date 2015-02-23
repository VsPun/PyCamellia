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
LinearTermPtr evaluate(const map< int, FunctionPtr> &varFunctions);

static IPPtr ip();
};

class IPPtr {
public:
  IP* operator->();
};
