%module RHS
%{
#include "RHS.h"
 %}

%include "std_string.i"

%nodefaultctor RHS; // Disables the default constructor for class RHS

class RHS {
 public:
  //RHS(bool legacySubclass); 
  static RHSPtr rhs();

  bool nonZeroRHS(int testVarID);
  
  void addTerm(LinearTermPtr rhsTerm);
  void addTerm(VarPtr v);
  
  LinearTermPtr linearTerm();
  LinearTermPtr linearTermCopy();

};

class RHSPtr {
 public:
  RHS* operator->();
};


