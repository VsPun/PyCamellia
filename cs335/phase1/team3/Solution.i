%module Solution
%{
#include "Solution.h"
%}


%include "std_string.i"
%include "std_vector.i"
%include "std_set.i"
%include "std_map.i"

namespace std {
  %template(DoubleVector) vector<double>;
  %template(IntVector) vector<int>;
  %template(IntSet) set<int>;
  %template(UnsignedSet) set<unsigned>;
  %template(MapIntToFunction) map<int,FunctionPtr>;
}
using namespace std;

class Solution {
 public:
 
  static SolutionPtr solution(MeshPtr mesh, BCPtr bc = Teuchos::null,
                              RHSPtr rhs = Teuchos::null, IPPtr ip = Teuchos::null);
  int solve();
  void addSolution(SolutionPtr soln, double weight,
		   bool allowEmptyCells = false, bool replaceBoundaryTerms = false);
  void addSolution(SolutionPtr soln, double weight,
		   set<int> varsToAdd, bool allowEmptyCells = false); 
  void clear();
  int cubatureEnrichmentDegree();
  void setCubatureEnrichmentDegree(int value);
  double L2NormOfSolution(int trialID);
  void projectOntoMesh(const map<int, FunctionPtr > &functionMap);
  double energyErrorTotal();
  void setWriteMatrixToFile(bool value,const string &filePath);
  void setWriteMatrixToMatrixMarketFile(bool value,const string &filePath);
  void setWriteRHSToMatrixMarketFile(bool value, const string &filePath);
  MeshPtr mesh();
  BCPtr bc();
  RHSPtr rhs();
  IPPtr ip();
  void setBC( BCPtr );
  void setRHS( RHSPtr );
  void setIP( IPPtr );
  void save(string meshAndSolutionPrefix);
  static SolutionPtr load(BFPtr bf, string meshAndSolutionPrefix);
  void saveToHDF5(string filename);
  void loadFromHDF5(string filename);
 };

typedef Teuchos::RCP<Solution> SolutionPtr;


class SolutionPtr {
public:
  Solution* operator->();
};
