%module (package = "PyCamellia") Solution
%{
#include "Solution.h"
%}

%include "Camellia.i"

using namespace std;

%nodefaultctor Solution;

class Solution {
 public:
  static SolutionPtr solution(MeshPtr mesh, BCPtr bc = Teuchos::null,
                              RHSPtr rhs = Teuchos::null, IPPtr ip = Teuchos::null);
  int solve();
  void addSolution(SolutionPtr soln, double weight,
                   bool allowEmptyCells = false, bool replaceBoundaryTerms=false);
  void addSolution(SolutionPtr soln, double weight,
                   set<int> varsToAdd, bool allowEmptyCells = false);
  void clear();
  int cubatureEnrichmentDegree();
  void setCubatureEnrichmentDegree(int value);
  double L2NormOfSolution(int trialID);
  void projectOntoMesh(const std::map<int, FunctionPtr > &functionMap);
  double energyErrorTotal();
  void setWriteMatrixToFile(bool value, const std::string &filePath);
  void setWriteMatrixToMatrixMarketFile(bool value,const std::string &filePath);
  void setWriteRHSToMatrixMarketFile(bool value, const std::string &filePath);
  MeshPtr mesh();
  BCPtr bc();
  RHSPtr rhs();
  IPPtr ip();
  void setBC( BCPtr );
  void setRHS( RHSPtr );
  void setIP( IPPtr );
  void save(std::string meshAndSolutionPrefix);
  static SolutionPtr load(BFPtr bf, std::string meshAndSolutionPrefix);
  void saveToHDF5(std::string filename);
  void loadFromHDF5(std::string filename);
  void setUseCondensedSolve(bool value);
};

class SolutionPtr {
public:
  Solution* operator->();
};
