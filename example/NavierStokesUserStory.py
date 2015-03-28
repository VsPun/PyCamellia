from PyCamellia import *
spaceDim = 2
Re = 800.0
dims = [8.0,2.0]
numElements = [8,2]
x0 = [0.,0.]
meshTopo = MeshFactory.rectilinearMeshTopology(dims,numElements,x0)
polyOrder = 3
delta_k = 1

form = NavierStokesVGPFormulation(meshTopo,Re,polyOrder,delta_k)

form.addZeroMeanPressureCondition()

inflow = SpatialFilter.matchingX(0.0) and SpatialFilter.greaterThanY(1.0)
outflow = SpatialFilter.matchingX(8.0)
wall = SpatialFilter.negatedFilter(inflow or outflow)

y = Function.yn(1)
inflowVelocity_x = -3*(y-1)*(y-2)
inflowVelocity_y = Function.constant(0.0)
inflowVelocity = Function.vectorize(inflowVelocity_x,inflowVelocity_y)

form.addWallCondition(wall)
form.addOutflowCondition(outflow)
form.addInflowCondition(inflow,inflowVelocity)

refinementNumber = 0

nonlinearThreshold = 1e-3

#define a local method that will do the nonlinear iteration:
def nonlinearSolve(maxSteps):
  normOfIncrement = 1
  stepNumber = 0
  while normOfIncrement > nonlinearThreshold and stepNumber < maxSteps:
    form.solveAndAccumulate()
    normOfIncrement = form.L2NormSolutionIncrement()
    print("L^2 norm of increment: %0.3f" % normOfIncrement)
    stepNumber += 1

maxSteps = 10
nonlinearSolve(maxSteps)
mesh = form.solution().mesh();

energyError = form.solutionIncrement().energyErrorTotal()
elementCount = mesh.numActiveElements()
globalDofCount = mesh.numGlobalDofs()
print("Initial mesh has %i elements and %i degrees of freedom." % (elementCount, globalDofCount))
print("Energy error after %i refinements: %0.3f" % (refinementNumber, energyError))
