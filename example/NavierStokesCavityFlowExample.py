from PyCamellia import *
spaceDim = 2
Re = 1000.0
dims = [1.0,1.0]
numElements = [2,2]
x0 = [0.,0.]
meshTopo = MeshFactory.rectilinearMeshTopology(dims,numElements,x0)
polyOrder = 3
delta_k = 1

form = NavierStokesVGPFormulation(meshTopo,Re,polyOrder,delta_k)

form.addZeroMeanPressureCondition()

topBoundary = SpatialFilter.matchingY(1.0)
notTopBoundary = SpatialFilter.negatedFilter(topBoundary)

x = Function.xn(1)
rampWidth = 1./64
H_left = Function.heaviside(rampWidth)
H_right = Function.heaviside(1.0-rampWidth);
ramp = (1-H_right) * H_left + (1./rampWidth) * (1-H_left) * x + (1./rampWidth) * H_right * (1-x)

zero = Function.constant(0)
topVelocity = Function.vectorize(ramp,zero)

form.addWallCondition(notTopBoundary)
form.addInflowCondition(topBoundary,topVelocity)

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

threshold = .01
maxRefs = 3
while energyError > threshold and refinementNumber <= maxRefs:
  form.hRefine()
  nonlinearSolve(maxSteps)
  energyError = form.solutionIncrement().energyErrorTotal()
  refinementNumber += 1
  elementCount = mesh.numActiveElements()
  globalDofCount = mesh.numGlobalDofs()
  print("Energy error after %i refinements: %0.3f" % (refinementNumber, energyError))
  print("Mesh has %i elements and %i degrees of freedom." % (elementCount, globalDofCount))

exporter = HDF5Exporter(form.solution().mesh(), "steadyNavierStokes", ".")
exporter.exportSolution(form.solution(),0)
