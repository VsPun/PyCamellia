%module RHS
%{
#include "RHS.h"
 %}

%include "std_strings.i"

%nodefaultctor RHS; // Disables the default constructor for class RHS

class RHS {
 public:
  RHS(bool legacySubclass); 
  RHS(){ // specification said Python interface would not require the legacy bool and always pass false
    return RHS(false);
  }

  bool nonZeroRHS(int testVarID);
  
  void addTerm(LinearTermPtr rhsTerm);
  void addTerm(VarPtr v);
  
  LinearTermPtr linearTerm();
  LinearTermPtr linearTermCopy();
};
