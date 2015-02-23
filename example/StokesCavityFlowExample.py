from PyCamellia import *
spaceDim = 2
useConformingTraces = False
form = StokesVGPFormulation(spaceDim,useConformingTraces)
dims = [1.0,1.0]
numElements = [2,2]
x0 = [0.,0.]
meshTopo = MeshFactory.rectilinearMeshTopology(dims,numElements,x0)
polyOrder = 2
delta_k = 1

form.initializeSolution(meshTopo,polyOrder,delta_k)

form.addZeroMeanPressureCondition()

topBoundary = SpatialFilter.matchingY(1.0)
notTopBoundary = SpatialFilter.negatedFilter(topBoundary)

x2 = Function.xn(2)
zero = Function.constant(0)
topVelocity = Function.vectorize(4*x2-1,zero)

form.addWallCondition(notTopBoundary)
form.addInflowCondition(topBoundary,topVelocity)

refinementNumber = 0
form.solve()

energyError = form.solution().energyErrorTotal()
print("Energy error after %i refinements: %0.3f" % (refinementNumber, energyError))

threshold = 0.2
while energyError > threshold:
  form.refine()
  form.solve()
  energyError = form.solution().energyErrorTotal()
  refinementNumber += 1
  print("Energy error after %i refinements: %0.3f" % (refinementNumber, energyError))

exporter = HDF5Exporter(form.solution().mesh(), "steadyStokes", ".")
exporter.exportSolution(form.solution(),0)

