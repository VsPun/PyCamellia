%module (package = "PyCamellia") NavierStokesVGPFormulation
%{
#include "NavierStokesVGPFormulation.h"
%}

%include "Camellia.i"

class NavierStokesVGPFormulation {
public:
  NavierStokesVGPFormulation(MeshTopologyPtr meshTopology, double Re, int fieldPolyOrder, int delta_k = 1,
                             FunctionPtr forcingFunction = Teuchos::null, bool transientFormulation = false,
                             bool useConformingTraces = false);

  NavierStokesVGPFormulation(std::string prefixString, int spaceDim, double Re, int fieldPolyOrder, int delta_k = 1,
                             FunctionPtr forcingFunction = Teuchos::null, bool transientFormulation = false,
                             bool useConformingTraces = false);

  // ! the NavierStokes VGP formulation bilinear form
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
  
  // ! returns the L^2 norm of the incremental solution
  double L2NormSolutionIncrement();
  
  // ! returns the L^2 norm of the background flow
  double L2NormSolution();
  
  // ! returns the nonlinear iteration count (since last refinement)
  int nonlinearIterationCount();
  
  // ! refine according to energy error in the solution
  void refine();
  
  // ! h-refine according to energy error in the solution
  void hRefine();
  
  // ! p-refine according to energy error in the solution
  void pRefine();
  
  // ! Returns an RHSPtr corresponding to the vector forcing function f and the formulation.
  RHSPtr rhs(FunctionPtr f, bool excludeFluxesAndTraces);
  
  // ! Saves the solution(s) and mesh to an HDF5 format.
  void save(std::string prefixString);

  // ! set current time step used for transient solve
  void setTimeStep(double dt);
  
  // ! Returns the background flow, i.e. the accumulated solution thus far
  SolutionPtr solution();
  
  // ! Returns the latest solution increment
  SolutionPtr solutionIncrement();
  
  // ! The first time this is called, calls solution()->solve(), and the weight argument is ignored.  After the first call, solves for the next iterate, and adds to background flow with the specified weight.
  void solveAndAccumulate(double weight=1.0);
  
  // ! Returns the variable in the stream solution that represents the stream function.
  VarPtr streamPhi();
  
  // ! Returns the stream solution (at current time).  (Stream solution is created during initializeSolution, but
  // ! streamSolution->solve() must be called manually.)  Use streamPhi() to get a VarPtr for the streamfunction.
  SolutionPtr streamSolution();
  
  // ! Takes a time step
//  void takeTimeStep();
  
  // ! Returns the sum of the time steps taken thus far.
//  double getTime();
  
  // ! Returns a FunctionPtr which gets updated with the current time.  Useful for setting BCs that vary in time.
//  FunctionPtr getTimeFunction();

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
