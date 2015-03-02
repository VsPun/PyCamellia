%module (package = "PyCamellia") Function
%{
#include "Function.h"
#include "Intrepid_FieldContainer.hpp"
#include "BasisCache.h"
%}

%include "Camellia.i"
%include "Mesh.i"
%include "Solution.i"

%nodefaultctor Function;  // Disable the default constructor for class Function

using namespace std;

class Function {
public:
  string displayString();
  double evaluate(double x);
  double evaluate(double x, double y);
  double evaluate(double x, double y, double z);
  
  virtual FunctionPtr x();
  virtual FunctionPtr y();
  virtual FunctionPtr div();
  int rank();
  double l2norm(MeshPtr mesh, int cubatureDegreeEnrichment = 0);
  
  // member functions for taking derivatives:
  FunctionPtr dx();
  FunctionPtr dy();

  FunctionPtr grad();

  // static methods:
  static double evaluate(FunctionPtr f, double x, double y); 
  
  static FunctionPtr xn(int n=1); // NOTE: important to have "FunctionPtr" here exactly as below; "Teuchos::RCP<Function>", though equivalent in C++, is not equivalent for SWIG
  static FunctionPtr yn(int n=1);
  
  static FunctionPtr composedFunction(FunctionPtr f, FunctionPtr g);
  static FunctionPtr constant(double value);
  static FunctionPtr heaviside(double xShift);
  static FunctionPtr vectorize(FunctionPtr f1, FunctionPtr f2);
  static FunctionPtr normal();
  static FunctionPtr solution(VarPtr var, SolutionPtr soln);

  // SWIG/Python extensions:
  %extend {
    string __str__() {
      return self->displayString();
    }
    pair<vector<double>,vector<vector<double> > > getCellValues(MeshPtr mesh, int cellID, const vector< vector<double> > &refPoints) {
      using namespace Intrepid;
      pair<vector<double>,vector<vector<double> > > emptyReturnValue = make_pair(vector<double>(), vector<vector<double> >());
      if (self->rank() != 0) {
        cout << "Error: getCellValues() only supports scalar-valued Functions.\n";
        return emptyReturnValue;
      }
      
      int spaceDim = mesh->getTopology()->getSpaceDim();
      int numPoints = refPoints.size();
      FieldContainer<double> refPointsFC(numPoints,spaceDim);
      for (int pointOrdinal=0; pointOrdinal<numPoints; pointOrdinal++) {
        if (refPoints[pointOrdinal].size() != spaceDim) {
          cout << "Error: refPoints[" << pointOrdinal << "].size() != spaceDim = " << spaceDim << endl;
          return emptyReturnValue;
        }
        for (int d=0; d<spaceDim; d++) {
          refPointsFC(pointOrdinal,d) = refPoints[pointOrdinal][d];
        }
      }
      BasisCachePtr basisCache = BasisCache::basisCacheForCell(mesh, cellID);
      basisCache->setRefCellPoints(refPointsFC);
      
      int numCells = 1;
      FieldContainer<double> valuesFC(numCells,numPoints);
      self->values(valuesFC,basisCache);
      vector<double> values(numPoints);
      vector< vector<double> > physicalPoints(numPoints);
      vector<double> point(spaceDim);
      FieldContainer<double> physicalPointsFC = basisCache->getPhysicalCubaturePoints();
      for (int pointOrdinal=0; pointOrdinal<numPoints; pointOrdinal++) {
        values[pointOrdinal] = valuesFC(0,pointOrdinal);
        for (int d=0; d<spaceDim; d++) {
          point[d] = physicalPointsFC(0,pointOrdinal,d);
        }
        physicalPoints[pointOrdinal] = point;
      }
      return make_pair(values,physicalPoints);
    }
  }
};

//FunctionPtr operator*(double weight, FunctionPtr f);

class FunctionPtr {
public:
  Function* operator->();

  %extend {
    FunctionPtr __add__(FunctionPtr f2) {
      return *self + f2;
    }
    FunctionPtr __add__(double value) {
      return *self + value;
    }
    FunctionPtr __radd__(double value) {
      return *self + value;
    }
    FunctionPtr __mul__(double value) {
      return *self * value;
    }
    FunctionPtr __rmul__(double value) {
      return *self * value;
    }
    FunctionPtr __sub__(FunctionPtr f2) {
      return *self - f2;
    }
    FunctionPtr __sub__(double value) {
      return *self - value;
    }
    FunctionPtr __rsub__(double value) {
      return value - *self;
    }
    FunctionPtr __mul__(FunctionPtr f2) {
      return *self * f2;
    }
    FunctionPtr __div__(FunctionPtr scalarDivision) {
      return *self / scalarDivision;
    }
    FunctionPtr __div__(double divisor) {
      return *self / divisor;
    }
    FunctionPtr __rdiv__(double value) {
      return value / *self;
    }
    FunctionPtr __mul__(vector<double> weight) {
      return *self * weight;
    }
    FunctionPtr __rmul__(vector<double> weight) {
      return weight * *self;
    }
    FunctionPtr __neg__() {
      return -1 * *self;
    }
  }
};
