%module IP
%{
#include "IP.h"
%}

%include "std_string.i"
%nodefaultctor IP; 

class IP{
public:
static IPPtr ip();
void addTerm(LinearTermPtr a);
void addTerm(VarPtr v);
LinearTermPtr evaluate(map< int, FunctionPtr> &varFunctions);
};

class IPPtr {
public:
  IP* operator->();
};
