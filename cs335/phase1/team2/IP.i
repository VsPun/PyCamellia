%module IP
%{
#include "IP.h"
%}


class IP{
public:
  IP();
  void addTerm(LinearTermPtr a);
  void addTerm(VarPtr v);
  LinearTermPtr evaluate(map< int, FunctionPtr> &varFunctions);
};
