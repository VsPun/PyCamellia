%module (package = "PyCamellia") StokesVGPFormulation
%{
#include "StokesVGPFormulation.h"
%}

%include "Camellia.i"

class StokesVGPFormulation {
public:
  StokesVGPFormulation(int spaceDim, bool useConformingTraces, double mu = 1.0);
  
  // ! the Stokes VGP formulation bilinear form
  BFPtr bf();
  
  // ! sets a wall boundary condition
  void addWallCondition(SpatialFilterPtr wall);
  
  // ! sets an inflow velocity boundary condition; in 2D and 3D, u should be a vector-valued function.
  void addInflowCondition(SpatialFilterPtr inflowRegion, FunctionPtr u);
  
  // ! sets an outflow velocity boundary condition
  void addOutflowCondition(SpatialFilterPtr outflowRegion);
  
  // ! set a pressure condition at a point
  void addPointPressureCondition();
  
  // ! set a pressure condition at a point
  void addZeroMeanPressureCondition();

  // ! initialize the Solution object(s) using the provided MeshTopology
  void initializeSolution(MeshTopologyPtr meshTopo, int fieldPolyOrder, int delta_k = 1,
                          FunctionPtr forcingFunction = Teuchos::null);
  
  // ! refine according to energy error in the solution
  void refine();
  
  // ! Returns an RHSPtr corresponding to the vector forcing function f and the formulation.
  RHSPtr rhs(FunctionPtr f);
  
  // ! set the RefinementStrategy to use for driving refinements
  void setRefinementStrategy(RefinementStrategyPtr refStrategy);
  
  // ! set current time step used for transient solve
  void setTimeStep(double dt);
  
  // ! Returns the solution (at current time)
  SolutionPtr solution();

  // ! Returns the solution (at previous time)
  SolutionPtr solutionPreviousTimeStep();
  
  // ! Solves
  void solve();
  
  // ! Takes a time step
  void takeTimeStep();
  
  // ! Returns the sum of the time steps taken thus far.
  double getTime();
  
  // ! Returns a FunctionPtr which gets updated with the current time.  Useful for setting BCs that vary in time.
  FunctionPtr getTimeFunction();

  // field variables:
  VarPtr sigma(int i);
  VarPtr u(int i);
  VarPtr p();
  
  // traces:
  VarPtr tn_hat(int i);
  VarPtr u_hat(int i);
  
  // test variables:
  VarPtr tau(int i);
  VarPtr v(int i);
};
