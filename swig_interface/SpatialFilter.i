%module SpatialFilter
%{
#include "SpatialFilter.h"
%}

%include "std_string.i"
%include "std_vector.i"

namespace std {
  %template(DoubleVector) vector<double>;
}

%nodefaultctor SpatialFilter;

using namespace std;

class SpatialFilter {
public:
  virtual bool matchesPoint(double x, double y);
  virtual bool matchesPoint(vector<double> &point); 
  static SpatialFilterPtr allSpace();  
  static SpatialFilterPtr unionFilter(SpatialFilterPtr a, SpatialFilterPtr b);
  static SpatialFilterPtr intersectionFilter(SpatialFilterPtr a, SpatialFilterPtr b);
  static SpatialFilterPtr negatedFilter(SpatialFilterPtr filterToNegate); 
  static SpatialFilterPtr matchingX(double x);
  static SpatialFilterPtr matchingY(double y);
  static SpatialFilterPtr lessThanX(double x);
  static SpatialFilterPtr lessThanY(double y);
  static SpatialFilterPtr greaterThanX(double x);
  static SpatialFilterPtr greaterThanY(double y);
  %extend {
    bool matchesPoint(const vector<double> &point) {
      vector<double> pointCopy = point;
      return self->matchesPoint(pointCopy);
    } 
  }
};

//FunctionPtr operator*(double weight, FunctionPtr f);

class SpatialFilterPtr {
public:
  SpatialFilter* operator->();

  %extend {
    SpatialFilterPtr __or__(SpatialFilterPtr b) {
      return SpatialFilter::unionFilter(*self,b);
    }
    SpatialFilterPtr __and__(SpatialFilterPtr b) {
      return SpatialFilter::intersectionFilter(*self,b);
    }
  }
};
